# Applying geometric transforms to images

**Framework**: Accelerate

Reflect, shear, rotate, and scale image buffers using vImage.

#### Overview

The vImage library provides a suite of functions to apply different geometric transforms to images. The image below shows examples of reflect, scale, rotate, and composite translate-rotate-scale transforms:

![Four variations of the same photograph of flowers. The first is horizontally reflected. The second is scaled down. The third is rotated clockwise. The fourth is rotated counterclockwise and scaled down to fit within its bounding box.](https://docs-assets.developer.apple.com/published/309bf547b80ae68f85e23a0d77eeaf11/media-3682459%402x.png)

By default, vImage uses the Lanczos-3 algorithm when resampling. If you need the higher-quality results of the Lanczos-5 algorithm and don’t mind slightly slower performance, pass the [`kvImageHighQualityResampling`](kvimagehighqualityresampling.md) flag to the geometric transform operations.

The vImage geometry operations don’t work in-place, that is, you can’t use the same buffer as the source and destination.

If you’re applying a geometric transform to an image with premultiplied alpha, you may see artifacts in high-frequency regions of the image. To avoid these artifacts, call [`vImageUnpremultiplyData_ARGB8888(_:_:_:)`](vimageunpremultiplydata_argb8888(_:_:_:).md) to remove the premultiplied alpha value from the image data before the operation. After the operation, call [`vImagePremultiplyData_ARGB8888(_:_:_:)`](vimagepremultiplydata_argb8888(_:_:_:).md) to premultiply the result.

##### Reflect a Vimage Buffer

The vImage reflect functions generate either a vertical or a horizontal reflection of the image. The image below shows the original buffer contents and the contents after vertical reflection:

![Two variations of the same photograph of a rocky landscape. The second image is vertically reflected so that it appears upside down.](https://docs-assets.developer.apple.com/published/99488eea71ad42c75c291574b24371bc/media-3682698%402x.png)

The destination buffer you pass to the vImage reflect functions needs to be the same size as the source buffer. The code below uses a precondition to ensure that both buffer sizes match:

```swift
static func verticalReflectBuffer(source: vImage_Buffer,
                                  destination: inout vImage_Buffer) {
    
    precondition(source.size == destination.size,
                 "Source and destination buffers need to have the same size.")
    
    _ = withUnsafePointer(to: source) { srcPointer in
        vImageVerticalReflect_ARGB8888(srcPointer,
                                       &destination,
                                       vImage_Flags(kvImageNoFlags))
    }
}
```

To learn more about reflection functions, see [`Image reflection`](image-reflection.md).

##### Shear a Vimage Buffer

The vImage shear functions scale and offset an image in one dimension. These functions accept a resampling filter that you use for fine control over the resampling algorithm. For more information on resampling, see [`Reducing artifacts with custom resampling filters`](reducing-artifacts-with-custom-resampling-filters.md).

![A sheared photograph of flowers. The image appears as a diagonal stripe across its background.](https://docs-assets.developer.apple.com/published/d32725171f1a1966018c441f8967df27/media-3682695%402x.png)

Control the amount of shear by specifying the `shearSlope` parameter. The functions define the shear slope as `deltaᵧ/deltaₓ` that’s the slope for a linear function `y = slope * x`. The `verticalShearBuffer(source:destination:byAngleInDegrees:verticalScale:backgroundColor:)` function accepts the shear as an angle in degrees and performs the transform.

```swift
static func verticalShearBuffer(source: vImage_Buffer,
                                destination: inout vImage_Buffer,
                                byAngleInDegrees angleInDegrees: Double,
                                verticalScale: Float = 1,
                                backgroundColor: [Pixel_8] = [0, 127, 127, 127]) {
    
    // 1. Ensure the shear angle is valid.
    precondition(angleInDegrees > -90 && angleInDegrees < 90,
                 "The shear angle needs to be greater than -90º and less than 90º.")
    
    // 2. Calculate `shearSlope` as the tangent of the specified angle.
    let angle = Measurement(value: angleInDegrees,
                            unit: UnitAngle.degrees)
    let radians = Float(angle.converted(to: .radians).value)
    let shearSlope = tan(radians)

    // 3. Create a default resampling filter using the specified scale.
    let resamplingFilter = vImageNewResamplingFilter(verticalScale,
                                                     vImage_Flags(kvImageNoFlags))
    defer {
        vImageDestroyResamplingFilter(resamplingFilter)
    }
    
    // 4. Apply the transform to `source` and write the result to `destination`.
    _ = withUnsafePointer(to: source) { srcPointer in
        vImageVerticalShear_ARGB8888(srcPointer,
                                     &destination,
                                     0, 0,
                                     0,
                                     shearSlope,
                                     resamplingFilter,
                                     backgroundColor,
                                     vImage_Flags(kvImageBackgroundColorFill))
    }
}
```

To fit the sheared image in a buffer with the same dimensions as the original image, specify a shear angle that’s the arctangent of the image’s height divided by twice its width.

```swift
let shearAngle = atan(Double(sourceImageBuffer.height) /
                      Double(sourceImageBuffer.width * 2)) *
                      180 / .pi

verticalShearBuffer(source: sourceImageBuffer,
                    destination: &destinationImageBuffer,
                    byAngleInDegrees: shearAngle,
                    verticalScale: 0.5)
```

On return, the destination buffer contains the image below:

![A sheared photograph of a rocky landscape. The image appears as a diagonal stripe across its background.](https://docs-assets.developer.apple.com/published/ac3efa8af8ea29ca9a85257f5edd31fb/media-3682697%402x.png)

To learn more about shearing functions, see [`Image shearing`](image-shearing.md).

##### Rotate a Vimage Buffer By Multiples of 90%c2%b0

The vImage library provides 90° rotation functions that perform a simple 0°, 90°, 180°, or 270° rotation of an image around its center. The image below shows a buffer’s contents without any rotation, rotated 90° counterclockwise, rotated 180°, and rotated 90° clockwise:

![Four variations of a photograph of a flower, rotated in 90 degree counterclockwise increments.](https://docs-assets.developer.apple.com/published/0936b3bc110e1c8f6fe55732ce6d8d08/media-3682700%402x.png)

Note that the 90° and 270° rotations don’t rotate around the true center of the image when the parity (that is, whether an integer is even or odd) of the source width and destination height don’t match. The same is true if the parity of the source height and destination width don’t match.

If the source and destination buffers are different sizes, the 0° and 180° rotations require that the two heights have the same parity and the two widths have the same parity.

The 90° rotation function crops source pixels that lie outside the destination buffer and fills destination pixels with the specified background color when source pixels don’t cover them.

The function below applies a multiple of 90° rotation to a buffer and returns the result in a correctly oriented destination buffer:

```swift
static func rotateNinety(source: vImage_Buffer,
                         rotation: Int) -> vImage_Buffer? {

    // 1. Create the destination buffer.
    guard var destination: vImage_Buffer = {
        switch rotation {
            case kRotate0DegreesClockwise, kRotate180DegreesClockwise:
                return try? vImage_Buffer(size: source.size,
                                          bitsPerPixel: 8 * 4)
            case kRotate90DegreesClockwise, kRotate270DegreesClockwise:
                return try? vImage_Buffer(width: Int(source.size.height),
                                          height: Int(source.size.width),
                                          bitsPerPixel: 8 * 4)
            default:
                NSLog("Unsupported rotation constant: \(rotation).")
                return nil
        }
    }() else {
        NSLog("Unable to initialize destination buffer.")
        return nil
    }
    
    // 2. Apply the transform to `source` and write the result to `destination`.
    _ = withUnsafePointer(to: source) { sourcePtr in
        vImageRotate90_ARGB8888(sourcePtr,
                                &destination,
                                UInt8(rotation),
                                [0],
                                vImage_Flags(kvImageNoFlags))
    }
    
    return destination
}
```

To learn more about rotation functions, see [`Image rotation`](image-rotation.md).

##### Rotate a Vimage Buffer By an Arbitrary Angle

The vImage library provides rotation functions that rotate an image by any angle around its center. The image below shows a buffer rotated 60° counterclockwise:

![A rotated photograph of some squashes.](https://docs-assets.developer.apple.com/published/37ab4672533109aaaa41288159836fbe/media-3682702%402x.png)

The function below rotates a buffer by the specified angle and writes the result to the destination:

```swift
static func rotateBuffer(source: vImage_Buffer,
                         destination: inout vImage_Buffer,
                         byAngleInDegrees angleInDegrees: Double,
                         backgroundColor: [Pixel_8] = [0, 127, 127, 127]) {
    
    let angle = Measurement(value: angleInDegrees,
                            unit: UnitAngle.degrees)
    let radians = Float(angle.converted(to: .radians).value)
    
    _ = withUnsafePointer(to: source) { srcPointer in
        vImageRotate_ARGB8888(srcPointer,
                              &destination,
                              nil,
                              radians,
                              backgroundColor,
                              vImage_Flags(kvImageBackgroundColorFill))
    }
}
```

##### Scale a Vimage Buffer

The vImage library provides functions to scale the contents of an image buffer. The scaling can either be uniform, where the operation preserves the image’s aspect ratio, or nonuniform, where the operation stretches or condenses the image. The image below shows four scaled versions of the same photograph, with the second and third image scaled nonuniformly:

![Four variations of a scaled photograph of flowers.](https://docs-assets.developer.apple.com/published/ac3522a7ff2cbc3fb7b20363ba958857/media-3682710%402x.png)

The vImage scale functions accept source and destination buffers as parameters and rescale the source to fill the destination buffer. The function below wraps [`vImageScale_ARGB8888(_:_:_:_:)`](vimagescale_argb8888(_:_:_:_:).md) to provide a simple interface to the scale operation:

```swift
static func scaleBuffer(source: vImage_Buffer,
                        destination: inout vImage_Buffer) {
    
    _ = withUnsafePointer(to: source) { sourcePointer in
        vImageScale_ARGB8888(sourcePointer,
                             &destination,
                             nil,
                             vImage_Flags(kvImageNoFlags))
    }
}
```

To learn more about scaling functions, see [`Image scaling`](image-scaling.md).

##### Apply a Simple Affine Transformation to a Vimage Buffer

Use an affine transformation to apply composite transformation, such as a scale and a translate.

A 3-by-3 matrix represents an affine transformation.

![A 3-by-3 matrix.](https://docs-assets.developer.apple.com/published/ad5f4a5c94518f9345389eb1608389cf/media-3682473%402x.png)

Because the third column is always `(0,0,1)`, the [`vImage_CGAffineTransform`](vimage_cgaffinetransform.md) data structure contains values for only the first two columns.

To perform a scale transformation, set the  and  parameters of the matrix to the required scale.

![A 3-by-3 matrix for scaling.](https://docs-assets.developer.apple.com/published/9f887f1de9bbcb61af9992432fb821eb/media-3682474%402x.png)

To perform the translate transformation, set the  and  parameters of the matrix to the required offset.

![A 3 by 3 matrix for translation.](https://docs-assets.developer.apple.com/published/d3f20158f45b6884521dea50065da09b/media-3682475%402x.png)

The `scaleAndCenterBuffer(source:destination:to:backgroundColor:)` function accepts a scale parameter and sets that parameter as the  and  parameters of the matrix.

```swift
static func scaleAndCenterBuffer(source: vImage_Buffer,
                                 destination: inout vImage_Buffer,
                                 to scale: Double,
                                 backgroundColor: [Pixel_8] = [0, 127, 127, 127]) {
    
    // 1. Calculate the translate required to center the scaled buffer.
    let sourceCenter = SIMD2<Double>(
        x: Double(source.size.width / 2),
        y: Double(source.size.height / 2))
    
    let desinationCenter = SIMD2<Double>(
        x: Double(destination.size.width / 2),
        y: Double(destination.size.height / 2))
    
    let tx = desinationCenter.x - sourceCenter.x * scale
    let ty = desinationCenter.y - sourceCenter.y * scale
    
    // 2. Create the affine transformation that represents the scale-translate.
    var vImageTransform = vImage_CGAffineTransform(
        a: scale, b: 0,
        c: 0,     d: scale,
        tx: tx,   ty: ty)

    // 3. Apply the transform to `source` and write the result to `destination`.
    _ = withUnsafePointer(to: source) { srcPointer in
        vImageAffineWarpCG_ARGB8888(srcPointer,
                                    &destination,
                                    nil,
                                    &vImageTransform,
                                    backgroundColor,
                                    vImage_Flags(kvImageBackgroundColorFill))
    }
}
```

The image below shows the result of applying `scaleAndCenterBuffer(_:to:backgroundColor:)` with a scale of `0.25`:

![A photograph of flowers that is scaled down against a colored background.](https://docs-assets.developer.apple.com/published/0e05209f2bda166e82da0667c1a6cf73/media-3682477%402x.png)

To learn more about affine transformation functions, see [`Applying affine transformations to images`](applying-affine-transformations-to-images.md).

##### Apply a Complex Affine Transformation to a Vimage Buffer

For complex transformations, [`CGAffineTransform`](https://developer.apple.com/documentation/CoreFoundation/CGAffineTransform) allows you to concatenate a series of transformations. For example, to rotate and scale an image to fit within its unrotated bounding box, your code needs to translate, rotate, scale, and translate again.

The `rotateAndScaleBuffer(source:destination:byAngleInDegrees:backgroundColor:)` function uses [`CGAffineTransform`](https://developer.apple.com/documentation/CoreFoundation/CGAffineTransform) to build the matrix required to rotate and scale an image to fit inside the bounding box of the destination buffer.

```swift
static func rotateAndScaleBuffer(source: vImage_Buffer,
                                 destination: inout vImage_Buffer,
                                 byAngleInDegrees angleInDegrees: Double,
                                 backgroundColor: [Pixel_8] = [0, 127, 127, 127]) {
    
    // 1. Convert the specified angle in degrees to radians.
    let angle = Measurement(value: angleInDegrees,
                            unit: UnitAngle.degrees)
    let radians = CGFloat(angle.converted(to: .radians).value)
    
    // 2. Calculate the scale based on the bounding box of the rotated image.
    let rotatedBoundingBox = CGRect(origin: .zero, size: source.size)
        .applying(CGAffineTransform(rotationAngle: radians))
    let scale = min(destination.size.width / rotatedBoundingBox.size.width,
                    destination.size.height / rotatedBoundingBox.size.height)
    
    // 3. Create the composite affine transformation.
    let cgTransform = CGAffineTransform.identity
        .translatedBy(x: destination.size.width / 2,
                      y: destination.size.height / 2)
        .rotated(by: radians)
        .scaledBy(x: scale, y: scale)
        .translatedBy(x: -source.size.width / 2,
                      y: -source.size.height / 2)
    
    // 4. Convert the `CGAffineTransform` to a `vImage_CGAffineTransform`.
    var vImageTransform = vImage_CGAffineTransform(
        a: Double(cgTransform.a),
        b: Double(cgTransform.b),
        c: Double(cgTransform.c),
        d: Double(cgTransform.d),
        tx: Double(cgTransform.tx),
        ty: Double(cgTransform.ty))
    
    // 5. Apply the transform to `source` and write the result to `destination`.
    _ = withUnsafePointer(to: source) { srcPointer in
        vImageAffineWarpCG_ARGB8888(srcPointer,
                                    &destination,
                                    nil,
                                    &vImageTransform,
                                    backgroundColor,
                                    vImage_Flags(kvImageBackgroundColorFill))
    }
}
```

The image below shows the result of applying `rotateAndScaleBuffer(_:byAngleInDegrees:backgroundColor:)` with an angle of 30°:

![A rotated photograph of flowers that is scaled down to fit within its bounding box.](https://docs-assets.developer.apple.com/published/b7e65b6d7548bc86dd7120968152052d/media-3682479%402x.png)

##### Optimize Performance with Temporary Buffers

The vImage rotate, scale, and affine transform functions use multiple-pass algorithms that save intermediate pixel values between passes. In some cases, the destination buffer may not be large enough to store that intermediate data, so the operation requires additional, temporary storage.

Pass `nil` to the function to have vImage create and manage this temporary storage for you. For example, the scale function below relies on the operation to manage the temporary buffer:

```swift
static func scaleBuffer(source: vImage_Buffer,
                        destination: inout vImage_Buffer) {
    
    _ = withUnsafePointer(to: source) { sourcePointer in
        vImageScale_ARGB8888(sourcePointer,
                             &destination,
                             nil,
                             vImage_Flags(kvImageNoFlags))
    }
}
```

In cases where your code calls the function frequently (for example, when processing video), create and manage this temporary buffer yourself and reuse it across function calls. Reusing a buffer avoids vImage allocating the temporary storage with each call. Pass [`kvImageGetTempBufferSize`](kvimagegettempbuffersize.md) to your geometry function to calculate the size, in bytes, of the temporary buffer, and use that value to allocate an [`UnsafeMutableRawPointer`](https://developer.apple.com/documentation/Swift/UnsafeMutableRawPointer) structure.

The version of the `scaleBuffer()` function below shows an example of creating a temporary buffer:

```swift
static func scaleBuffer(source: vImage_Buffer,
                        destination: inout vImage_Buffer) {
    
    withUnsafePointer(to: source) { sourcePointer in
        let bufferSize = vImageScale_ARGB8888(sourcePointer,
                                              &destination,
                                              nil,
                                              vImage_Flags(kvImageGetTempBufferSize))
        
        if bufferSize < 0 {
            fatalError("Error calculating buffer size for scale operation (\(bufferSize)).")
        }
        
        // In a real app, you reuse this buffer across multiple calls of `vImageScale_ARGB8888`.
        let temporaryBuffer = UnsafeMutableRawPointer.allocate(byteCount: bufferSize,
                                                               alignment: 64)
        defer {
            temporaryBuffer.deallocate()
        }
        
        vImageScale_ARGB8888(sourcePointer,
                             &destination,
                             temporaryBuffer,
                             vImage_Flags(kvImageNoFlags))
    }
}
```

## See Also

- [Converting bitmap data between Core Graphics images and vImage buffers](converting-bitmap-data-between-core-graphics-images-and-vimage-buffers.md)
  Pass image data between Core Graphics and vImage to create and manipulate images.
- [Creating and Populating Buffers from Core Graphics Images](creating-and-populating-buffers-from-core-graphics-images.md)
  Initialize vImage buffers from Core Graphics images.
- [Creating a Core Graphics Image from a vImage Buffer](creating-a-core-graphics-image-from-a-vimage-buffer.md)
  Create displayable representations of vImage buffers.
- [Building a Basic Image-Processing Workflow](building-a-basic-image-processing-workflow.md)
  Resize an image with vImage.
- [Compositing images with alpha blending](compositing-images-with-alpha-blending.md)
  Combine two images by using alpha blending to create a single output.
- [Compositing images with vImage blend modes](compositing-images-with-vimage-blend-modes.md)
  Combine two images by using blend modes to create a single output.
- [Applying vImage operations to regions of interest](applying-vimage-operations-to-regions-of-interest.md)
  Limit the effect of vImage operations to rectangular regions of interest.
- [Optimizing image-processing performance](optimizing-image-processing-performance.md)
  Improve your app’s performance by converting image buffer formats from interleaved to planar.
- [vImage](vimage-library.md)
  Manipulate large images using the CPU’s vector processor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/applying-geometric-transforms-to-images)*
# Applying geometric transforms to images

**Framework**: Accelerate  
**Role**: Article

Reflect, shear, rotate, and scale image buffers using vImage.

## Overview

The vImage library provides a suite of functions to apply different geometric transforms to images. The image below shows examples of reflect, scale, rotate, and composite translate-rotate-scale transforms:

![Four variations of the same photograph of flowers. The first is horizontally reflected. The second is scaled down. The third is rotated clockwise. The fourth is rotated counterclockwise and scaled down to fit within its bounding box.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3682459@2x.png)

By default, vImage uses the Lanczos-3 algorithm when resampling. If you need the higher-quality results of the Lanczos-5 algorithm and don’t mind slightly slower performance, pass the [`kvImageHighQualityResampling`](./kvimagehighqualityresampling.md) flag to the geometric transform operations.

The vImage geometry operations don’t work in-place, that is, you can’t use the same buffer as the source and destination.

If you’re applying a geometric transform to an image with premultiplied alpha, you may see artifacts in high-frequency regions of the image. To avoid these artifacts, call [`vImageUnpremultiplyData_ARGB8888(_:_:_:)`](./vimageunpremultiplydata_argb8888%28_,_,_%29.md) to remove the premultiplied alpha value from the image data before the operation. After the operation, call [`vImagePremultiplyData_ARGB8888(_:_:_:)`](./vimagepremultiplydata_argb8888%28_,_,_%29.md) to premultiply the result.

### Reflect a vImage buffer

The vImage reflect functions generate either a vertical or a horizontal reflection of the image. The image below shows the original buffer contents and the contents after vertical reflection:

![Two variations of the same photograph of a rocky landscape. The second image is vertically reflected so that it appears upside down.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3682698@2x.png)

The destination buffer you pass to the vImage reflect functions needs to be the same size as the source buffer. The code below uses a precondition to ensure that both buffer sizes match:

**Swift**:

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

**Objective-C**:

```objc
void verticalReflectBuffer(const vImage_Buffer *source,
                           vImage_Buffer *destination) {

    NSCAssert(source->width == destination->width &&
              source->height == destination->height,
              @"Source and destination buffers need to have the same size.");

    vImageVerticalReflect_ARGB8888(source,
                                   destination,
                                   kvImageNoFlags);
}
```

To learn more about reflection functions, see [Image reflection](./image-reflection.md).

### Shear a vImage buffer

The vImage shear functions scale and offset an image in one dimension. These functions accept a resampling filter that you use for fine control over the resampling algorithm. For more information on resampling, see [Reducing artifacts with custom resampling filters](./reducing-artifacts-with-custom-resampling-filters.md).

![A sheared photograph of flowers. The image appears as a diagonal stripe across its background.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3682695@2x.png)

Control the amount of shear by specifying the `shearSlope` parameter. The functions define the shear slope as `deltaᵧ/deltaₓ` that’s the slope for a linear function `y = slope * x`. The `verticalShearBuffer(source:destination:byAngleInDegrees:verticalScale:backgroundColor:)` function accepts the shear as an angle in degrees and performs the transform.

**Swift**:

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

**Objective-C**:

```objc
void verticalShearBuffer(const vImage_Buffer *source,
                         vImage_Buffer *destination,
                         double angleInDegrees,
                         float verticalScale,
                         const Pixel_8888 backgroundColor) {

    // 1. Ensure the shear angle is valid.
    NSCAssert(angleInDegrees > -90 && angleInDegrees < 90,
              @"The shear angle needs to be greater than -90° and less than 90°.");

    // 2. Calculate `shearSlope` as the tangent of the specified angle.
    float radians = (float)(angleInDegrees * M_PI / 180.0);
    float shearSlope = tanf(radians);

    // 3. Create a default resampling filter using the specified scale.
    ResamplingFilter resamplingFilter = vImageNewResamplingFilter(verticalScale,
                                                                  kvImageNoFlags);

    // 4. Apply the transform to `source` and write the result to `destination`.
    vImageVerticalShear_ARGB8888(source,
                                 destination,
                                 0, 0,
                                 0,
                                 shearSlope,
                                 resamplingFilter,
                                 backgroundColor,
                                 kvImageBackgroundColorFill);

    vImageDestroyResamplingFilter(resamplingFilter);
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

![A sheared photograph of a rocky landscape. The image appears as a diagonal stripe across its background.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3682697@2x.png)

To learn more about shearing functions, see [Image shearing](./image-shearing.md).

### Rotate a vImage buffer by multiples of 90°

The vImage library provides 90° rotation functions that perform a simple 0°, 90°, 180°, or 270° rotation of an image around its center. The image below shows a buffer’s contents without any rotation, rotated 90° counterclockwise, rotated 180°, and rotated 90° clockwise:

![Four variations of a photograph of a flower, rotated in 90 degree counterclockwise increments.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3682700@2x.png)

Note that the 90° and 270° rotations don’t rotate around the true center of the image when the parity (that is, whether an integer is even or odd) of the source width and destination height don’t match. The same is true if the parity of the source height and destination width don’t match.

If the source and destination buffers are different sizes, the 0° and 180° rotations require that the two heights have the same parity and the two widths have the same parity.

The 90° rotation function crops source pixels that lie outside the destination buffer and fills destination pixels with the specified background color when source pixels don’t cover them.

The function below applies a multiple of 90° rotation to a buffer and returns the result in a correctly oriented destination buffer:

**Swift**:

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

**Objective-C**:

```objc
vImage_Buffer *rotateNinety(const vImage_Buffer *source, int rotation) {

    // 1. Create the destination buffer.
    vImage_Buffer *destination = malloc(sizeof(vImage_Buffer));
    if (!destination) {
        return NULL;
    }

    vImage_Error initError;
    if (rotation == kRotate0DegreesClockwise || rotation == kRotate180DegreesClockwise) {
        initError = vImageBuffer_Init(destination,
                                     source->height,
                                     source->width,
                                     8 * 4,
                                     kvImageNoFlags);
    } else if (rotation == kRotate90DegreesClockwise || rotation == kRotate270DegreesClockwise) {
        initError = vImageBuffer_Init(destination,
                                     source->width,
                                     source->height,
                                     8 * 4,
                                     kvImageNoFlags);
    } else {
        NSLog(@"Unsupported rotation constant: %d.", rotation);
        free(destination);
        return NULL;
    }

    if (initError != kvImageNoError) {
        NSLog(@"Unable to initialize destination buffer.");
        free(destination);
        return NULL;
    }

    // 2. Apply the transform to `source` and write the result to `destination`.
    Pixel_8888 backColor = {0, 0, 0, 0};
    vImageRotate90_ARGB8888(source,
                            destination,
                            (uint8_t)rotation,
                            backColor,
                            kvImageNoFlags);

    return destination;
}
```

To learn more about rotation functions, see [Image rotation](./image-rotation.md).

### Rotate a vImage buffer by an arbitrary angle

The vImage library provides rotation functions that rotate an image by any angle around its center. The image below shows a buffer rotated 60° counterclockwise:

![A rotated photograph of some squashes.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3682702@2x.png)

The function below rotates a buffer by the specified angle and writes the result to the destination:

**Swift**:

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

**Objective-C**:

```objc
void rotateBuffer(const vImage_Buffer *source,
                  vImage_Buffer *destination,
                  double angleInDegrees,
                  const Pixel_8888 backgroundColor) {

    float radians = (float)(angleInDegrees * M_PI / 180.0);

    vImageRotate_ARGB8888(source,
                          destination,
                          NULL,
                          radians,
                          backgroundColor,
                          kvImageBackgroundColorFill);
}
```

### Scale a vImage buffer

The vImage library provides functions to scale the contents of an image buffer. The scaling can either be uniform, where the operation preserves the image’s aspect ratio, or nonuniform, where the operation stretches or condenses the image. The image below shows four scaled versions of the same photograph, with the second and third image scaled nonuniformly:

![Four variations of a scaled photograph of flowers.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3682710@2x.png)

The vImage scale functions accept source and destination buffers as parameters and rescale the source to fill the destination buffer. The function below wraps [`vImageScale_ARGB8888(_:_:_:_:)`](./vimagescale_argb8888%28_,_,_,_%29.md) to provide a simple interface to the scale operation:

**Swift**:

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

**Objective-C**:

```objc
void scaleBuffer(const vImage_Buffer *source, vImage_Buffer *destination) {

    vImageScale_ARGB8888(source,
                         destination,
                         NULL,
                         kvImageNoFlags);
}
```

To learn more about scaling functions, see [Image scaling](./image-scaling.md).

### Apply a simple affine transformation to a vImage buffer

Use an affine transformation to apply composite transformation, such as a scale and a translate.

A 3-by-3 matrix represents an affine transformation.

![A 3-by-3 matrix.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3682473@2x.png)

Because the third column is always `(0,0,1)`, the [`vImage_CGAffineTransform`](./vimage_cgaffinetransform.md) data structure contains values for only the first two columns.

To perform a scale transformation, set the *a* and *d* parameters of the matrix to the required scale.

![A 3-by-3 matrix for scaling.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3682474@2x.png)

To perform the translate transformation, set the *tx* and *ty* parameters of the matrix to the required offset.

![A 3 by 3 matrix for translation.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3682475@2x.png)

The `scaleAndCenterBuffer(source:destination:to:backgroundColor:)` function accepts a scale parameter and sets that parameter as the *a* and *d* parameters of the matrix.

**Swift**:

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

**Objective-C**:

```objc
void scaleAndCenterBuffer(const vImage_Buffer *source,
                          vImage_Buffer *destination,
                          double scale,
                          const Pixel_8888 backgroundColor) {

    // 1. Calculate the translate required to center the scaled buffer.
    double sourceCenterX = (double)source->width / 2.0;
    double sourceCenterY = (double)source->height / 2.0;

    double destinationCenterX = (double)destination->width / 2.0;
    double destinationCenterY = (double)destination->height / 2.0;

    double tx = destinationCenterX - sourceCenterX * scale;
    double ty = destinationCenterY - sourceCenterY * scale;

    // 2. Create the affine transformation that represents the scale-translate.
    vImage_CGAffineTransform vImageTransform = {
        .a  = scale, .b = 0,
        .c  = 0,     .d = scale,
        .tx = tx,    .ty = ty
    };

    // 3. Apply the transform to `source` and write the result to `destination`.
    vImageAffineWarpCG_ARGB8888(source,
                                destination,
                                NULL,
                                &vImageTransform,
                                backgroundColor,
                                kvImageBackgroundColorFill);
}
```

The image below shows the result of applying `scaleAndCenterBuffer(_:to:backgroundColor:)` with a scale of `0.25`:

![A photograph of flowers that is scaled down against a colored background.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3682477@2x.png)

To learn more about affine transformation functions, see [Applying affine transformations to images](./applying-affine-transformations-to-images.md).

### Apply a complex affine transformation to a vImage buffer

For complex transformations, [`CGAffineTransform`](../CoreFoundation/cgaffinetransform.md) allows you to concatenate a series of transformations. For example, to rotate and scale an image to fit within its unrotated bounding box, your code needs to translate, rotate, scale, and translate again.

The `rotateAndScaleBuffer(source:destination:byAngleInDegrees:backgroundColor:)` function uses [`CGAffineTransform`](../CoreFoundation/cgaffinetransform.md) to build the matrix required to rotate and scale an image to fit inside the bounding box of the destination buffer.

**Swift**:

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

**Objective-C**:

```objc
void rotateAndScaleBuffer(const vImage_Buffer *source,
                          vImage_Buffer *destination,
                          double angleInDegrees,
                          const Pixel_8888 backgroundColor) {

    // 1. Convert the specified angle in degrees to radians.
    CGFloat radians = (CGFloat)(angleInDegrees * M_PI / 180.0);

    // 2. Calculate the scale based on the bounding box of the rotated image.
    CGRect sourceRect = CGRectMake(0, 0, source->width, source->height);
    CGRect rotatedBoundingBox = CGRectApplyAffineTransform(
        sourceRect, CGAffineTransformMakeRotation(radians));
    CGFloat scaleX = (CGFloat)destination->width / rotatedBoundingBox.size.width;
    CGFloat scaleY = (CGFloat)destination->height / rotatedBoundingBox.size.height;
    CGFloat scale = scaleX < scaleY ? scaleX : scaleY;

    // 3. Create the composite affine transformation.
    CGAffineTransform cgTransform = CGAffineTransformIdentity;
    cgTransform = CGAffineTransformTranslate(cgTransform,
                                             (CGFloat)destination->width / 2,
                                             (CGFloat)destination->height / 2);
    cgTransform = CGAffineTransformRotate(cgTransform, radians);
    cgTransform = CGAffineTransformScale(cgTransform, scale, scale);
    cgTransform = CGAffineTransformTranslate(cgTransform,
                                             -(CGFloat)source->width / 2,
                                             -(CGFloat)source->height / 2);

    // 4. Convert the `CGAffineTransform` to a `vImage_CGAffineTransform`.
    vImage_CGAffineTransform vImageTransform = {
        .a  = (double)cgTransform.a,
        .b  = (double)cgTransform.b,
        .c  = (double)cgTransform.c,
        .d  = (double)cgTransform.d,
        .tx = (double)cgTransform.tx,
        .ty = (double)cgTransform.ty
    };

    // 5. Apply the transform to `source` and write the result to `destination`.
    vImageAffineWarpCG_ARGB8888(source,
                                destination,
                                NULL,
                                &vImageTransform,
                                backgroundColor,
                                kvImageBackgroundColorFill);
}
```

The image below shows the result of applying `rotateAndScaleBuffer(_:byAngleInDegrees:backgroundColor:)` with an angle of 30°:

![A rotated photograph of flowers that is scaled down to fit within its bounding box.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3682479@2x.png)

### Optimize performance with temporary buffers

The vImage rotate, scale, and affine transform functions use multiple-pass algorithms that save intermediate pixel values between passes. In some cases, the destination buffer may not be large enough to store that intermediate data, so the operation requires additional, temporary storage.

Pass `nil` to the function to have vImage create and manage this temporary storage for you. For example, the scale function below relies on the operation to manage the temporary buffer:

**Swift**:

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

**Objective-C**:

```objc
void scaleBuffer(const vImage_Buffer *source, vImage_Buffer *destination) {

    vImageScale_ARGB8888(source,
                         destination,
                         NULL,
                         kvImageNoFlags);
}
```

In cases where your code calls the function frequently (for example, when processing video), create and manage this temporary buffer yourself and reuse it across function calls. Reusing a buffer avoids vImage allocating the temporary storage with each call. Pass [`kvImageGetTempBufferSize`](./kvimagegettempbuffersize.md) to your geometry function to calculate the size, in bytes, of the temporary buffer, and use that value to allocate an [`UnsafeMutableRawPointer`](../Swift/unsafemutablerawpointer.md) structure.

The version of the `scaleBuffer()` function below shows an example of creating a temporary buffer:

**Swift**:

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

**Objective-C**:

```objc
void scaleBuffer(const vImage_Buffer *source, vImage_Buffer *destination) {

    vImage_Error bufferSize = vImageScale_ARGB8888(source,
                                                   destination,
                                                   NULL,
                                                   kvImageGetTempBufferSize);

    if (bufferSize < 0) {
        // Error calculating buffer size for scale operation.
        return;
    }

    // In a real app, you reuse this buffer across multiple calls of `vImageScale_ARGB8888`.
    void *temporaryBuffer = malloc((size_t)bufferSize);

    vImageScale_ARGB8888(source,
                         destination,
                         temporaryBuffer,
                         kvImageNoFlags);

    free(temporaryBuffer);
}
```

## See Also

### Image Processing Essentials
- [Converting bitmap data between Core Graphics images and vImage buffers](./converting-bitmap-data-between-core-graphics-images-and-vimage-buffers.md)
  Pass image data between Core Graphics and vImage to create and manipulate images.
- [Creating and Populating Buffers from Core Graphics Images](./creating-and-populating-buffers-from-core-graphics-images.md)
  Initialize vImage buffers from Core Graphics images.
- [Creating a Core Graphics Image from a vImage Buffer](./creating-a-core-graphics-image-from-a-vimage-buffer.md)
  Create displayable representations of vImage buffers.
- [Building a Basic Image-Processing Workflow](./building-a-basic-image-processing-workflow.md)
  Resize an image with vImage.
- [Compositing images with alpha blending](./compositing-images-with-alpha-blending.md)
  Combine two images by using alpha blending to create a single output.
- [Compositing images with vImage blend modes](./compositing-images-with-vimage-blend-modes.md)
  Combine two images by using blend modes to create a single output.
- [Applying vImage operations to regions of interest](./applying-vimage-operations-to-regions-of-interest.md)
  Limit the effect of vImage operations to rectangular regions of interest.
- [Optimizing image-processing performance](./optimizing-image-processing-performance.md)
  Improve your app’s performance by converting image buffer formats from interleaved to planar.
- [vImage](./vimage-library.md)
  Manipulate large images using the CPU’s vector processor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/applying-geometric-transforms-to-images)*
# vImageMatrixMultiply_Planar8(_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Multiplies each pixel in a set of 8-bit source image planes by a matrix to produce a set of 8-bit destination image planes.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 5.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageMatrixMultiply_Planar8(_ srcs: UnsafeMutablePointer<UnsafePointer<vImage_Buffer>?>, _ dests: UnsafeMutablePointer<UnsafePointer<vImage_Buffer>?>, _ src_planes: UInt32, _ dest_planes: UInt32, _ matrix: UnsafePointer<Int16>, _ divisor: Int32, _ pre_bias: UnsafePointer<Int16>!, _ post_bias: UnsafePointer<Int32>!, _ flags: vImage_Flags) -> vImage_Error
```

```c
vImage_Error vImageMatrixMultiply_Planar8(const vImage_Buffer * srcs[], const vImage_Buffer * dests[], uint32_t src_planes, uint32_t dest_planes, const int16_t matrix[], int32_t divisor, const int16_t *pre_bias, const int32_t *post_bias, vImage_Flags flags);
```

## Return Value

[`kvImageNoError`](./kvimagenoerror.md); otherwise, one of the error codes in [Data Types and Constants](./data-types-and-constants.md).

## Discussion

This function treats corresponding pixels in the source buffers as `m`-element vectors, and the corresponding pixels in the destination buffers as `n`-element vectors. Therefore, the multiplication requires an `m x n` matrix, that is, a matrix with `src_planes` rows and `dest_planes` columns.

The following code shows three source planes multiplied by a three-element column matrix to produce a single destination plane. The values in the matrix represent the Rec. 709 luminance coefficients that convert the color source pixels to a grayscale destination image. The three source planes represent the individual red, green, and blue channels of an image that contains a red pixel, a green pixel, and a blue pixel:

**Swift**:

```swift
let size = vImage.Size(width: 1, height: 3)

let red = vImage.PixelBuffer<vImage.Planar8>(
    pixelValues: [255, 0, 0],
    size: size)
let green = vImage.PixelBuffer<vImage.Planar8>(
    pixelValues: [0, 255, 0],
    size: size)
let blue = vImage.PixelBuffer<vImage.Planar8>(
    pixelValues: [0, 0, 255],
    size: size)

let destination = vImage.PixelBuffer<vImage.Planar8>(
    size: size)

let divisor: Int32 = 0x1000
let fDivisor = Float(divisor)

let redCoefficient: Float = 0.2126
let greenCoefficient: Float = 0.7152
let blueCoefficient: Float = 0.0722

let matrix = [
    Int16(redCoefficient * fDivisor),
    Int16(greenCoefficient * fDivisor),
    Int16(blueCoefficient * fDivisor)
]

red.withUnsafePointerToVImageBuffer { r in
    green.withUnsafePointerToVImageBuffer { g in
        blue.withUnsafePointerToVImageBuffer { b in
            destination.withUnsafePointerToVImageBuffer { dest in
                
                var srcs: [UnsafePointer<vImage_Buffer>?] = [ r, g, b ]
                var dests: [UnsafePointer<vImage_Buffer>?] = [ dest ]
                
                vImageMatrixMultiply_Planar8(
                    &srcs,
                    &dests,
                    3,
                    1,
                    matrix,
                    divisor,
                    nil,
                    nil,
                    vImage_Flags(kvImageNoFlags))
            }
        }
    }
}

// Prints "[0.21176, 0.71373, 0.070588]".
print(destination.array.map { Float($0) / 255 })
```

**Objective-C**:

```objc
uint8_t redData[3]   = {255, 0, 0};
uint8_t greenData[3] = {0, 255, 0};
uint8_t blueData[3]  = {0, 0, 255};
uint8_t dstData[3]   = {0, 0, 0};

vImage_Buffer redBuf   = { .data = redData,   .width = 1, .height = 3, .rowBytes = 1 };
vImage_Buffer greenBuf = { .data = greenData, .width = 1, .height = 3, .rowBytes = 1 };
vImage_Buffer blueBuf  = { .data = blueData,  .width = 1, .height = 3, .rowBytes = 1 };
vImage_Buffer destBuf  = { .data = dstData,   .width = 1, .height = 3, .rowBytes = 1 };

int32_t divisor = 0x1000;
float fDivisor = (float)divisor;
float redCoefficient   = 0.2126f;
float greenCoefficient = 0.7152f;
float blueCoefficient  = 0.0722f;

int16_t matrix[3] = {
    (int16_t)(redCoefficient   * fDivisor),
    (int16_t)(greenCoefficient * fDivisor),
    (int16_t)(blueCoefficient  * fDivisor)
};

const vImage_Buffer *srcs[3]  = { &redBuf, &greenBuf, &blueBuf };
const vImage_Buffer *dests[1] = { &destBuf };

vImageMatrixMultiply_Planar8(srcs, dests,
                             3, 1,
                             matrix, divisor,
                             NULL, NULL,
                             kvImageNoFlags);

// Prints "[0.21176, 0.71373, 0.070588]".
printf("[%f, %f, %f]\n",
      (float)dstData[0] / 255.0f,
      (float)dstData[1] / 255.0f,
      (float)dstData[2] / 255.0f);
```

On return, the destination buffer contains a grayscale representation of the red, green, and blue source buffers.

## Parameters

- `srcs`: A pointer to an array of vImage buffers. Each buffer represents a source plane.
- `dests`: A pointer to an array of vImage buffers. Each buffer represents a destination plane.
- `src_planes`: The number of source planes.
- `dest_planes`: The number of destination planes.
- `matrix`: An array of values that contains the `src_planes` rows multiplied by `dest_planes` columns 2D matrix elements.
- `divisor`: A value that the function divides the matrix multiplication result by after adding postbias.
- `pre_bias`: An array of bias values for each source plane. The function adds the corresponding bias value to each source value before the matrix multiplication step. Pass `nil` to specify zero prebias.
- `post_bias`: An array of bias values for each source plane. The function adds the corresponding bias value to each destination value after the matrix multiplication step. Pass `nil` to specify zero postbias.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass [`kvImageDoNotTile`](./kvimagedonottile.md); otherwise, pass [`kvImageNoFlags`](./kvimagenoflags.md).

## See Also

### Multiplying multiple-plane pixels by a matrix
- [Adjusting saturation and applying tone mapping](./adjusting-saturation-and-applying-tone-mapping.md)
  Convert an RGB image to discrete luminance and chrominance channels, and apply color and contrast treatments.
- [func vImageMatrixMultiply_Planar16S(UnsafeMutablePointer<UnsafePointer<vImage_Buffer>?>, UnsafeMutablePointer<UnsafePointer<vImage_Buffer>?>, UInt32, UInt32, UnsafePointer<Int16>, Int32, UnsafePointer<Int16>!, UnsafePointer<Int32>!, vImage_Flags) -> vImage_Error](./vimagematrixmultiply_planar16s%28_,_,_,_,_,_,_,_,_%29.md)
  Multiplies each pixel in a set of 16-bit source image planes by a matrix to produce a set of 8-bit destination image planes.
- [func vImageMatrixMultiply_PlanarF(UnsafeMutablePointer<UnsafePointer<vImage_Buffer>?>, UnsafeMutablePointer<UnsafePointer<vImage_Buffer>?>, UInt32, UInt32, UnsafePointer<Float>, UnsafePointer<Float>!, UnsafePointer<Float>!, vImage_Flags) -> vImage_Error](./vimagematrixmultiply_planarf%28_,_,_,_,_,_,_,_%29.md)
  Multiplies each pixel in a set of 32-bit source image planes by a matrix to produce a set of 32-bit destination image planes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagematrixmultiply_planar8(_:_:_:_:_:_:_:_:_:))*
# vImageMatrixMultiply_Planar16S(_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Multiplies each pixel in a set of 16-bit source image planes by a matrix to produce a set of 8-bit destination image planes.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 7.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageMatrixMultiply_Planar16S(_ srcs: UnsafeMutablePointer<UnsafePointer<vImage_Buffer>?>, _ dests: UnsafeMutablePointer<UnsafePointer<vImage_Buffer>?>, _ src_planes: UInt32, _ dest_planes: UInt32, _ matrix: UnsafePointer<Int16>, _ divisor: Int32, _ pre_bias: UnsafePointer<Int16>!, _ post_bias: UnsafePointer<Int32>!, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

This function treats corresponding pixels in the source buffers as `m`-element vectors, and the corresponding pixels in the destination buffers as `n`-element vectors. Therefore, the multiplication requires an `m x n` matrix, that is, a matrix with `src_planes` rows and `dest_planes` columns.

The following code shows three source planes multiplied by a three-element column matrix to produce a single destination plane. The values in the matrix represent the Rec. 709 luminance coefficients that convert the color source pixels to a grayscale destination image. The three source planes represent the individual red, green, and blue channels of an image that contains a red pixel, a green pixel, and a blue pixel.

```swift
var red = vImage_Buffer()
vImageBuffer_Init(&red, 1, 3, 16, 0)
red.data.assumingMemoryBound(to: Pixel_16S.self)[0] = Pixel_16S.max

var green = vImage_Buffer()
vImageBuffer_Init(&green, 1, 3, 16, 0)
green.data.assumingMemoryBound(to: Pixel_16S.self)[1] = Pixel_16S.max

var blue = vImage_Buffer()
vImageBuffer_Init(&blue, 1, 3, 16, 0)
blue.data.assumingMemoryBound(to: Pixel_16S.self)[2] = Pixel_16S.max

var destination = vImage_Buffer()
vImageBuffer_Init(&destination, 1, 3, 16, 0)

defer {
    red.free()
    green.free()
    blue.free()
    destination.free()
}

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

withUnsafePointer(to: red) { r in
    withUnsafePointer(to: green) { g in
        withUnsafePointer(to: blue) { b in
            withUnsafePointer(to: destination) { dest in
                
                var srcs: [UnsafePointer<vImage_Buffer>?] = [ r, g, b ]
                var dests: [UnsafePointer<vImage_Buffer>?] = [ dest ]
                
                vImageMatrixMultiply_Planar16S(
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

let result = UnsafeMutableBufferPointer(
    start: destination.data.assumingMemoryBound(to: Pixel_16S.self),
    count: 3)

// Prints "[0.21240883, 0.7150792, 0.07202368]".
print(Array(result).map { Float($0) / Float(Pixel_16S.max) })
```

On return, the destination buffer contains a grayscale representation of the red, green, and blue source buffers.

## Parameters

- `srcs`: A pointer to an array of vImage buffers. Each buffer represents a source plane.
- `dests`: A pointer to an array of vImage buffers. Each buffer represents a destination plane.
- `src_planes`: The number of source planes.
- `dest_planes`: The number of destination planes.
- `matrix`: An array of values that contains the   rows multiplied by   columns 2D matrix elements.
- `divisor`: A value that the function divides the matrix multiplication result by after adding postbias.
- `pre_bias`: An array of bias values for each source plane. The function adds the corresponding bias value to each source value before the matrix multiplication step. Pass   to specify zero prebias.
- `post_bias`: An array of bias values for each source plane. The function adds the corresponding bias value to each destination value after the matrix multiplication step. Pass   to specify zero postbias.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [Adjusting saturation and applying tone mapping](adjusting-saturation-and-applying-tone-mapping.md)
  Convert an RGB image to discrete luminance and chrominance channels, and apply color and contrast treatments.
- [func vImageMatrixMultiply_Planar8(UnsafeMutablePointer<UnsafePointer<vImage_Buffer>?>, UnsafeMutablePointer<UnsafePointer<vImage_Buffer>?>, UInt32, UInt32, UnsafePointer<Int16>, Int32, UnsafePointer<Int16>!, UnsafePointer<Int32>!, vImage_Flags) -> vImage_Error](vimagematrixmultiply_planar8(_:_:_:_:_:_:_:_:_:).md)
  Multiplies each pixel in a set of 8-bit source image planes by a matrix to produce a set of 8-bit destination image planes.
- [func vImageMatrixMultiply_PlanarF(UnsafeMutablePointer<UnsafePointer<vImage_Buffer>?>, UnsafeMutablePointer<UnsafePointer<vImage_Buffer>?>, UInt32, UInt32, UnsafePointer<Float>, UnsafePointer<Float>!, UnsafePointer<Float>!, vImage_Flags) -> vImage_Error](vimagematrixmultiply_planarf(_:_:_:_:_:_:_:_:).md)
  Multiplies each pixel in a set of 32-bit source image planes by a matrix to produce a set of 32-bit destination image planes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagematrixmultiply_planar16s(_:_:_:_:_:_:_:_:_:))*
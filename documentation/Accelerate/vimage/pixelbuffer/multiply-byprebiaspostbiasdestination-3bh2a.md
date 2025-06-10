# multiply(by:preBias:postBias:destination:)

**Framework**: Accelerate  
**Kind**: method

Multiplies each pixel in a 32-bit planar pixel buffer by the specified factor.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
func multiply(by factor: Float, preBias: Float, postBias: Float, destination: vImage.PixelBuffer<vImage.PlanarF>)
```

#### Discussion

This function applies the following operation to each pixel:

```swift
destination = ((source + preBias) * factor) + postBias
```

For example, the following code multiplies each pixel value in a 32-bit planar buffer by `2`:

```swift
   let buffer = vImage.PixelBuffer<vImage.PlanarF>(
       pixelValues: [0.1, 0.2, 0.3, 0.4, 0.5],
       size: vImage.Size(width: 5,
                         height: 1))

   buffer.multiply(by: 2,
                   preBias: 0, postBias: 0,
                   destination: buffer)

   // Prints "[0.2, 0.4, 0.6, 0.8, 1.0]"
   print(buffer.array)
```

## Parameters

- `factor`: The multiplication factor.
- `preBias`: A value that the function adds to the source before multiplication.
- `postBias`: A value that the function adds to the result after multiplication.
- `destination`: The destination pixel buffer.

## See Also

- [func multiply(by: Int, divisor: Int, preBias: Int, postBias: Int, destination: vImage.PixelBuffer<vImage.Planar8>)](vimage/pixelbuffer/multiply(by:divisor:prebias:postbias:destination:)-7jo6v.md)
  Multiplies each pixel in an 8-bit planar pixel buffer by the specified factor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/multiply(by:prebias:postbias:destination:)-3bh2a)*
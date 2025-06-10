# clip(to:destination:)

**Framework**: Accelerate  
**Kind**: method

Clips the values of a 32-bit pixel buffer to the specified bounds.

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
func clip(to bounds: ClosedRange<Float>, destination: vImage.PixelBuffer<Format>)
```

#### Discussion

Use this function to set all pixel values outside of the clipping range to the lower and upper bounds. For example, the following code clips pixel values to the range `0.25 ... 0.75`.

The function clips the source values `0.0` and `0.2` to `0.25`, and the source values `0.8` and `1.0` to `0.75`.

```swift
let buffer = vImage.PixelBuffer<vImage.PlanarF>(
    pixelValues: [0.0, 0.2, 0.4, 0.6, 0.8, 1.0],
    size: vImage.Size(width: 6,
                      height: 1))

buffer.clip(to: 0.25 ... 0.75,
            destination: buffer)

// Prints "[0.25, 0.25, 0.4, 0.6, 0.75, 0.75]".
print(buffer.array)
```

## Parameters

- `bounds`: The clipping range.
- `destination`: The destination pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/clip(to:destination:))*
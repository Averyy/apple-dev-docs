# colorThreshold(_:destination:)

**Framework**: Accelerate  
**Kind**: method

Creates a binary image from a 32-bit pixel buffer.

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
func colorThreshold(_ threshold: Float, destination: vImage.PixelBuffer<Format>)
```

## Mentions

- [Applying flood fills to an image](applying-flood-fills-to-an-image.md)

#### Discussion

This function generates an image with source values that are less than `threshold` set to `0`, and source values that are greater than `threshold` set to `1`.

Use this function to binarize an image. For example, the following code applies a threshold of `0.5` to a pixel buffer. The source values `0.0`, `0.2`, and `0.4` are less than the threshold and the function returns `0.0` for the first three elements. The source values `0.6`, `0.8`, and `1.0` are greater than the threshold and the function returns `1.0` for the last three elements.

```swift
let buffer = vImage.PixelBuffer<vImage.PlanarF>(
    pixelValues: [0.0, 0.2, 0.4, 0.6, 0.8, 1.0],
    size: vImage.Size(width: 6,
                      height: 1))

buffer.colorThreshold(0.5,
                      destination: buffer)

// Prints "[0.0, 0.0, 0.0, 1.0, 1.0, 1.0]".
print(buffer.array)
```

## Parameters

- `threshold`: The threshold value.
- `destination`: The destination pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/colorthreshold(_:destination:))*
# applyMorphology(operation:destination:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Applies a morphology operation to the buffer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
func applyMorphology(operation: vImage.MorphologyOperation<Format.ComponentType>, destination: vImage.PixelBuffer<Format>)
```

Available when `Format` conforms to `MultiplePlanePixelFormat`, `Format.ComponentType` is `UInt8`, and `Format.PlanarPixelFormat.ComponentType` is `UInt8`.

## Discussion

> **Precondition**: Source and destination buffer must be the same size.

> **Precondition**: The kernel size width and height must be positive, odd integers in the range

> **Precondition**: `dilate` and `erode` user defined kernels must contain `width * height` elements.

> **Precondition**: Source and destination buffers must point to different underlying memory.

## Parameters

- `operation`: The operation that the function applies.
- `destination`: The destination pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/applymorphology(operation:destination:)-5al25)*
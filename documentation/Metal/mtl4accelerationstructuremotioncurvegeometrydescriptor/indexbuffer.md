# indexBuffer

**Framework**: Metal  
**Kind**: property

Assigns an optional index buffer containing references to control points in the control point buffers.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var indexBuffer: MTL4BufferRange { get set }
```

#### Discussion

All keyframes share the same index buffer, with each index representing the first control point of a curve segment.

You are responsible for ensuring the buffer address of the range is not zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4accelerationstructuremotioncurvegeometrydescriptor/indexbuffer)*
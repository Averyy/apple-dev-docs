# boundingBoxStride

**Framework**: Metal  
**Kind**: property

Assigns the stride, in bytes, between bounding boxes in the bounding box buffer `boundingBoxBuffer` references.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var boundingBoxStride: Int { get set }
```

#### Discussion

You are responsible for ensuring this stride is at least 24 bytes and a multiple of 4 bytes.

This property defaults to `24` bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4accelerationstructureboundingboxgeometrydescriptor/boundingboxstride)*
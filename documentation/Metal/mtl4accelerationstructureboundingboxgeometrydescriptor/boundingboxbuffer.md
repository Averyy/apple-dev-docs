# boundingBoxBuffer

**Framework**: Metal  
**Kind**: property

References a buffer containing bounding box data in `MTLAxisAlignedBoundingBoxes` format.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var boundingBoxBuffer: MTL4BufferRange { get set }
```

#### Discussion

You are responsible for ensuring the buffer address of the range is not zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4accelerationstructureboundingboxgeometrydescriptor/boundingboxbuffer)*
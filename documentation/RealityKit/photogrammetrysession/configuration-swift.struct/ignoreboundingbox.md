# ignoreBoundingBox

**Framework**: RealityKit  
**Kind**: property

Ignores any bounding box information embedded in the input images and instead returns all possible geometry that can be automatically estimated using the image set.  The resulting mesh will likely need post-processing. Note: to recover the entire scene geometry as well as ignore the box, `isObjectMaskingEnabled` should also be set to false.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
var ignoreBoundingBox: Bool
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/configuration-swift.struct/ignoreboundingbox)*
# ImmersiveImageMask

**Framework**: Immersive Media Support  
**Kind**: class

An object that holds all the information needed to load immersive media masks from image data or from a file.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final class ImmersiveImageMask
```

#### Overview

An image file containing the alpha values is used to generate the image mask.

## Topics

### Initializers
- [init(name: String, maskData: Data?)](immersiveimagemask/init(name:maskdata:).md)
- [init(name: String, maskURL: URL)](immersiveimagemask/init(name:maskurl:).md)
### Instance Properties
- [let maskData: Data?](immersiveimagemask/maskdata.md)
- [let name: String](immersiveimagemask/name.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersiveimagemask)*
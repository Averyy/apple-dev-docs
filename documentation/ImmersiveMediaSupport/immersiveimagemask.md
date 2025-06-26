# ImmersiveImageMask

**Framework**: Immersive Media Support  
**Kind**: class

Immersive media image masks are generated using an image file containing the alpha values for the mask.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
final class ImmersiveImageMask
```

## Topics

### Initializers
- [init(from: any Decoder) throws](immersiveimagemask/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [init(name: String, maskData: Data?)](immersiveimagemask/init(name:maskdata:).md)
- [init(name: String, maskURL: URL)](immersiveimagemask/init(name:maskurl:).md)
### Instance Properties
- [let maskData: Data?](immersiveimagemask/maskdata.md)
- [let name: String](immersiveimagemask/name.md)
### Instance Methods
- [func encode(to: any Encoder) throws](immersiveimagemask/encode(to:).md)
  Encodes this value into the given encoder.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersiveimagemask)*
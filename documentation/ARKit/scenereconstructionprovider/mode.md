# SceneReconstructionProvider.Mode

**Framework**: ARKit  
**Kind**: enum  
**Role**: Enumeration

The additional kinds of information you can request about a person’s surroundings.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
enum Mode
```

## Topics

### Scene reconstruction modes
- [SceneReconstructionProvider.Mode.classification](./mode/classification.md)
  The reconstruction mode that classifies each face of a mesh anchor.
### Instance Properties
- [var description: String](./mode/description.md)
  A textual representation of SceneReconstructionProvider.Mode

## Relationships

### Conforms To
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a scene reconstruction provider
- [init(modes: [SceneReconstructionProvider.Mode])](./init%28modes%29.md)
  Creates a provider that reconstructs a person’s surroundings.
- [let modes: [SceneReconstructionProvider.Mode]](./modes.md)
  The modes of scene reconstruction a provider supplies.
- [static var isSupported: Bool](./issupported.md)
  A Boolean value that indicates whether the current runtime environment supports scene reconstruction providers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/scenereconstructionprovider/mode)*
# SceneReconstructionProvider.Mode

**Framework**: ARKit  
**Kind**: enum

The additional kinds of information you can request about a person’s surroundings.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
enum Mode
```

## Topics

### Scene reconstruction modes
- [SceneReconstructionProvider.Mode.classification](scenereconstructionprovider/mode/classification.md)
  The reconstruction mode that classifies each face of a mesh anchor.
### Instance Properties
- [var description: String](scenereconstructionprovider/mode/description.md)
  A textual representation of SceneReconstructionProvider.Mode

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(modes: [SceneReconstructionProvider.Mode])](scenereconstructionprovider/init(modes:).md)
  Creates a provider that reconstructs a person’s surroundings.
- [let modes: [SceneReconstructionProvider.Mode]](scenereconstructionprovider/modes.md)
  The modes of scene reconstruction a provider supplies.
- [static var isSupported: Bool](scenereconstructionprovider/issupported.md)
  A Boolean value that indicates whether the current runtime environment supports scene reconstruction providers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/scenereconstructionprovider/mode)*
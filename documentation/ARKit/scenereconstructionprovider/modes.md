# modes

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The modes of scene reconstruction a provider supplies.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
final let modes: [SceneReconstructionProvider.Mode]
```

## See Also

### Creating a scene reconstruction provider
- [init(modes: [SceneReconstructionProvider.Mode])](./init%28modes%29.md)
  Creates a provider that reconstructs a person’s surroundings.
- [SceneReconstructionProvider.Mode](./mode.md)
  The additional kinds of information you can request about a person’s surroundings.
- [static var isSupported: Bool](./issupported.md)
  A Boolean value that indicates whether the current runtime environment supports scene reconstruction providers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/scenereconstructionprovider/modes)*
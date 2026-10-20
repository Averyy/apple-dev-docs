# init(modes:)

**Framework**: ARKit  
**Kind**: init  
**Role**: Initializer

Creates a provider that reconstructs a person’s surroundings.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
init(modes: [SceneReconstructionProvider.Mode] = [])
```

#### Discussion

You can pass additional modes, such as [`SceneReconstructionProvider.Mode.classification`](./mode/classification.md), if you need more than the default mesh data.

## Parameters

- `modes`: The modes of scene reconstruction your app requires.

## See Also

### Creating a scene reconstruction provider
- [let modes: [SceneReconstructionProvider.Mode]](./modes.md)
  The modes of scene reconstruction a provider supplies.
- [SceneReconstructionProvider.Mode](./mode.md)
  The additional kinds of information you can request about a person’s surroundings.
- [static var isSupported: Bool](./issupported.md)
  A Boolean value that indicates whether the current runtime environment supports scene reconstruction providers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/scenereconstructionprovider/init(modes:))*
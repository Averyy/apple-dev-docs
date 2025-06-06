# registerSoundEventAsset(rootNode:identifier:)

**Framework**: PHASE  
**Kind**: method

Registers the root node of the sound event asset.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func registerSoundEventAsset(rootNode: PHASESoundEventNodeDefinition, identifier: String?) throws -> PHASESoundEventNodeAsset
```

#### Return Value

A sound event node asset.

## Parameters

- `rootNode`: The root node of the sound event asset to register.
- `identifier`: The identifier to assign to this parameter. Assigning   generates an automatic identifier.

## See Also

- [func asset(forIdentifier: String) -> PHASEAsset?](phaseassetregistry/asset(foridentifier:).md)
  Provides the asset named with the designated identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseassetregistry/registersoundeventasset(rootnode:identifier:))*
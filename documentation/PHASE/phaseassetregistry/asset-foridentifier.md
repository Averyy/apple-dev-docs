# asset(forIdentifier:)

**Framework**: PHASE  
**Kind**: method

Provides the asset named with the designated identifier.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func asset(forIdentifier identifier: String) -> PHASEAsset?
```

#### Return Value

A framework asset by the destignated name, if the app registers the asset prior. Otherwise, returns `nil`.

## Parameters

- `identifier`: The unique name of the asset.

## See Also

- [func registerSoundEventAsset(rootNode: PHASESoundEventNodeDefinition, identifier: String?) throws -> PHASESoundEventNodeAsset](phaseassetregistry/registersoundeventasset(rootnode:identifier:).md)
  Registers the root node of the sound event asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseassetregistry/asset(foridentifier:))*
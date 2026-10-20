# asset(forIdentifier:)

**Framework**: PHASE  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (PHASEAsset *) assetForIdentifier:(NSString *) identifier;
```

#### Return Value

A framework asset by the destignated name, if the app registers the asset prior. Otherwise, returns `nil`.

## Parameters

- `identifier`: The unique name of the asset.

## See Also

### Registering Sound Event Assets
- [func registerSoundEventAsset(rootNode: PHASESoundEventNodeDefinition, identifier: String?) throws -> PHASESoundEventNodeAsset](./registersoundeventasset%28rootnode,identifier%29.md)
  Registers the root node of the sound event asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseassetregistry/asset(foridentifier:))*
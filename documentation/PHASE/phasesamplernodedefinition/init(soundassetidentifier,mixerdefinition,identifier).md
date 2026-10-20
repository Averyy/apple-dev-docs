# init(soundAssetIdentifier:mixerDefinition:identifier:)

**Framework**: PHASE  
**Kind**: init  
**Role**: Initializer

Creates a named sampler node with the given sound asset and mixer.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(soundAssetIdentifier: String, mixerDefinition: PHASEMixerDefinition, identifier: String)
```

```objc
- (instancetype) initWithSoundAssetIdentifier:(NSString *) soundAssetIdentifier mixerDefinition:(PHASEMixerDefinition *) mixerDefinition identifier:(NSString *) identifier;
```

## Parameters

- `soundAssetIdentifier`: A name that refers to the audio data that the node plays. See [`assetIdentifier`](./assetidentifier.md).
- `mixerDefinition`: An object that combines audio layers.
- `identifier`: A unique name for the sample node.

## See Also

### Creating a Sampler Node
- [init(soundAssetIdentifier: String, mixerDefinition: PHASEMixerDefinition)](./init%28soundassetidentifier,mixerdefinition%29.md)
  Creates a sampler node with the given sound asset and mixer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesamplernodedefinition/init(soundassetidentifier:mixerdefinition:identifier:))*
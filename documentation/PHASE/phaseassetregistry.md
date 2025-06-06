# PHASEAssetRegistry

**Framework**: PHASE  
**Kind**: class

A central repository of audio assets.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASEAssetRegistry
```

#### Overview

This class manages audio by registering two types of assets throughout the app’s life cycle:

When you’re done with a sound asset, call [`unregisterAsset(identifier:completion:)`](phaseassetregistry/unregisterasset(identifier:completion:).md) to free up its system resources.

## Topics

### Registering Sound Assets
- [func registerSoundAsset(url: URL, identifier: String?, assetType: PHASEAsset.AssetType, channelLayout: AVAudioChannelLayout?, normalizationMode: PHASENormalizationMode) throws -> PHASESoundAsset](phaseassetregistry/registersoundasset(url:identifier:assettype:channellayout:normalizationmode:).md)
  Loads a sound asset from the argument URL and adds it to the engine’s list of registered assets.
- [func registerSoundAsset(data: Data, identifier: String?, format: AVAudioFormat, normalizationMode: PHASENormalizationMode) throws -> PHASESoundAsset](phaseassetregistry/registersoundasset(data:identifier:format:normalizationmode:).md)
  Loads a sound asset from memory and adds it to the engine’s list of registered assets.
- [func unregisterAsset(identifier: String, completion: ((Bool) -> Void)?)](phaseassetregistry/unregisterasset(identifier:completion:).md)
  Deallocates system memory for a given asset and removes it from the engine’s list of registered assets.
### Registering Sound Event Assets
- [func registerSoundEventAsset(rootNode: PHASESoundEventNodeDefinition, identifier: String?) throws -> PHASESoundEventNodeAsset](phaseassetregistry/registersoundeventasset(rootnode:identifier:).md)
  Registers the root node of the sound event asset.
- [func asset(forIdentifier: String) -> PHASEAsset?](phaseassetregistry/asset(foridentifier:).md)
  Provides the asset named with the designated identifier.
### Registering Global Metaparameters
- [func registerGlobalMetaParameter(metaParameterDefinition: PHASEMetaParameterDefinition) throws -> PHASEGlobalMetaParameterAsset](phaseassetregistry/registerglobalmetaparameter(metaparameterdefinition:).md)
  Registers a global metaparameter with the asset registry.
- [var globalMetaParameters: [String : PHASEMetaParameter]](phaseassetregistry/globalmetaparameters.md)
  A dictionary of metaparameters that all sound event assets share.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PHASEEngine](phaseengine.md)
  An object that manages audio assets, controls playback, and configures environmental effects.
- [PHASEEngine.UpdateMode](phaseengine/updatemode.md)
  Modes that determine when the framework consumes API calls and updates internal state.
- [enum PHASENormalizationMode](phasenormalizationmode.md)
  Options that determine whether the framework adjusts a sound asset’s loudness for the user’s output device.
- [enum PHASESpatializationMode](phasespatializationmode.md)
  The manner in which PHASE outputs spatial audio.
- [enum PHASEReverbPreset](phasereverbpreset.md)
  The manner in which PHASE diffuses resonating sound.
- [class PHASEMedium](phasemedium.md)
  A property or quality of the environment that affects how sound travels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseassetregistry)*
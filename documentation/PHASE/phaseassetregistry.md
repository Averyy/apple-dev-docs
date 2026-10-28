# PHASEAssetRegistry

**Framework**: PHASE  
**Kind**: class  
**Role**: Class

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

```objc
@interface PHASEAssetRegistry : NSObject
```

## Overview

This class manages audio by registering two types of assets throughout the app’s life cycle:

- **[`PHASESoundAsset`](./phasesoundasset.md)**: A sound asset identifies the particular audio data that your app intends to play.
- **[`PHASESoundEventNodeAsset`](./phasesoundeventnodeasset.md)**: A sound event asset provides audio with an avenue to the output device, and either represents a single sound or a dynamic set of sounds that play individually, depending on the app’s state.

When you’re done with a sound asset, call [`unregisterAsset(identifier:completion:)`](./phaseassetregistry/unregisterasset%28identifier,completion%29.md) to free up its system resources.

## Topics

### Registering Sound Assets
- [func registerSoundAsset(url: URL, identifier: String?, assetType: PHASEAsset.AssetType, channelLayout: AVAudioChannelLayout?, normalizationMode: PHASENormalizationMode) throws -> PHASESoundAsset](./phaseassetregistry/registersoundasset%28url,identifier,assettype,channellayout,normalizationmode%29.md)
  Loads a sound asset from the argument URL and adds it to the engine’s list of registered assets.
- [func registerSoundAsset(data: Data, identifier: String?, format: AVAudioFormat, normalizationMode: PHASENormalizationMode) throws -> PHASESoundAsset](./phaseassetregistry/registersoundasset%28data,identifier,format,normalizationmode%29.md)
  Loads a sound asset from memory and adds it to the engine’s list of registered assets.
- [func unregisterAsset(identifier: String, completion: ((Bool) -> Void)?)](./phaseassetregistry/unregisterasset%28identifier,completion%29.md)
  Deallocates system memory for a given asset and removes it from the engine’s list of registered assets.
### Registering Sound Event Assets
- [func registerSoundEventAsset(rootNode: PHASESoundEventNodeDefinition, identifier: String?) throws -> PHASESoundEventNodeAsset](./phaseassetregistry/registersoundeventasset%28rootnode,identifier%29.md)
  Registers the root node of the sound event asset.
- [func asset(forIdentifier: String) -> PHASEAsset?](./phaseassetregistry/asset%28foridentifier%29.md)
  Provides the asset named with the designated identifier.
### Registering Global Metaparameters
- [func registerGlobalMetaParameter(metaParameterDefinition: PHASEMetaParameterDefinition) throws -> PHASEGlobalMetaParameterAsset](./phaseassetregistry/registerglobalmetaparameter%28metaparameterdefinition%29.md)
  Registers a global metaparameter with the asset registry.
- [var globalMetaParameters: [String : PHASEMetaParameter]](./phaseassetregistry/globalmetaparameters.md)
  A dictionary of metaparameters that all sound event assets share.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Setup
- [class PHASEEngine](./phaseengine.md)
  An object that manages audio assets, controls playback, and configures environmental effects.
- [PHASEEngine.UpdateMode](./phaseengine/updatemode.md)
  Modes that determine when the framework consumes API calls and updates internal state.
- [PHASEEngine.RenderingMode](./phaseengine/renderingmode.md)
  Modes that determine whether the system renders audio in process or out of process.
- [enum PHASENormalizationMode](./phasenormalizationmode.md)
  Options that determine whether the framework adjusts a sound asset’s loudness for the user’s output device.
- [enum PHASESpatializationMode](./phasespatializationmode.md)
  The manner in which PHASE outputs spatial audio.
- [enum PHASEReverbPreset](./phasereverbpreset.md)
  The manner in which PHASE diffuses resonating sound.
- [class PHASEMedium](./phasemedium.md)
  A property or quality of the environment that affects how sound travels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseassetregistry)*
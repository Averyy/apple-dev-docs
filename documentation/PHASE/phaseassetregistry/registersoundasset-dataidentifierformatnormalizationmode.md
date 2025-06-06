# registerSoundAsset(data:identifier:format:normalizationMode:)

**Framework**: PHASE  
**Kind**: method

Loads a sound asset from memory and adds it to the engine’s list of registered assets.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func registerSoundAsset(data: Data, identifier: String?, format: AVAudioFormat, normalizationMode: PHASENormalizationMode) throws -> PHASESoundAsset
```

#### Return Value

A sound asset object. If an error occurs, the function returns `nil`.

## Parameters

- `data`: A buffer containing the audio data to register. Audio data needs to be single-channel interleaved PCM, or per-channel de-interleaved PCM with buffers organized back to back.
- `identifier`: A unique name for the sound asset. If you provide  , the framework determines and sets value for the asset’s identifier.
- `format`: And object that describes the audio data layout.
- `normalizationMode`: An option to calibrate the sound asset for the user’s output device.

## See Also

- [func registerSoundAsset(url: URL, identifier: String?, assetType: PHASEAsset.AssetType, channelLayout: AVAudioChannelLayout?, normalizationMode: PHASENormalizationMode) throws -> PHASESoundAsset](phaseassetregistry/registersoundasset(url:identifier:assettype:channellayout:normalizationmode:).md)
  Loads a sound asset from the argument URL and adds it to the engine’s list of registered assets.
- [func unregisterAsset(identifier: String, completion: ((Bool) -> Void)?)](phaseassetregistry/unregisterasset(identifier:completion:).md)
  Deallocates system memory for a given asset and removes it from the engine’s list of registered assets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseassetregistry/registersoundasset(data:identifier:format:normalizationmode:))*
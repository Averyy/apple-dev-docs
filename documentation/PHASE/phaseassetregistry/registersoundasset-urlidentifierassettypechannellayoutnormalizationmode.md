# registerSoundAsset(url:identifier:assetType:channelLayout:normalizationMode:)

**Framework**: PHASE  
**Kind**: method

Loads a sound asset from the argument URL and adds it to the engine’s list of registered assets.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func registerSoundAsset(url: URL, identifier: String?, assetType: PHASEAsset.AssetType, channelLayout: AVAudioChannelLayout?, normalizationMode: PHASENormalizationMode) throws -> PHASESoundAsset
```

#### Return Value

A sound asset object. If an error occurs, the function returns `nil`.

#### Discussion

To expedite audio loading, run this function for multiple assets on multiple threads. This function runs synchronously. As a thread-safe function, you can run it off the main thread.

## Parameters

- `url`: A URL to an audio file on disk. This function doesn’t support network URLs.
- `identifier`: A unique name for the sound asset. If you provide  , the framework determines and sets value for the asset’s identifier.
- `assetType`: The asset’s type.
- `channelLayout`: If the asset is stereo or mono, you can pass   because the framework generates the channel layout for you in that case.
- `normalizationMode`: An option to calibrate the sound asset for the user’s output device.

## See Also

- [func registerSoundAsset(data: Data, identifier: String?, format: AVAudioFormat, normalizationMode: PHASENormalizationMode) throws -> PHASESoundAsset](phaseassetregistry/registersoundasset(data:identifier:format:normalizationmode:).md)
  Loads a sound asset from memory and adds it to the engine’s list of registered assets.
- [func unregisterAsset(identifier: String, completion: ((Bool) -> Void)?)](phaseassetregistry/unregisterasset(identifier:completion:).md)
  Deallocates system memory for a given asset and removes it from the engine’s list of registered assets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseassetregistry/registersoundasset(url:identifier:assettype:channellayout:normalizationmode:))*
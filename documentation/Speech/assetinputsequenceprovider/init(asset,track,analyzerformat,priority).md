# init(asset:track:analyzerFormat:priority:)

**Framework**: Speech  
**Kind**: init  
**Role**: Initializer

Creates an input sequence provider.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
init(asset: AVAsset, track: AVAssetTrack, analyzerFormat: AVAudioFormat, priority: TaskPriority? = nil)
```

## Parameters

- `asset`: The asset to read from.
- `track`: The track to read audio samples from.
- `analyzerFormat`: The audio format to convert the audio samples to. The audio format should be one supported by the speech analyzer’s modules.
- `priority`: The desired priority of the asset-reading task.

## See Also

### Creating a provider
- [static func provider(from: AVAsset, compatibleWith: [any SpeechModule], priority: TaskPriority?) async throws -> AssetInputSequenceProvider](./provider%28from,compatiblewith,priority%29.md)
  Returns an input sequence provider that reads from the first track of an asset or file.
- [static func provider(from: AVAsset, track: AVAssetTrack, compatibleWith: [any SpeechModule], priority: TaskPriority?) async throws -> AssetInputSequenceProvider](./provider%28from,track,compatiblewith,priority%29.md)
  Returns an input sequence provider that reads from a track of an asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/assetinputsequenceprovider/init(asset:track:analyzerformat:priority:))*
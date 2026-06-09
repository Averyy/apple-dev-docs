# init(asset:track:analyzerFormat:priority:)

**Framework**: Speech  
**Kind**: init

Creates an input sequence provider.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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

- [static func provider(from: AVAsset, compatibleWith: [any SpeechModule], priority: TaskPriority?) async throws -> AssetInputSequenceProvider](assetinputsequenceprovider/provider(from:compatiblewith:priority:).md)
  Returns an input sequence provider that reads from the first track of an asset or file.
- [static func provider(from: AVAsset, track: AVAssetTrack, compatibleWith: [any SpeechModule], priority: TaskPriority?) async throws -> AssetInputSequenceProvider](assetinputsequenceprovider/provider(from:track:compatiblewith:priority:).md)
  Returns an input sequence provider that reads from a track of an asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/assetinputsequenceprovider/init(asset:track:analyzerformat:priority:))*
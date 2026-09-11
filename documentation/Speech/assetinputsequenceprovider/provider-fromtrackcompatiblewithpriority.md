# provider(from:track:compatibleWith:priority:)

**Framework**: Speech  
**Kind**: method

Returns an input sequence provider that reads from a track of an asset.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static func provider(from asset: AVAsset, track: AVAssetTrack, compatibleWith modules: [any SpeechModule], priority: TaskPriority? = nil) async throws -> AssetInputSequenceProvider
```

#### Return Value

An instance of this class.

## Parameters

- `asset`: The asset to read from.
- `track`: The track to read from.
- `modules`: The speech modules that will analyze the audio.
- `priority`: The desired priority of the asset-reading task.

## See Also

- [static func provider(from: AVAsset, compatibleWith: [any SpeechModule], priority: TaskPriority?) async throws -> AssetInputSequenceProvider](assetinputsequenceprovider/provider(from:compatiblewith:priority:).md)
  Returns an input sequence provider that reads from the first track of an asset or file.
- [init(asset: AVAsset, track: AVAssetTrack, analyzerFormat: AVAudioFormat, priority: TaskPriority?)](assetinputsequenceprovider/init(asset:track:analyzerformat:priority:).md)
  Creates an input sequence provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/assetinputsequenceprovider/provider(from:track:compatiblewith:priority:))*
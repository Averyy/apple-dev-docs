# provider(from:compatibleWith:priority:)

**Framework**: Speech  
**Kind**: method

Returns an input sequence provider that reads from the first track of an asset or file.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func provider(from asset: AVAsset, compatibleWith modules: [any SpeechModule], priority: TaskPriority? = nil) async throws -> AssetInputSequenceProvider
```

#### Return Value

An instance of this class.

## Parameters

- `asset`: The asset to read from.
- `modules`: The speech modules that will analyze the audio.
- `priority`: The desired priority of the asset-reading task.

## See Also

- [static func provider(from: AVAsset, track: AVAssetTrack, compatibleWith: [any SpeechModule], priority: TaskPriority?) async throws -> AssetInputSequenceProvider](assetinputsequenceprovider/provider(from:track:compatiblewith:priority:).md)
  Returns an input sequence provider that reads from a track of an asset.
- [init(asset: AVAsset, track: AVAssetTrack, analyzerFormat: AVAudioFormat, priority: TaskPriority?)](assetinputsequenceprovider/init(asset:track:analyzerformat:priority:).md)
  Creates an input sequence provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/assetinputsequenceprovider/provider(from:compatiblewith:priority:))*
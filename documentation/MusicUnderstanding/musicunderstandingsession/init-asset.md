# init(asset:)

**Framework**: MusicUnderstanding  
**Kind**: init

Creates a music understanding session from an audio asset.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
convenience init(asset: any AVAsset & Sendable) async throws
```

#### Discussion

Use this initializer when your audio source is an `AVAsset` rather than a streaming sequence of audio buffers.

> **Note**:  If the asset is unreadable, does not contain valid audio tracks, or cannot be processed for analysis.

> **Note**:  This initializer doesn’t support HTTP livestreams (HLS). The asset must represent locally available media or a complete file.

## Parameters

- `asset`: An `AVAsset` containing an audio track.

## See Also

- [convenience init<Provider>(audioProvider: Provider)](musicunderstandingsession/init(audioprovider:).md)
  Creates a music understanding session that accepts streaming audio buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musicunderstanding/musicunderstandingsession/init(asset:))*
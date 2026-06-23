# init(audioProvider:)

**Framework**: Music Understanding  
**Kind**: init

Creates a music understanding session that accepts streaming audio buffers.

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
convenience init<Provider>(audioProvider: Provider) where Provider : AsyncSequence, Provider.Element == AVReadOnlyAudioPCMBuffer, Provider.Failure == Never
```

## Parameters

- `audioProvider`: A non-throwing async sequence of audio buffers. The sequence must have `Failure == Never`, meaning callers are responsible for handling any errors in their audio pipeline before passing buffers to the session.

## See Also

- [convenience init(asset: any AVAsset & Sendable) async throws](musicunderstandingsession/init(asset:).md)
  Creates a music understanding session from an audio asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musicunderstanding/musicunderstandingsession/init(audioprovider:))*
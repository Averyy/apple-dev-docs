# init(layoutTag:)

**Framework**: AVFAudio  
**Kind**: init

Creates an audio channel layout object from a layout tag.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init?(layoutTag: AudioChannelLayoutTag)
```

#### Return Value

A new `AVAudioChannelLayout` object, or `nil` if `layoutTag` is [`kAudioChannelLayoutTag_UseChannelDescriptions`](https://developer.apple.com/documentation/CoreAudioTypes/kAudioChannelLayoutTag_UseChannelDescriptions) or [`kAudioChannelLayoutTag_UseChannelBitmap`](https://developer.apple.com/documentation/CoreAudioTypes/kAudioChannelLayoutTag_UseChannelBitmap).

## Parameters

- `layoutTag`: The audio channel layout tag.

## See Also

- [init(layout: UnsafePointer<AudioChannelLayout>)](avaudiochannellayout/init(layout:).md)
  Creates an audio channel layout object from an existing one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiochannellayout/init(layouttag:))*
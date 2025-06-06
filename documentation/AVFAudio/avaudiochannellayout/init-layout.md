# init(layout:)

**Framework**: AVFAudio  
**Kind**: init

Creates an audio channel layout object from an existing one.

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
init(layout: UnsafePointer<AudioChannelLayout>)
```

#### Return Value

A new `AVAudioChannelLayout` object.

#### Discussion

If the audio channel layout object’s tag is [`kAudioChannelLayoutTag_UseChannelDescriptions`](https://developer.apple.com/documentation/CoreAudioTypes/kAudioChannelLayoutTag_UseChannelDescriptions), this initializer attempts to convert it to a more specific tag.

## Parameters

- `layout`: The existing audio channel layout object.

## See Also

- [var layout: UnsafePointer<AudioChannelLayout>](avaudiochannellayout/layout.md)
  The underlying audio channel layout.
- [convenience init?(layoutTag: AudioChannelLayoutTag)](avaudiochannellayout/init(layouttag:).md)
  Creates an audio channel layout object from a layout tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiochannellayout/init(layout:))*
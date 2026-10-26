# init(layoutTag:)

**Framework**: AVFAudio  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithLayoutTag:(AudioChannelLayoutTag) layoutTag;
```

#### Return Value

A new `AVAudioChannelLayout` object, or `nil` if `layoutTag` is [`kAudioChannelLayoutTag_UseChannelDescriptions`](../../CoreAudioTypes/kaudiochannellayouttag_usechanneldescriptions.md) or [`kAudioChannelLayoutTag_UseChannelBitmap`](../../CoreAudioTypes/kaudiochannellayouttag_usechannelbitmap.md).

## Parameters

- `layoutTag`: The audio channel layout tag.

## See Also

### Creating an audio channel layout
- [init(layout: UnsafePointer<AudioChannelLayout>)](./init%28layout%29.md)
  Creates an audio channel layout object from an existing one.
- [+ layoutWithLayout:](./layoutwithlayout_.md)
  Creates an audio channel layout object from an existing one.
- [+ layoutWithLayoutTag:](./layoutwithlayouttag_.md)
  Creates an audio channel layout object from an audio channel layout tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiochannellayout/init(layouttag:))*
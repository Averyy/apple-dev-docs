# layoutWithLayoutTag:

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Type Method

Creates an audio channel layout object from an audio channel layout tag.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (instancetype) layoutWithLayoutTag:(AudioChannelLayoutTag) layoutTag;
```

## Return Value

A new `AVAudioChannelLayout` object.

## Discussion

If the provided audio channel layout object’s tag is [`kAudioChannelLayoutTag_UseChannelDescriptions`](../../CoreAudioTypes/kaudiochannellayouttag_usechanneldescriptions.md), this initializer attempts to convert it to a more specific tag.

## Parameters

- `layoutTag`: The audio channel layout tag.

## See Also

### Creating an audio channel layout
- [init(layout: UnsafePointer<AudioChannelLayout>)](./init%28layout%29.md)
  Creates an audio channel layout object from an existing one.
- [+ layoutWithLayout:](./layoutwithlayout_.md)
  Creates an audio channel layout object from an existing one.
- [convenience init?(layoutTag: AudioChannelLayoutTag)](./init%28layouttag%29.md)
  Creates an audio channel layout object from a layout tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiochannellayout/layoutwithlayouttag:)*
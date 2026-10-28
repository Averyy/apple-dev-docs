# layoutWithLayout:

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (instancetype) layoutWithLayout:(const AudioChannelLayout *) layout;
```

## Return Value

A new `AVAudioChannelLayout` object.

## Discussion

If the layout’s tag is [`kAudioChannelLayoutTag_UseChannelDescriptions`](../../CoreAudioTypes/kaudiochannellayouttag_usechanneldescriptions.md), the method attempts to convert it to a more specific tag.

## Parameters

- `layout`: The existing audio channel layout object.

## See Also

### Creating an audio channel layout
- [init(layout: UnsafePointer<AudioChannelLayout>)](./init%28layout%29.md)
  Creates an audio channel layout object from an existing one.
- [convenience init?(layoutTag: AudioChannelLayoutTag)](./init%28layouttag%29.md)
  Creates an audio channel layout object from a layout tag.
- [+ layoutWithLayoutTag:](./layoutwithlayouttag_.md)
  Creates an audio channel layout object from an audio channel layout tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiochannellayout/layoutwithlayout:)*
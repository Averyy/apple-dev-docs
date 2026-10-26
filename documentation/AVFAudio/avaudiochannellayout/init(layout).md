# init(layout:)

**Framework**: AVFAudio  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithLayout:(const AudioChannelLayout *) layout;
```

#### Return Value

A new `AVAudioChannelLayout` object.

#### Discussion

If the audio channel layout object’s tag is [`kAudioChannelLayoutTag_UseChannelDescriptions`](../../CoreAudioTypes/kaudiochannellayouttag_usechanneldescriptions.md), this initializer attempts to convert it to a more specific tag.

## Parameters

- `layout`: The existing audio channel layout object.

## See Also

### Related Documentation
- [var layout: UnsafePointer<AudioChannelLayout>](./layout.md)
  The underlying audio channel layout.
### Creating an audio channel layout
- [convenience init?(layoutTag: AudioChannelLayoutTag)](./init%28layouttag%29.md)
  Creates an audio channel layout object from a layout tag.
- [+ layoutWithLayout:](./layoutwithlayout_.md)
  Creates an audio channel layout object from an existing one.
- [+ layoutWithLayoutTag:](./layoutwithlayouttag_.md)
  Creates an audio channel layout object from an audio channel layout tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiochannellayout/init(layout:))*
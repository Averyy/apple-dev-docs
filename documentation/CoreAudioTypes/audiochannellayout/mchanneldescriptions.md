# mChannelDescriptions

**Framework**: Core Audio Types  
**Kind**: property

A variable length array of `mNumberChannelDescription` elements that describes a layout. If the `mChannelLayoutTag` field is set to `kAudioChannelLayoutTag_UseChannelDescriptions`, use this field to describe the layout.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var mChannelDescriptions: AudioChannelDescription
```

## See Also

- [var mChannelBitmap: AudioChannelBitmap](audiochannellayout/mchannelbitmap.md)
  If `mChannelLayoutTag` is set to `kAudioChannelLayoutTag_UseChannelBitmap`, this field is the channel-use bitmap.
- [struct AudioChannelBitmap](audiochannelbitmap.md)
  The supported channel bitmaps to use when defining channel layouts.
- [var mChannelLayoutTag: AudioChannelLayoutTag](audiochannellayout/mchannellayouttag.md)
  The `AudioChannelLayoutTag` value that indicates the layout. See [`Audio Channel Layout Tags`](audio-channel-layout-tags.md) for possible values.
- [typealias AudioChannelLayoutTag](audiochannellayouttag.md)
  Identifies a previously-defined channel layout.
- [Audio Channel Layout Tags](audio-channel-layout-tags.md)
  The identifiers that represent audio channel layouts.
- [var mNumberChannelDescriptions: UInt32](audiochannellayout/mnumberchanneldescriptions.md)
  The number of items in the `mChannelDescriptions` array.
- [func AudioChannelLayoutTag_GetNumberOfChannels(AudioChannelLayoutTag) -> UInt32](audiochannellayouttag_getnumberofchannels(_:).md)
  Retrieves the number of channels from an audio channel layout tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audiochannellayout/mchanneldescriptions)*
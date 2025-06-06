# AudioChannelLayoutTag_GetNumberOfChannels(_:)

**Framework**: Core Audio Types  
**Kind**: func

Retrieves the number of channels from an audio channel layout tag.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func AudioChannelLayoutTag_GetNumberOfChannels(_ inLayoutTag: AudioChannelLayoutTag) -> UInt32
```

#### Return Value

A count of audio channels.

## Parameters

- `inLayoutTag`: The layout tag from which to retrieve the number of channels.

## See Also

- [var mChannelBitmap: AudioChannelBitmap](audiochannellayout/mchannelbitmap.md)
  If `mChannelLayoutTag` is set to `kAudioChannelLayoutTag_UseChannelBitmap`, this field is the channel-use bitmap.
- [struct AudioChannelBitmap](audiochannelbitmap.md)
  The supported channel bitmaps to use when defining channel layouts.
- [var mChannelDescriptions: AudioChannelDescription](audiochannellayout/mchanneldescriptions.md)
  A variable length array of `mNumberChannelDescription` elements that describes a layout. If the `mChannelLayoutTag` field is set to `kAudioChannelLayoutTag_UseChannelDescriptions`, use this field to describe the layout.
- [var mChannelLayoutTag: AudioChannelLayoutTag](audiochannellayout/mchannellayouttag.md)
  The `AudioChannelLayoutTag` value that indicates the layout. See [`Audio Channel Layout Tags`](audio-channel-layout-tags.md) for possible values.
- [typealias AudioChannelLayoutTag](audiochannellayouttag.md)
  Identifies a previously-defined channel layout.
- [Audio Channel Layout Tags](audio-channel-layout-tags.md)
  The identifiers that represent audio channel layouts.
- [var mNumberChannelDescriptions: UInt32](audiochannellayout/mnumberchanneldescriptions.md)
  The number of items in the `mChannelDescriptions` array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audiochannellayouttag_getnumberofchannels(_:))*
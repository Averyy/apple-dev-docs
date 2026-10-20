# AudioChannelLayout

**Framework**: Core Audio Types  
**Kind**: struct  
**Role**: Structure

A structure that specifies a channel layout in a file or in hardware.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
struct AudioChannelLayout
```

```c
struct AudioChannelLayout;
```

## Topics

### Accessing the Data
- [var mChannelBitmap: AudioChannelBitmap](./audiochannellayout/mchannelbitmap.md)
  If `mChannelLayoutTag` is set to `kAudioChannelLayoutTag_UseChannelBitmap`, this field is the channel-use bitmap.
- [struct AudioChannelBitmap](./audiochannelbitmap.md)
  The supported channel bitmaps to use when defining channel layouts.
- [var mChannelDescriptions: AudioChannelDescription](./audiochannellayout/mchanneldescriptions.md)
  A variable length array of `mNumberChannelDescription` elements that describes a layout. If the `mChannelLayoutTag` field is set to `kAudioChannelLayoutTag_UseChannelDescriptions`, use this field to describe the layout.
- [var mChannelLayoutTag: AudioChannelLayoutTag](./audiochannellayout/mchannellayouttag.md)
  The `AudioChannelLayoutTag` value that indicates the layout. See [Audio Channel Layout Tags](./audio-channel-layout-tags.md) for possible values.
- [typealias AudioChannelLayoutTag](./audiochannellayouttag.md)
  Identifies a previously-defined channel layout.
- [Audio Channel Layout Tags](./audio-channel-layout-tags.md)
  The identifiers that represent audio channel layouts.
- [var mNumberChannelDescriptions: UInt32](./audiochannellayout/mnumberchanneldescriptions.md)
  The number of items in the `mChannelDescriptions` array.
- [func AudioChannelLayoutTag_GetNumberOfChannels(AudioChannelLayoutTag) -> UInt32](./audiochannellayouttag_getnumberofchannels%28_%29.md)
  Retrieves the number of channels from an audio channel layout tag.
### Initializers
- [init()](./audiochannellayout/init%28%29.md)
- [init(mChannelLayoutTag: AudioChannelLayoutTag, mChannelBitmap: AudioChannelBitmap, mNumberChannelDescriptions: UInt32, mChannelDescriptions: AudioChannelDescription)](./audiochannellayout/init%28mchannellayouttag,mchannelbitmap,mnumberchanneldescriptions,mchanneldescriptions%29.md)
### Structures
- [AudioChannelLayout.UnsafeMutablePointer](./audiochannellayout/unsafemutablepointer.md)
- [AudioChannelLayout.UnsafePointer](./audiochannellayout/unsafepointer.md)
### Type Methods
- [static func allocate(maximumDescriptions: Int) -> AudioChannelLayout.UnsafeMutablePointer](./audiochannellayout/allocate%28maximumdescriptions%29.md)
- [static func sizeInBytes(maximumDescriptions: Int) -> Int](./audiochannellayout/sizeinbytes%28maximumdescriptions%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Channels
- [struct AudioChannelDescription](./audiochanneldescription.md)
  A structure that describes a channel of audio data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audiochannellayout)*
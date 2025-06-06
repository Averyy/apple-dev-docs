# AudioChannelBitmap

**Framework**: Core Audio Types  
**Kind**: struct

The supported channel bitmaps to use when defining channel layouts.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
struct AudioChannelBitmap
```

## Topics

### Left
- [static var bit_Left: AudioChannelBitmap](audiochannelbitmap/bit_left.md)
  The left channel.
- [static var bit_LeftCenter: AudioChannelBitmap](audiochannelbitmap/bit_leftcenter.md)
  The left center channel.
- [static var bit_LeftSurround: AudioChannelBitmap](audiochannelbitmap/bit_leftsurround.md)
  The left surround channel.
- [static var bit_LeftSurroundDirect: AudioChannelBitmap](audiochannelbitmap/bit_leftsurrounddirect.md)
  The left surround direct channel.
- [static var bit_LeftTopFront: AudioChannelBitmap](audiochannelbitmap/bit_lefttopfront.md)
  The left-top front channel.
- [static var bit_LeftTopMiddle: AudioChannelBitmap](audiochannelbitmap/bit_lefttopmiddle.md)
  The left-top middle channel.
- [static var bit_LeftTopRear: AudioChannelBitmap](audiochannelbitmap/bit_lefttoprear.md)
  The left-top rear channel.
- [static var bit_TopBackLeft: AudioChannelBitmap](audiochannelbitmap/bit_topbackleft.md)
  The top-back left channel.
- [static var bit_VerticalHeightLeft: AudioChannelBitmap](audiochannelbitmap/bit_verticalheightleft.md)
  The vertical height left channel.
### Center
- [static var bit_Center: AudioChannelBitmap](audiochannelbitmap/bit_center.md)
  The center channel.
- [static var bit_CenterSurround: AudioChannelBitmap](audiochannelbitmap/bit_centersurround.md)
  The center surround channel.
- [static var bit_CenterTopFront: AudioChannelBitmap](audiochannelbitmap/bit_centertopfront.md)
  The top-front center channel.
- [static var bit_CenterTopMiddle: AudioChannelBitmap](audiochannelbitmap/bit_centertopmiddle.md)
  The top-middle center channel.
- [static var bit_CenterTopRear: AudioChannelBitmap](audiochannelbitmap/bit_centertoprear.md)
  The top-right center channel.
- [static var bit_TopBackCenter: AudioChannelBitmap](audiochannelbitmap/bit_topbackcenter.md)
  The top-back center channel.
- [static var bit_TopCenterSurround: AudioChannelBitmap](audiochannelbitmap/bit_topcentersurround.md)
  The top center surround channel.
- [static var bit_VerticalHeightCenter: AudioChannelBitmap](audiochannelbitmap/bit_verticalheightcenter.md)
  The vertical height center channel.
### Right
- [static var bit_Right: AudioChannelBitmap](audiochannelbitmap/bit_right.md)
  The right channel.
- [static var bit_RightCenter: AudioChannelBitmap](audiochannelbitmap/bit_rightcenter.md)
  The right center channel.
- [static var bit_RightSurround: AudioChannelBitmap](audiochannelbitmap/bit_rightsurround.md)
  The rIght surround channel.
- [static var bit_RightSurroundDirect: AudioChannelBitmap](audiochannelbitmap/bit_rightsurrounddirect.md)
  The right surround direct channel.
- [static var bit_RightTopFront: AudioChannelBitmap](audiochannelbitmap/bit_righttopfront.md)
  The top-front front channel.
- [static var bit_RightTopMiddle: AudioChannelBitmap](audiochannelbitmap/bit_righttopmiddle.md)
  The top-middle right channel.
- [static var bit_RightTopRear: AudioChannelBitmap](audiochannelbitmap/bit_righttoprear.md)
  The top-rear right channel.
- [static var bit_TopBackRight: AudioChannelBitmap](audiochannelbitmap/bit_topbackright.md)
  The top-back right channel.
- [static var bit_VerticalHeightRight: AudioChannelBitmap](audiochannelbitmap/bit_verticalheightright.md)
  The vertical height right channel.
### Low-Frequency Effects
- [static var bit_LFEScreen: AudioChannelBitmap](audiochannelbitmap/bit_lfescreen.md)
  The Low Frequency Effects (LFE) screen channel.
### Initializers
- [init(rawValue: UInt32)](audiochannelbitmap/init(rawvalue:).md)
  Creates an audio channel bitmap.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var mChannelBitmap: AudioChannelBitmap](audiochannellayout/mchannelbitmap.md)
  If `mChannelLayoutTag` is set to `kAudioChannelLayoutTag_UseChannelBitmap`, this field is the channel-use bitmap.
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
- [func AudioChannelLayoutTag_GetNumberOfChannels(AudioChannelLayoutTag) -> UInt32](audiochannellayouttag_getnumberofchannels(_:).md)
  Retrieves the number of channels from an audio channel layout tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audiochannelbitmap)*
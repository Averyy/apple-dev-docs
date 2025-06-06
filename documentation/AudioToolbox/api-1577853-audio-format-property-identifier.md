# Audio Format Property Identifiers

**Framework**: Audio Toolbox

Constants for use with the [`AudioFormatGetPropertyInfo(_:_:_:_:)`](audioformatgetpropertyinfo(_:_:_:_:).md) and [`AudioFormatGetProperty(_:_:_:_:_:)`](audioformatgetproperty(_:_:_:_:_:).md) functions.

## Topics

### Constants
- [var kAudioFormatProperty_FormatInfo: AudioFormatPropertyID](kaudioformatproperty_formatinfo.md)
  General information about a format. Set the `inSpecifier` parameter to a magic cookie, or `NULL`. On input, the property value is an `AudioStreamBasicDescription` structure which should have at least the `mFormatID` field filled out. On output, the structure will be filled out as much as possible given the information known about the format and the contents of the magic cookie (if any is given). If multiple formats can be described by the `AudioStreamBasicDescription` and the associated magic cookie, this property will return the base level format.
- [var kAudioFormatProperty_FormatName: AudioFormatPropertyID](kaudioformatproperty_formatname.md)
  A name for a given format. Set the `inSpecifier` parameter to an `AudioStreamBasicDescription` structure describing the format to ask about. The value is a `CFStringRef` object. The caller is responsible for releasing the returned string. For some formats, such as linear PCM, you get back a descriptive string, for example, “16-bit, interleaved.”
- [var kAudioFormatProperty_EncodeFormatIDs: AudioFormatPropertyID](kaudioformatproperty_encodeformatids.md)
  An array of `UInt32` values representing format identifiers for formats that are valid output formats for a converter. You must set the `inSpecifier` parameter to `NULL`.
- [var kAudioFormatProperty_DecodeFormatIDs: AudioFormatPropertyID](kaudioformatproperty_decodeformatids.md)
  An array of `UInt32` values representing format identifiers for formats that are valid input formats for a converter. You must set the `inSpecifier` parameter to `NULL`.
- [var kAudioFormatProperty_FormatList: AudioFormatPropertyID](kaudioformatproperty_formatlist.md)
  A list of structures describing the audio formats.
- [var kAudioFormatProperty_ASBDFromESDS: AudioFormatPropertyID](kaudioformatproperty_asbdfromesds.md)
  An `AudioStreamBasicDescription` structure for a given elementary stream descriptor (ESDS). Set the `inSpecifier` parameter to an ESDS. If multiple formats can be described by the ESDS, this property will return the base level format.
- [var kAudioFormatProperty_ChannelLayoutFromESDS: AudioFormatPropertyID](kaudioformatproperty_channellayoutfromesds.md)
  An `AudioChannelLayout` structure for a given elementary stream descriptor (ESDS).
- [var kAudioFormatProperty_OutputFormatList: AudioFormatPropertyID](kaudioformatproperty_outputformatlist.md)
  A list of structures describing the audio formats.
- [var kAudioFormatProperty_FirstPlayableFormatFromList: AudioFormatPropertyID](kaudioformatproperty_firstplayableformatfromlist.md)
  The index of the first `AudioFormatListItem` that represents an audio format.
- [var kAudioFormatProperty_Encoders: AudioFormatPropertyID](kaudioformatproperty_encoders.md)
  An array of `AudioClassDescription` structures for all installed encoders for the specified audio format. Set the `inSpecifier` parameter to the format that you are interested in, for instance, `'aac'`.
- [var kAudioFormatProperty_Decoders: AudioFormatPropertyID](kaudioformatproperty_decoders.md)
  An array of `AudioClassDescription` structures for all installed decoders for the specified audio format. Set the `inSpecifier` parameter to the format that you are interested in, for instance, `'aac'`.
- [var kAudioFormatProperty_FormatIsVBR: AudioFormatPropertyID](kaudioformatproperty_formatisvbr.md)
  Indicates whether or not a format has a variable number of bytes-per-packet.
- [var kAudioFormatProperty_FormatIsExternallyFramed: AudioFormatPropertyID](kaudioformatproperty_formatisexternallyframed.md)
  Indicates whether or not a format requires external framing information.
- [var kAudioFormatProperty_AvailableEncodeBitRates: AudioFormatPropertyID](kaudioformatproperty_availableencodebitrates.md)
  An array of `AudioValueRange` structures describing all available bit rates.
- [var kAudioFormatProperty_AvailableEncodeSampleRates: AudioFormatPropertyID](kaudioformatproperty_availableencodesamplerates.md)
  An array of `AudioValueRange` structures.
- [var kAudioFormatProperty_AvailableEncodeChannelLayoutTags: AudioFormatPropertyID](kaudioformatproperty_availableencodechannellayouttags.md)
  An array of `AudioChannelLayoutTag` values for the format and number of channels specified.
- [var kAudioFormatProperty_AvailableEncodeNumberChannels: AudioFormatPropertyID](kaudioformatproperty_availableencodenumberchannels.md)
  An array of `UInt32` values indicating the number of channels that can be encoded.
- [var kAudioFormatProperty_ASBDFromMPEGPacket: AudioFormatPropertyID](kaudioformatproperty_asbdfrommpegpacket.md)
  An `AudioStreamBasicDescription` structure for a given MPEG Packet.
- [var kAudioFormatProperty_BitmapForLayoutTag: AudioFormatPropertyID](kaudioformatproperty_bitmapforlayouttag.md)
  A bitmap for an `AudioChannelLayoutTag` value.
- [var kAudioFormatProperty_MatrixMixMap: AudioFormatPropertyID](kaudioformatproperty_matrixmixmap.md)
  A matrix of scaling coefficients for converting audio from one channel map to another in a standard way, if one is known. Otherwise, an error is returned. Set the `inSpecifier` parameter to an array of two pointers to `AudioChannelLayout` structures. The first points to the input layout, the second to the output layout. The value is a two dimensional array of `Float32` values, where the first dimension (rows) is the input channel and the second dimension (columns) is the output channel.
- [var kAudioFormatProperty_ChannelMap: AudioFormatPropertyID](kaudioformatproperty_channelmap.md)
  An array of `SInt32` values for reordering input channels. Set the `inSpecifier` parameter to an array of two pointers to `AudioChannelLayout` structures. The first points to the input layout, the second to the output layout. The length of the output array is equal to the number of output channels.
- [var kAudioFormatProperty_NumberOfChannelsForLayout: AudioFormatPropertyID](kaudioformatproperty_numberofchannelsforlayout.md)
  The number of valid channels.
- [var kAudioFormatProperty_ValidateChannelLayout: AudioFormatPropertyID](kaudioformatproperty_validatechannellayout.md)
  The validity of an audio channel layout structure.
- [var kAudioFormatProperty_ChannelLayoutForTag: AudioFormatPropertyID](kaudioformatproperty_channellayoutfortag.md)
  The channel descriptions for a standard channel layout.
- [var kAudioFormatProperty_TagForChannelLayout: AudioFormatPropertyID](kaudioformatproperty_tagforchannellayout.md)
  An `AudioChannelLayoutTag` value for a layout.
- [var kAudioFormatProperty_ChannelLayoutName: AudioFormatPropertyID](kaudioformatproperty_channellayoutname.md)
  The a name for a particular channel layout.
- [var kAudioFormatProperty_ChannelLayoutSimpleName: AudioFormatPropertyID](kaudioformatproperty_channellayoutsimplename.md)
  A simplified name for channel layout.
- [var kAudioFormatProperty_ChannelLayoutForBitmap: AudioFormatPropertyID](kaudioformatproperty_channellayoutforbitmap.md)
  The channel descriptions for a standard channel layout,
- [var kAudioFormatProperty_ChannelName: AudioFormatPropertyID](kaudioformatproperty_channelname.md)
  The name for a particular channel.
- [var kAudioFormatProperty_ChannelShortName: AudioFormatPropertyID](kaudioformatproperty_channelshortname.md)
  An abbreviated name for a particular channel.
- [var kAudioFormatProperty_TagsForNumberOfChannels: AudioFormatPropertyID](kaudioformatproperty_tagsfornumberofchannels.md)
  An array of AudioChannelLayoutTag values for the number of channels specified. The specifier is a `UInt32` value that indicates the number of channels.
- [var kAudioFormatProperty_PanningMatrix: AudioFormatPropertyID](kaudioformatproperty_panningmatrix.md)
  An array of `Float32` values, each representing the audio level of one channel.
- [var kAudioFormatProperty_BalanceFade: AudioFormatPropertyID](kaudioformatproperty_balancefade.md)
  An array of coefficients, each a `Float32` value, for applying left/right audio balance and front/back audio fade.
- [var kAudioFormatProperty_ID3TagSize: AudioFormatPropertyID](kaudioformatproperty_id3tagsize.md)
  A `UInt32` value indicating the ID3 tag size. The `inSpecifier` parameter must begin with the ID3 tag header and be at least 10 bytes in length.
- [var kAudioFormatProperty_ID3TagToDictionary: AudioFormatPropertyID](kaudioformatproperty_id3tagtodictionary.md)
  A `CFDictionary` object containing key/value pairs for the frames in the ID3 tag. Set the `inSpecifier` parameter to the entire ID3 tag. The caller must call the `CFRelease` function for the returned dictionary.
- [var kAudioFormatProperty_AreChannelLayoutsEquivalent: AudioFormatPropertyID](kaudioformatproperty_arechannellayoutsequivalent.md)
- [var kAudioFormatProperty_ChannelLayoutHash: AudioFormatPropertyID](kaudioformatproperty_channellayouthash.md)
- [var kAudioFormatProperty_FormatIsEncrypted: AudioFormatPropertyID](kaudioformatproperty_formatisencrypted.md)
- [var kAudioFormatProperty_AvailableDecodeNumberChannels: AudioFormatPropertyID](kaudioformatproperty_availabledecodenumberchannels.md)
- [var kAudioFormatProperty_FormatEmploysDependentPackets: AudioFormatPropertyID](kaudioformatproperty_formatemploysdependentpackets.md)

## See Also

- [enum AudioBalanceFadeType](audiobalancefadetype.md)
  Identifiers for audio balance fade types.
- [Audio Codec Component Constants](1494086-audio-codec-component-constants.md)
  Audio codec component types.
- [Audio Codec Manufacturer and Implementation Types](1620448-audio-codec-manufacturer-and-imp.md)
  Identifiers for audio codec manufacturers and implementation types.
- [enum AudioPanningMode](audiopanningmode.md)
  Identifiers for audio panning algorithms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/1577853-audio-format-property-identifier)*
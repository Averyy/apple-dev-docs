# kAudioFormatProperty_FormatIsExternallyFramed

**Framework**: Audio Toolbox  
**Kind**: var

Indicates whether or not a format requires external framing information.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var kAudioFormatProperty_FormatIsExternallyFramed: AudioFormatPropertyID { get }
```

#### Discussion

Indicates whether or not a format requires external framing information in the form of [`AudioStreamPacketDescription`](https://developer.apple.com/documentation/CoreAudioTypes/AudioStreamPacketDescription) structures. The specifier is an [`AudioStreamBasicDescription`](https://developer.apple.com/documentation/CoreAudioTypes/AudioStreamBasicDescription) structure describing the format to ask about. The value is a `UInt32` where nonzero means the format is externally framed. Any format that has variable-byte-sized packets requires packet descriptions.

## See Also

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
- [var kAudioFormatProperty_AvailableEncodeBitRates: AudioFormatPropertyID](kaudioformatproperty_availableencodebitrates.md)
  An array of `AudioValueRange` structures describing all available bit rates.
- [var kAudioFormatProperty_AvailableEncodeSampleRates: AudioFormatPropertyID](kaudioformatproperty_availableencodesamplerates.md)
  An array of `AudioValueRange` structures.
- [var kAudioFormatProperty_AvailableEncodeChannelLayoutTags: AudioFormatPropertyID](kaudioformatproperty_availableencodechannellayouttags.md)
  An array of `AudioChannelLayoutTag` values for the format and number of channels specified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudioformatproperty_formatisexternallyframed)*
# frameQuanta

**Framework**: Core Media  
**Kind**: property

The frames per second for the time code, or the frame per tick for counter mode.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var frameQuanta: UInt32 { get }
```

## See Also

- [var audioFormatList: [AudioFormatListItem]](cmformatdescription/audioformatlist.md)
  The audio format list items that describe the audio formats.
- [var audioStreamBasicDescription: AudioStreamBasicDescription?](cmformatdescription/audiostreambasicdescription.md)
  The audio stream description.
- [var audioChannelLayout: ManagedAudioChannelLayout?](cmformatdescription/audiochannellayout.md)
  The audio channel layout.
- [var dimensions: CMVideoDimensions](cmformatdescription/dimensions.md)
  The encoded pixels not including the pixel aspect ratio or clean aperture tags.
- [var extensions: CMFormatDescription.Extensions](cmformatdescription/extensions-swift.property.md)
  A dictionary that contains all of the extensions.
- [var frameDuration: CMTime](cmformatdescription/frameduration.md)
  The duration of each frame.
- [var identifiers: [String]](cmformatdescription/identifiers.md)
  An array of metadata identifiers.
- [var magicCookie: Data?](cmformatdescription/magiccookie.md)
  A copy of the magic cookie, if any.
- [var mediaSubType: CMFormatDescription.MediaSubType](cmformatdescription/mediasubtype-swift.property.md)
  The media subtype.
- [var mediaType: CMFormatDescription.MediaType](cmformatdescription/mediatype-swift.property.md)
  The media type.
- [var mostCompatibleFormat: AudioFormatListItem?](cmformatdescription/mostcompatibleformat.md)
  The most compatible audio format list item.
- [var nalUnitHeaderLength: Int?](cmformatdescription/nalunitheaderlength.md)
  The size, in bytes, of the unit length field in an AVC or HEVC video sample or parameter set sample.
- [var parameterSets: CMFormatDescription.ParameterSetCollection](cmformatdescription/parametersets.md)
  The parameter sets that an H.264 or HEVC format contains.
- [var richestDecodableFormat: AudioFormatListItem?](cmformatdescription/richestdecodableformat.md)
  The audio format list item the system validates.
- [var timeCodeFlags: CMFormatDescription.TimeCode.Flag](cmformatdescription/timecodeflags.md)
  The flags for the available time codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmformatdescription/framequanta)*
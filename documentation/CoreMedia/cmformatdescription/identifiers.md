# identifiers

**Framework**: Core Media  
**Kind**: property  
**Role**: Instance Property

An array of metadata identifiers.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var identifiers: [String] { get }
```

## See Also

### Inspecting Format Descriptions
- [var audioFormatList: [AudioFormatListItem]](./audioformatlist.md)
  The audio format list items that describe the audio formats.
- [var audioStreamBasicDescription: AudioStreamBasicDescription?](./audiostreambasicdescription.md)
  The audio stream description.
- [var audioChannelLayout: ManagedAudioChannelLayout?](./audiochannellayout.md)
  The audio channel layout.
- [var dimensions: CMVideoDimensions](./dimensions.md)
  The encoded pixels not including the pixel aspect ratio or clean aperture tags.
- [var extensions: CMFormatDescription.Extensions](./extensions-swift.property.md)
  A dictionary that contains all of the extensions.
- [var frameDuration: CMTime](./frameduration.md)
  The duration of each frame.
- [var frameQuanta: UInt32](./framequanta.md)
  The frames per second for the time code, or the frame per tick for counter mode.
- [var magicCookie: Data?](./magiccookie.md)
  A copy of the magic cookie, if any.
- [var mediaSubType: CMFormatDescription.MediaSubType](./mediasubtype-swift.property.md)
  The media subtype.
- [var mediaType: CMFormatDescription.MediaType](./mediatype-swift.property.md)
  The media type.
- [var mostCompatibleFormat: AudioFormatListItem?](./mostcompatibleformat.md)
  The most compatible audio format list item.
- [var nalUnitHeaderLength: Int?](./nalunitheaderlength.md)
  The size, in bytes, of the unit length field in an AVC or HEVC video sample or parameter set sample.
- [var parameterSets: CMFormatDescription.ParameterSetCollection](./parametersets.md)
  The parameter sets that an H.264 or HEVC format contains.
- [var richestDecodableFormat: AudioFormatListItem?](./richestdecodableformat.md)
  The audio format list item the system validates.
- [var timeCodeFlags: CMFormatDescription.TimeCode.Flag](./timecodeflags.md)
  The flags for the available time codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmformatdescription/identifiers)*
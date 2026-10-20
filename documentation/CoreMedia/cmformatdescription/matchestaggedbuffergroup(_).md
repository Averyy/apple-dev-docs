# matchesTaggedBufferGroup(_:)

**Framework**: Core Media  
**Kind**: method  
**Role**: Instance Method

Whether the format description matches a set of tagged buffers.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func matchesTaggedBufferGroup(_ taggedBuffers: [CMTaggedBuffer]) -> Bool
```

#### Return Value

Returns `true` if the description contains a tag collection matching the tags of the buffer group, `false` otherwise.

## Parameters

- `taggedBuffers`: An array of tagged buffers to match tags against this media description.

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
- [var identifiers: [String]](./identifiers.md)
  An array of metadata identifiers.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmformatdescription/matchestaggedbuffergroup(_:))*
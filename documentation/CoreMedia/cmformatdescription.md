# CMFormatDescription

**Framework**: Core Media  
**Kind**: class

An object that describes a media format descriptor.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class CMFormatDescription
```

#### Overview

A `CMFormatDescription` object is an object that describes media types (audio, video, muxed, and so on).

## Topics

### Inspecting Format Descriptions
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
- [var frameQuanta: UInt32](cmformatdescription/framequanta.md)
  The frames per second for the time code, or the frame per tick for counter mode.
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
- [var tagCollections: [[CMTag]]?](cmformatdescription/tagcollections.md)
  The tag collections associated with this media.
- [func matchesTaggedBufferGroup([CMTaggedBuffer]) -> Bool](cmformatdescription/matchestaggedbuffergroup(_:).md)
  Whether the format description matches a set of tagged buffers.
### Working with Audio Descriptions
- [func withMagicCookie<R>((UnsafeRawBufferPointer?) throws -> R) rethrows -> R](cmformatdescription/withmagiccookie(_:).md)
  Returns the magic cookie.
### Working with Video Descriptions
- [func cleanAperture(originIsAtTopLeft: Bool) -> CGRect](cmformatdescription/cleanaperture(originisattopleft:).md)
  Returns the clean aperture.
- [func matchesImageBuffer(CVImageBuffer) -> Bool](cmformatdescription/matchesimagebuffer(_:).md)
  Returns a Boolean value that indicates whether the format description matches an image buffer.
- [func presentationDimensions(usePixelAspectRatio: Bool, useCleanAperture: Bool) -> CGSize](cmformatdescription/presentationdimensions(usepixelaspectratio:usecleanaperture:).md)
  Returns the dimensions to take the pixel aspect ratio or clean aperture into account.
### Working with Metadata Descriptions
- [func keyWithLocalID(OSType) -> [String : CFPropertyList]?](cmformatdescription/keywithlocalid(_:).md)
  Returns the metadata for the local identifier you specify.
### Working with Text Descriptions
- [func defaultStyle() throws -> (localFontID: Int, bold: Bool, italic: Bool, underline: Bool, fontSize: CGFloat, colorComponents: [CGFloat])](cmformatdescription/defaultstyle.md)
  Returns the default text style.
- [func defaultTextBox(originIsAtTopLeft: Bool, heightOfTextTrack: CGFloat) throws -> CGRect](cmformatdescription/defaulttextbox(originisattopleft:heightoftexttrack:).md)
  Returns the default text box.
- [func displayFlags() throws -> CMFormatDescription.Extensions.Value.TextDisplayFlags](cmformatdescription/displayflags.md)
  Returns the display mode flags for the text media.
- [func fontName(localFontID: Int) throws -> String](cmformatdescription/fontname(localfontid:).md)
  Returns the font name for the local font identifier.
- [func justification() throws -> (horizontal: CMFormatDescription.Extensions.Value.TextJustification, vertical: CMFormatDescription.Extensions.Value.TextJustification)](cmformatdescription/justification.md)
  Returns the horizontal and vertical justification.
### Comparing Format Descriptions
- [static func == (CMFormatDescription, CMFormatDescription) -> Bool](cmformatdescription/==(_:_:).md)
  Equality is derived from
- [func equalTo(CMAudioFormatDescription, equalityMask: CMFormatDescription.EqualityMask) -> (Bool, equalityMask: CMFormatDescription.EqualityMask)](cmformatdescription/equalto(_:equalitymask:).md)
  Evaluates equality for the parts of two audio format descriptions.
- [func equalTo(CMFormatDescription, extensionKeysToIgnore: [CMFormatDescription.Extensions.Key], sampleDescriptionExtensionAtomKeysToIgnore: [String]) -> Bool](cmformatdescription/equalto(_:extensionkeystoignore:sampledescriptionextensionatomkeystoignore:).md)
  Evaluates equality for the parts of two audio format descriptions, ignoring the extensions you specify.
### Errors
- [CMFormatDescription.Error](cmformatdescription/error.md)
  A type that describes format description errors.
### Constants
- [static var extensionKeysCommonWithImageBuffers: [CMFormatDescription.Extensions.Key]](cmformatdescription/extensionkeyscommonwithimagebuffers.md)
  A constant that represents keys you use with video format description extensions and image buffers.
- [static var typeID: CFTypeID](cmformatdescription/typeid.md)
  A type identifier that corresponds to a description object.
- [CMFormatDescription.MediaType](cmformatdescription/mediatype-swift.struct.md)
  A type that describes format description media.
- [CMFormatDescription.MediaSubType](cmformatdescription/mediasubtype-swift.struct.md)
  A type that describes format description media subtypes.
- [CMFormatDescription.TimeCode](cmformatdescription/timecode.md)
  A type that describes format description time codes.
- [CMFormatDescription.EqualityMask](cmformatdescription/equalitymask.md)
  A type that describes format description equality masks.
- [CMFormatDescription.Extensions](cmformatdescription/extensions-swift.struct.md)
  A type that describes format description extensions.
- [CMFormatDescription.ParameterSetCollection](cmformatdescription/parametersetcollection.md)
  A type that describes format description parameter sets.
### Initializers
- [init(referencing: CMFormatDescription)](cmformatdescription/init(referencing:).md)
### Type Aliases
- [CMFormatDescription.T](cmformatdescription/t.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [typealias CMAudioFormatDescription](cmaudioformatdescription.md)
  A type you use to interact with audio format descriptions.
- [typealias CMClosedCaptionFormatDescription](cmclosedcaptionformatdescription.md)
  A type you use to interact with closed caption format descriptions.
- [typealias CMMetadataFormatDescription](cmmetadataformatdescription.md)
  A type you use to interact with metadata format descriptions.
- [typealias CMMuxedFormatDescription](cmmuxedformatdescription.md)
  A type you use to interact with muxed format descriptions.
- [typealias CMTextFormatDescription](cmtextformatdescription.md)
  A type you use to interact with text format descriptions.
- [typealias CMTimeCodeFormatDescription](cmtimecodeformatdescription.md)
  A type you use to interact with time code format descriptions.
- [typealias CMVideoFormatDescription](cmvideoformatdescription.md)
  A type you use to interact with video format descriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmformatdescription)*
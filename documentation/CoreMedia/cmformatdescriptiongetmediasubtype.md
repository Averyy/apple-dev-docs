# CMFormatDescriptionGetMediaSubType(_:)

**Framework**: Core Media  
**Kind**: func

Returns the media subtype of a format description.

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
func CMFormatDescriptionGetMediaSubType(_ desc: CMFormatDescription) -> FourCharCode
```

#### Return Value

A media type that identifies the subtype of the `CMFormatDescription`.

#### Discussion

For audio streams, the media subtype is the `asbd.mFormatID`. For video streams, the media subtype is the video codec type. For muxed streams, it’s the format of the muxed stream.

For example, the function returns `aac` for a description of an AAC audio stream, `avc1` for a description of an H.264 video stream, and `mp2t` for a description of an MPEG-2 transport (muxed) stream.  If a media stream doesn’t have subtypes, this API may return `0`.

## Parameters

- `desc`: The   to examine.

## See Also

- [func CMFormatDescriptionGetMediaType(CMFormatDescription) -> CMMediaType](cmformatdescriptiongetmediatype(_:).md)
  Returns the media type of a format description.
- [func CMFormatDescriptionGetExtension(CMFormatDescription, extensionKey: CFString) -> CFPropertyList?](cmformatdescriptiongetextension(_:extensionkey:).md)
  Returns an extension from the format description by using an extension key.
- [func CMFormatDescriptionGetExtensions(CMFormatDescription) -> CFDictionary?](cmformatdescriptiongetextensions(_:).md)
  Returns all of the extensions for a format description.
- [func CMFormatDescriptionGetTypeID() -> CFTypeID](cmformatdescriptiongettypeid().md)
  Returns the Core Foundation type identifier that identifies format description objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmformatdescriptiongetmediasubtype(_:))*
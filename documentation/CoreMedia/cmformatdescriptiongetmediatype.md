# CMFormatDescriptionGetMediaType(_:)

**Framework**: Core Media  
**Kind**: func

Returns the media type of a format description.

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
func CMFormatDescriptionGetMediaType(_ desc: CMFormatDescription) -> CMMediaType
```

#### Return Value

A media type that identifies the format description.

#### Discussion

For example, this function returns [`kCMMediaType_Audio`](kcmmediatype_audio.md) for a description of an audio stream.

## Parameters

- `desc`: A   to examine.

## See Also

- [func CMFormatDescriptionGetMediaSubType(CMFormatDescription) -> FourCharCode](cmformatdescriptiongetmediasubtype(_:).md)
  Returns the media subtype of a format description.
- [func CMFormatDescriptionGetExtension(CMFormatDescription, extensionKey: CFString) -> CFPropertyList?](cmformatdescriptiongetextension(_:extensionkey:).md)
  Returns an extension from the format description by using an extension key.
- [func CMFormatDescriptionGetExtensions(CMFormatDescription) -> CFDictionary?](cmformatdescriptiongetextensions(_:).md)
  Returns all of the extensions for a format description.
- [func CMFormatDescriptionGetTypeID() -> CFTypeID](cmformatdescriptiongettypeid().md)
  Returns the Core Foundation type identifier that identifies format description objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmformatdescriptiongetmediatype(_:))*
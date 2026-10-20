# CMFormatDescriptionGetMediaType(_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

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

```c
extern CMMediaType CMFormatDescriptionGetMediaType(CMFormatDescriptionRef desc);
```

#### Return Value

A media type that identifies the format description.

#### Discussion

For example, this function returns [`kCMMediaType_Audio`](./kcmmediatype_audio.md) for a description of an audio stream.

## Parameters

- `desc`: A `CMFormatDescription` to examine.

## See Also

### Inspecting Format Descriptions
- [func CMFormatDescriptionGetMediaSubType(CMFormatDescription) -> FourCharCode](./cmformatdescriptiongetmediasubtype%28_%29.md)
  Returns the media subtype of a format description.
- [func CMFormatDescriptionGetExtension(CMFormatDescription, extensionKey: CFString) -> CFPropertyList?](./cmformatdescriptiongetextension%28_,extensionkey%29.md)
  Returns an extension from the format description by using an extension key.
- [func CMFormatDescriptionGetExtensions(CMFormatDescription) -> CFDictionary?](./cmformatdescriptiongetextensions%28_%29.md)
  Returns all of the extensions for a format description.
- [func CMFormatDescriptionGetTypeID() -> CFTypeID](./cmformatdescriptiongettypeid%28%29.md)
  Returns the Core Foundation type identifier that identifies format description objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmformatdescriptiongetmediatype(_:))*
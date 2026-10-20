# CMFormatDescriptionGetTypeID()

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Returns the Core Foundation type identifier that identifies format description objects.

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
func CMFormatDescriptionGetTypeID() -> CFTypeID
```

```c
extern CFTypeID CMFormatDescriptionGetTypeID();
```

#### Discussion

You can check if a `CFTypeRef` object is a `CMFormatDescription` by comparing CFGetTypeID(object) with `CMFormatDescriptionGetTypeID`().

## See Also

### Inspecting Format Descriptions
- [func CMFormatDescriptionGetMediaType(CMFormatDescription) -> CMMediaType](./cmformatdescriptiongetmediatype%28_%29.md)
  Returns the media type of a format description.
- [func CMFormatDescriptionGetMediaSubType(CMFormatDescription) -> FourCharCode](./cmformatdescriptiongetmediasubtype%28_%29.md)
  Returns the media subtype of a format description.
- [func CMFormatDescriptionGetExtension(CMFormatDescription, extensionKey: CFString) -> CFPropertyList?](./cmformatdescriptiongetextension%28_,extensionkey%29.md)
  Returns an extension from the format description by using an extension key.
- [func CMFormatDescriptionGetExtensions(CMFormatDescription) -> CFDictionary?](./cmformatdescriptiongetextensions%28_%29.md)
  Returns all of the extensions for a format description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmformatdescriptiongettypeid())*
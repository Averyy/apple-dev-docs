# CMFormatDescriptionGetExtension(_:extensionKey:)

**Framework**: Core Media  
**Kind**: func

Returns an extension from the format description by using an extension key.

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
func CMFormatDescriptionGetExtension(_ desc: CMFormatDescription, extensionKey: CFString) -> CFPropertyList?
```

#### Return Value

An extension, or `NULL` if it doesn’t exist.

#### Discussion

The extension is always a valid property list object. This means that it will be either a `CFNumber`, `CFString`, `CFBoolean`, `CFArray`, `CFDictionary`, `CFDate`, or `CFData`. If it’s a `CFDictionary`, the keys will all be `CFStrings`. The extension this function returns is not retained by this call, so it’s only valid as long as the `CMFormatDescription` is valid — retain it to keep it longer.

## Parameters

- `desc`: The   to examine.
- `extensionKey`: The key of the extension to return. May not be  .

## See Also

- [func CMFormatDescriptionGetMediaType(CMFormatDescription) -> CMMediaType](cmformatdescriptiongetmediatype(_:).md)
  Returns the media type of a format description.
- [func CMFormatDescriptionGetMediaSubType(CMFormatDescription) -> FourCharCode](cmformatdescriptiongetmediasubtype(_:).md)
  Returns the media subtype of a format description.
- [func CMFormatDescriptionGetExtensions(CMFormatDescription) -> CFDictionary?](cmformatdescriptiongetextensions(_:).md)
  Returns all of the extensions for a format description.
- [func CMFormatDescriptionGetTypeID() -> CFTypeID](cmformatdescriptiongettypeid().md)
  Returns the Core Foundation type identifier that identifies format description objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmformatdescriptiongetextension(_:extensionkey:))*
# CMFormatDescriptionGetExtensions(_:)

**Framework**: Core Media  
**Kind**: func

Returns all of the extensions for a format description.

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
func CMFormatDescriptionGetExtensions(_ desc: CMFormatDescription) -> CFDictionary?
```

#### Return Value

An immutable dictionary that contains all the extensions of the `CMFormatDescription`.  May be `NULL`.

#### Discussion

If there are no extensions, the function returns `NULL`. Extensions dictionaries are valid property list objects.  This means that dictionary keys are all `CFStrings`, and the values are all either `CFNumber`, `CFString`, `CFBoolean`, `CFArray`, `CFDictionary`, `CFDate`, or `CFData`. The returned dictionary is not retained by this call, so clients are required to retain it if they need to keep it longer.

## Parameters

- `desc`: The   to examine.

## See Also

- [func CMFormatDescriptionGetMediaType(CMFormatDescription) -> CMMediaType](cmformatdescriptiongetmediatype(_:).md)
  Returns the media type of a format description.
- [func CMFormatDescriptionGetMediaSubType(CMFormatDescription) -> FourCharCode](cmformatdescriptiongetmediasubtype(_:).md)
  Returns the media subtype of a format description.
- [func CMFormatDescriptionGetExtension(CMFormatDescription, extensionKey: CFString) -> CFPropertyList?](cmformatdescriptiongetextension(_:extensionkey:).md)
  Returns an extension from the format description by using an extension key.
- [func CMFormatDescriptionGetTypeID() -> CFTypeID](cmformatdescriptiongettypeid().md)
  Returns the Core Foundation type identifier that identifies format description objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmformatdescriptiongetextensions(_:))*
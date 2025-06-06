# CGImageMetadataTagCreate(_:_:_:_:_:)

**Framework**: Image I/O  
**Kind**: func

Creates a new image metadata tag, and fills it with the specified information.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CGImageMetadataTagCreate(_ xmlns: CFString, _ prefix: CFString?, _ name: CFString, _ type: CGImageMetadataType, _ value: CFTypeRef) -> CGImageMetadataTag?
```

#### Return Value

A new [`CGImageMetadataTag`](cgimagemetadatatag.md) type, or `NULL` if an error occurred.

## Parameters

- `xmlns`: The namespace for the tag. Specify a common XMP namespace, such as  , or a string with a custom namespace URI. A custom namespace must be a valid XML namespace. By convention, namespaces end with either the   or   character.
- `prefix`: An abbreviation for the XML namespace. You must specify a valid string for custom namespace. For standard namespaces such as  , you may specify  .
- `name`: The name of the metadata tag. This string must correspond to a valid XMP name.
- `type`: The type of data in the   parameter. For a list of possible values, see  .
- `value`: The newly created tag stores only a shallow copy of the original value. As a result, modifying the original value doesn’t affect the value in the new  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagemetadatatagcreate(_:_:_:_:_:))*
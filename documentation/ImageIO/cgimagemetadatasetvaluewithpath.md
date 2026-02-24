# CGImageMetadataSetValueWithPath(_:_:_:_:)

**Framework**: Image I/O  
**Kind**: func

Update the value of an existing metadata tag, or create a new tag using the specified information.

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
func CGImageMetadataSetValueWithPath(_ metadata: CGMutableImageMetadata, _ parent: CGImageMetadataTag?, _ path: CFString, _ value: CFTypeRef) -> Bool
```

#### Return Value

`true` if this function set the tag successfully, or `false` if a problem occurred.

#### Discussion

As needed, this function creates any intermediate tags that are required to create the tag at the specified path. This function creates each tag with default types. Tag creation fails if the path includes an unregistered prefix.

If you specify a tag object in the `parent` parameter, this function modifies the children of that tag, which might create different references for those children. To fix the references, commit the changed parent back to the metadata object using the [`CGImageMetadataSetTagWithPath(_:_:_:_:)`](cgimagemetadatasettagwithpath(_:_:_:_:).md) function. Pass the parent’s full path string when calling that function; don’t specify the parent using a parent object and relative path.

## Parameters

- `metadata`: The metadata object that contains the tag. If the tag doesn’t exist in this metadata object, this function creates a new tag.
- `parent`: The parent tag, if any. Specify `NULL` to add or update a tag starting at the top-level of the metadata object. If this parameter is `NULL`, you must include a valid prefix string in the `path` parameter.
- `path`: A string that represents the path to the tag. A path consists of the tag’s name, plus optional prefix and parent information. Separate prefix information from other path information using a colon (`:`) character. Separate parent and child tags using the period (`.`) character. For example, the string `“exif:Flash.RedEyeMode”` represents the path to the `RedEyeMode` field of the `Flash` parent structure in the EXIF metadata. When a tag contains an ordered or unordered array, specify elements using a `0`-based index inside square brackets. For example, use the string `“dc.subject[2]”` to access the third element in the `subject` array. When the tag contains an alternate-text array, access elements using an RFC 3066 language code inside square brackets. For example, use the string `“dc.description[de]”` to access the German description information. Use the ? character to delimit qualifiers for tags with string values. You may not use this character for arrays and structures.
- `value`: The new value for the property. The new value’s type must match the expected XMP type of the property at the specified `path`.

## See Also

- [func CGImageMetadataSetValueMatchingImageProperty(CGMutableImageMetadata, CFString, CFString, CFTypeRef) -> Bool](cgimagemetadatasetvaluematchingimageproperty(_:_:_:_:).md)
  Updates the value of the metadata tag assigned to the specified image property.
- [func CGImageMetadataSetTagWithPath(CGMutableImageMetadata, CGImageMetadataTag?, CFString, CGImageMetadataTag) -> Bool](cgimagemetadatasettagwithpath(_:_:_:_:).md)
  Sets the tag at the specified path in the metadata object.
- [func CGImageMetadataRemoveTagWithPath(CGMutableImageMetadata, CGImageMetadataTag?, CFString) -> Bool](cgimagemetadataremovetagwithpath(_:_:_:).md)
  Removes the tag at the specified path from the metadata object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagemetadatasetvaluewithpath(_:_:_:_:))*
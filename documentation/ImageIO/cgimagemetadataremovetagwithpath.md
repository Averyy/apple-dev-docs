# CGImageMetadataRemoveTagWithPath(_:_:_:)

**Framework**: Image I/O  
**Kind**: func

Removes the tag at the specified path from the metadata object.

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
func CGImageMetadataRemoveTagWithPath(_ metadata: CGMutableImageMetadata, _ parent: CGImageMetadataTag?, _ path: CFString) -> Bool
```

#### Return Value

True if this function removed the tag, or false if it encountered a problem.

## Parameters

- `metadata`: The metadata object that contains the tag. If the tag doesn’t exist in this metadata object, this function creates a new tag.
- `parent`: The parent tag, if any. Specify `NULL` to add or update a tag starting at the top-level of the metadata object. If this parameter is `NULL`, you must include a valid prefix string in the `path` parameter. If you specify a value for this parameter, this function modifies the children its children, which might create different references for those children. To fix the references, commit this object back to the metadata object using this function. Pass the parent’s full path string; don’t specify the parent using a parent object and relative path.
- `path`: A string that represents the path to the tag. A path consists of the tag’s name, plus optional prefix and parent information. Separate prefix information from other path information using a colon (`:`) character. Separate parent and child tags using the period (`.`) character. For example, the string `“exif:Flash.RedEyeMode”` represents the path to the `RedEyeMode` field of the `Flash` parent structure in the EXIF metadata. When a tag contains an ordered or unordered array, specify elements using a `0`-based index inside square brackets. For example, use the string `“dc.subject[2]”` to access the third element in the `subject` array. When the tag contains an alternate-text array, access elements using an RFC 3066 language code inside square brackets. For example, use the string `“dc.description[de]”` to access the German description information. Use the ? character to delimit qualifiers for tags with string values. You may not use this character for arrays and structures.

## See Also

- [func CGImageMetadataSetValueWithPath(CGMutableImageMetadata, CGImageMetadataTag?, CFString, CFTypeRef) -> Bool](cgimagemetadatasetvaluewithpath(_:_:_:_:).md)
  Update the value of an existing metadata tag, or create a new tag using the specified information.
- [func CGImageMetadataSetValueMatchingImageProperty(CGMutableImageMetadata, CFString, CFString, CFTypeRef) -> Bool](cgimagemetadatasetvaluematchingimageproperty(_:_:_:_:).md)
  Updates the value of the metadata tag assigned to the specified image property.
- [func CGImageMetadataSetTagWithPath(CGMutableImageMetadata, CGImageMetadataTag?, CFString, CGImageMetadataTag) -> Bool](cgimagemetadatasettagwithpath(_:_:_:_:).md)
  Sets the tag at the specified path in the metadata object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagemetadataremovetagwithpath(_:_:_:))*
# CGImageMetadataSetTagWithPath(_:_:_:_:)

**Framework**: Image I/O  
**Kind**: func

Sets the tag at the specified path in the metadata object.

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
func CGImageMetadataSetTagWithPath(_ metadata: CGMutableImageMetadata, _ parent: CGImageMetadataTag?, _ path: CFString, _ tag: CGImageMetadataTag) -> Bool
```

#### Return Value

`true` if the function saved the tag successfully, or `false` if it encountered a problem.

## Parameters

- `metadata`: The metadata object that contains the tag. If the tag doesn’t exist in this metadata object, this function creates a new tag.
- `parent`: If you specify a value for this parameter, this function modifies the children its children, which might create different references for those children. To fix the references, commit this object back to the metadata object using this function. Pass the parent’s full path string; don’t specify the parent using a parent object and relative path.
- `path`: Use the ? character to delimit qualifiers for tags with string values. You may not use this character for arrays and structures.
- `tag`: The tag object to add to the metadata. This function retains the tag object.

## See Also

- [func CGImageMetadataSetValueWithPath(CGMutableImageMetadata, CGImageMetadataTag?, CFString, CFTypeRef) -> Bool](cgimagemetadatasetvaluewithpath(_:_:_:_:).md)
  Update the value of an existing metadata tag, or create a new tag using the specified information.
- [func CGImageMetadataSetValueMatchingImageProperty(CGMutableImageMetadata, CFString, CFString, CFTypeRef) -> Bool](cgimagemetadatasetvaluematchingimageproperty(_:_:_:_:).md)
  Updates the value of the metadata tag assigned to the specified image property.
- [func CGImageMetadataRemoveTagWithPath(CGMutableImageMetadata, CGImageMetadataTag?, CFString) -> Bool](cgimagemetadataremovetagwithpath(_:_:_:).md)
  Removes the tag at the specified path from the metadata object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagemetadatasettagwithpath(_:_:_:_:))*
# CMTagIsValid

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Whether the provided tag is valid.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```c
static Boolean CMTagIsValid(CMTag tag);
```

#### Return Value

Returns `YES` when a tag contains valid data for its [`category`](./cmtag-c.struct/category.md), [`dataType`](./cmtag-c.struct/datatype.md), and [`value`](./cmtag-c.struct/value.md).

## Parameters

- `tag`: The tag to check for validity.

## See Also

### Inspecting Tags
- [CMTagCopyDescription](./cmtagcopydescription.md)
  Copies the description of a tag to a new string.
- [CMTagGetCategory](./cmtaggetcategory.md)
  Retrieves the category of a tag.
- [CMTagGetValueDataType](./cmtaggetvaluedatatype.md)
  Retrieves the data type of a tag.
- [CMTagHasCategory](./cmtaghascategory.md)
  Checks if a tag contains a specific category.
- [CMTagHasFlagsValue](./cmtaghasflagsvalue.md)
  Whether a given tag contains a value for a 64-bit flag field.
- [CMTagHasFloat64Value](./cmtaghasfloat64value.md)
  Whether a given tag contains a value for a 64-bit floating point number.
- [CMTagHasOSTypeValue](./cmtaghasostypevalue.md)
  Whether a given tag contains a value for use by the operating system.
- [CMTagHasSInt64Value](./cmtaghassint64value.md)
  Whether a given tag contains a value for a signed 64-bit integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtagisvalid)*
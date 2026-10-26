# CMTagHasCategory

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Checks if a tag contains a specific category.

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
static Boolean CMTagHasCategory(CMTag tag, CMTagCategory category);
```

#### Return Value

Returns `YES` when the tag’s category and the category argument match.

#### Discussion

Prefer using this function over directly comparing a tag’s [`category`](./cmtag-c.struct/category.md) property to a value.

## Parameters

- `tag`: The tag to inspect the category of.
- `category`: The category to check the `tag` against.

## See Also

### Inspecting Tags
- [CMTagCopyDescription](./cmtagcopydescription.md)
  Copies the description of a tag to a new string.
- [CMTagIsValid](./cmtagisvalid.md)
  Whether the provided tag is valid.
- [CMTagGetCategory](./cmtaggetcategory.md)
  Retrieves the category of a tag.
- [CMTagGetValueDataType](./cmtaggetvaluedatatype.md)
  Retrieves the data type of a tag.
- [CMTagHasFlagsValue](./cmtaghasflagsvalue.md)
  Whether a given tag contains a value for a 64-bit flag field.
- [CMTagHasFloat64Value](./cmtaghasfloat64value.md)
  Whether a given tag contains a value for a 64-bit floating point number.
- [CMTagHasOSTypeValue](./cmtaghasostypevalue.md)
  Whether a given tag contains a value for use by the operating system.
- [CMTagHasSInt64Value](./cmtaghassint64value.md)
  Whether a given tag contains a value for a signed 64-bit integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtaghascategory)*
# CMTagHasSInt64Value

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Whether a given tag contains a value for a signed 64-bit integer.

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
extern Boolean CMTagHasSInt64Value(CMTag tag);
```

#### Return Value

Returns `YES` if the tag represents an integer.

#### Discussion

Prefer using this method over directly comparing a tag’s data type to [`kCMTagDataType_SInt64`](./cmtagdatatype/kcmtagdatatype_sint64.md).

## Parameters

- `tag`: The tag to inspect.

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
- [CMTagHasCategory](./cmtaghascategory.md)
  Checks if a tag contains a specific category.
- [CMTagHasFlagsValue](./cmtaghasflagsvalue.md)
  Whether a given tag contains a value for a 64-bit flag field.
- [CMTagHasFloat64Value](./cmtaghasfloat64value.md)
  Whether a given tag contains a value for a 64-bit floating point number.
- [CMTagHasOSTypeValue](./cmtaghasostypevalue.md)
  Whether a given tag contains a value for use by the operating system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtaghassint64value)*
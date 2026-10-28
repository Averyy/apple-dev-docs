# CMTagHasOSTypeValue

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Whether a given tag contains a value for use by the operating system.

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
extern Boolean CMTagHasOSTypeValue(CMTag tag);
```

## Return Value

Returns `YES` if the tag represents an [`OSType`](../kernel/ostype.md).

## Discussion

Prefer using this method over directly comparing a tag’s data type to [`kCMTagDataType_OSType`](./cmtagdatatype/kcmtagdatatype_ostype.md).

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
- [CMTagHasSInt64Value](./cmtaghassint64value.md)
  Whether a given tag contains a value for a signed 64-bit integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtaghasostypevalue)*
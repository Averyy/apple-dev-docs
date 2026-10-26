# CMTagCopyAsDictionary

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Copies an existing tag to a new dictionary object.

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
extern CFDictionaryRefCMTagCopyAsDictionary(CMTag tag, CFAllocatorRef allocator);
```

#### Return Value

A reference to a new [`CFDictionary`](../CoreFoundation/cfdictionary.md), or `NULL` if no dictionary could be created.

#### Discussion

The created dictionary contains values for the keys [`kCMTagCategoryKey`](./kcmtagcategorykey.md), [`kCMTagDataTypeKey`](./kcmtagdatatypekey.md), and [`kCMTagValueKey`](./kcmtagvaluekey.md).

## Parameters

- `tag`: The tag to create a new dictionary from.
- `allocator`: The allocator to use for creating a new dictionary. Pass `kCFAllocatorDefault` to use the default global allocator.

## See Also

### Retrieving Tag Values
- [CMTagGetFlagsValue](./cmtaggetflagsvalue.md)
  Retrieves a tag’s value as a 64-bit field flag.
- [CMTagGetFloat64Value](./cmtaggetfloat64value.md)
  Retrieves a tag’s value as a 64-bit floating point number.
- [CMTagGetOSTypeValue](./cmtaggetostypevalue.md)
  Retrieves a tag’s value for use by the operating system.
- [CMTagGetSInt64Value](./cmtaggetsint64value.md)
  Retrieves a tag’s value as a signed 64-bit integer.
- [CMTagGetValue](./cmtaggetvalue.md)
  Retrieves a tag’s value as an uninterpreted 64-bit wide unsigned integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtagcopyasdictionary)*
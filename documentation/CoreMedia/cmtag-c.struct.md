# CMTag

**Framework**: Core Media  
**Kind**: struct  
**Role**: Structure

A tag representing additional metadata on tagged media buffers.

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
struct CMTag;
```

## Overview

The Core Media framework uses tags to describe the properties of media channels. Each tag consists of a category and a value, both of which are 64 bits in size.

> ❗ **Important**: Tag data can only contain values that can be safely stored on disk. This restriction means `CMTag` structs can’t contain a pointer as their value. If you need to refer to another media element or in-memory data as part of a tag, use a buffer index or other constant.

## Topics

### Tag Data
- [category](./cmtag-c.struct/category.md)
  The category assigned to a tag.
- [dataType](./cmtag-c.struct/datatype.md)
  The data type for the value stored in the tag.
- [value](./cmtag-c.struct/value.md)
  The value of the tag.

## See Also

### Types
- [CMTagValue](./cmtagvalue.md)
  The type used to represent tag values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtag-c.struct)*
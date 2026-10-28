# CMTagDataType

**Framework**: Core Media  
**Kind**: enum  
**Role**: Enumeration

The data type of a tag’s value.

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
enum CMTagDataType : uint32_t;
```

## Overview

Use methods from Inspecting Tags to determine a tag’s data type.

## Topics

### Tag Value Types
- [kCMTagDataType_SInt64](./cmtagdatatype/kcmtagdatatype_sint64.md)
  The tag value is a signed 64-bit integer.
- [kCMTagDataType_Float64](./cmtagdatatype/kcmtagdatatype_float64.md)
  The tag value is a 64-bit floating point number.
- [kCMTagDataType_Flags](./cmtagdatatype/kcmtagdatatype_flags.md)
  The tag value is a 64-bit wide bitflag field.
- [kCMTagDataType_OSType](./cmtagdatatype/kcmtagdatatype_ostype.md)
  The tag value is a 64-bit identifier used by the operating system.
- [kCMTagDataType_Invalid](./cmtagdatatype/kcmtagdatatype_invalid.md)
  The tag value isn’t associated with any known data type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtagdatatype)*
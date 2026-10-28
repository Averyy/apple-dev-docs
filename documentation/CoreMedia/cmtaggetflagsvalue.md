# CMTagGetFlagsValue

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Retrieves a tag’s value as a 64-bit field flag.

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
extern uint64_t CMTagGetFlagsValue(CMTag tag);
```

## Discussion

> **Note**:  Before retrieving a tag’s value with this function, call [`CMTagHasFlagsValue`](./cmtaghasflagsvalue.md) to ensure it has the correct type.

## Parameters

- `tag`: The tag to get the value from.

## See Also

### Retrieving Tag Values
- [CMTagCopyAsDictionary](./cmtagcopyasdictionary.md)
  Copies an existing tag to a new dictionary object.
- [CMTagGetFloat64Value](./cmtaggetfloat64value.md)
  Retrieves a tag’s value as a 64-bit floating point number.
- [CMTagGetOSTypeValue](./cmtaggetostypevalue.md)
  Retrieves a tag’s value for use by the operating system.
- [CMTagGetSInt64Value](./cmtaggetsint64value.md)
  Retrieves a tag’s value as a signed 64-bit integer.
- [CMTagGetValue](./cmtaggetvalue.md)
  Retrieves a tag’s value as an uninterpreted 64-bit wide unsigned integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtaggetflagsvalue)*
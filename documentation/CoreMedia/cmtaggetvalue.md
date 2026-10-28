# CMTagGetValue

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Retrieves a tag’s value as an uninterpreted 64-bit wide unsigned integer.

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
static CMTagValue CMTagGetValue(CMTag tag);
```

## Discussion

Prefer using another method from Retrieving Tag Values that automatically interprets a tag to calling this method and performing your own typecast.

## Parameters

- `tag`: The tag to retrieve the value of.

## See Also

### Retrieving Tag Values
- [CMTagCopyAsDictionary](./cmtagcopyasdictionary.md)
  Copies an existing tag to a new dictionary object.
- [CMTagGetFlagsValue](./cmtaggetflagsvalue.md)
  Retrieves a tag’s value as a 64-bit field flag.
- [CMTagGetFloat64Value](./cmtaggetfloat64value.md)
  Retrieves a tag’s value as a 64-bit floating point number.
- [CMTagGetOSTypeValue](./cmtaggetostypevalue.md)
  Retrieves a tag’s value for use by the operating system.
- [CMTagGetSInt64Value](./cmtaggetsint64value.md)
  Retrieves a tag’s value as a signed 64-bit integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtaggetvalue)*
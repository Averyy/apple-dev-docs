# CMTagMakeWithFlagsValue

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Creates a new tag with a given category and a value interpreted as a 64-bit flag field.

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
extern CMTag CMTagMakeWithFlagsValue(CMTagCategory category, uint64_t flagsForTag);
```

## Return Value

A new tag with the assigned category containing flags as its value, or [`kCMTagInvalid`](./kcmtaginvalid.md) if no tag could be created.

## Parameters

- `category`: The category of the new tag. For available categories, see Tag Category Constants.
- `flagsForTag`: The bitfield to set as the new tag’s value.

## See Also

### Creating Tags
- [CMTagMakeFromDictionary](./cmtagmakefromdictionary.md)
  Create a new tag from a dictionary object.
- [CMTagMakeWithFloat64Value](./cmtagmakewithfloat64value.md)
  Creates a new tag with a given category and a 64-bit floating point value.
- [CMTagMakeWithOSTypeValue](./cmtagmakewithostypevalue.md)
  Creates a new tag with a given category and a 64-bit value for use by the framework.
- [CMTagMakeWithSInt64Value](./cmtagmakewithsint64value.md)
  Creates a new tag with a given category and a 64-bit signed integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtagmakewithflagsvalue)*
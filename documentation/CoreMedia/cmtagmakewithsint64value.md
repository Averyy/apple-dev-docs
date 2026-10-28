# CMTagMakeWithSInt64Value

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Creates a new tag with a given category and a 64-bit signed integer.

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
extern CMTag CMTagMakeWithSInt64Value(CMTagCategory category, int64_t value);
```

## Return Value

A new tag with the assigned category containing a signed 64-bit integer, or [`kCMTagInvalid`](./kcmtaginvalid.md) if no tag could be created.

## Parameters

- `category`: The category of the new tag. For available categories, see Tag Category Constants.
- `value`: The value of the new tag.

## See Also

### Creating Tags
- [CMTagMakeFromDictionary](./cmtagmakefromdictionary.md)
  Create a new tag from a dictionary object.
- [CMTagMakeWithFlagsValue](./cmtagmakewithflagsvalue.md)
  Creates a new tag with a given category and a value interpreted as a 64-bit flag field.
- [CMTagMakeWithFloat64Value](./cmtagmakewithfloat64value.md)
  Creates a new tag with a given category and a 64-bit floating point value.
- [CMTagMakeWithOSTypeValue](./cmtagmakewithostypevalue.md)
  Creates a new tag with a given category and a 64-bit value for use by the framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtagmakewithsint64value)*
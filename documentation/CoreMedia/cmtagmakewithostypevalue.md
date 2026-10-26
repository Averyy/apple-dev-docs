# CMTagMakeWithOSTypeValue

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Creates a new tag with a given category and a 64-bit value for use by the framework.

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
extern CMTag CMTagMakeWithOSTypeValue(CMTagCategory category, OSType value);
```

#### Return Value

A new tag with the assigned category containing an [`OSType`](../kernel/ostype.md), or [`kCMTagInvalid`](./kcmtaginvalid.md) if no tag could be created.

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
- [CMTagMakeWithSInt64Value](./cmtagmakewithsint64value.md)
  Creates a new tag with a given category and a 64-bit signed integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtagmakewithostypevalue)*
# value(for:)

**Framework**: Core Media  
**Kind**: method

Convert a tag value into a typed value valid for this category, if possible.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func value(for tagValue: CMTag.Value) -> TypedValue?
```

#### Return Value

A value of type `TypedValue` containing the tag value, or `nil` if the tag value couldn’t be converted to a `TypedValue`.

## Parameters

- `tagValue`: The tag value to convert to a typed value.

## See Also

- [func tagValue(for: TypedValue) -> CMTag.Value](cmtypedtag/category-swift.struct/tagvalue(for:).md)
  Convert a typed value to a raw tag value for this category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtypedtag/category-swift.struct/value(for:))*
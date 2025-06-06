# tagValue(for:)

**Framework**: Core Media  
**Kind**: method

Convert a typed value to a raw tag value for this category.

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
func tagValue(for value: TypedValue) -> CMTag.Value
```

#### Return Value

The typed value as a wrapped tag value.

## Parameters

- `value`: The value to convert to a tag value.

## See Also

- [func value(for: CMTag.Value) -> TypedValue?](cmtypedtag/category-swift.struct/value(for:).md)
  Convert a tag value into a typed value valid for this category, if possible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtypedtag/category-swift.struct/tagvalue(for:))*
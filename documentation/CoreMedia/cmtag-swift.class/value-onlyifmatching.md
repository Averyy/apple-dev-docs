# value(onlyIfMatching:)

**Framework**: Core Media  
**Kind**: method

Retrieves a tag’s value as a specific type, if and only if it matches a category.

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
func value<T>(onlyIfMatching category: CMTypedTag<T>.Category) -> T? where T : Sendable
```

#### Return Value

The value contained in the tag as an instance of type `T` if the category matches. Otherwise, returns `nil`.

## Parameters

- `category`: The category to check if the tag contains.

## See Also

- [let rawCategory: CMTag.RawCategory](cmtag-swift.class/rawcategory-swift.property.md)
  The raw 64-bit representation of the tag’s category.
- [let rawTagValue: CMTag.Value](cmtag-swift.class/rawtagvalue.md)
  The tag’s contained value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtag-swift.class/value(onlyifmatching:))*
# insert(_:at:)

**Framework**: Foundation  
**Kind**: method

Inserts the specified string at a specific index in the attributed string.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
mutating func insert(_ s: some AttributedStringProtocol, at index: AttributedString.Index)
```

## Parameters

- `s`: The string to insert.
- `index`: The index that indicates where to insert the string.

## See Also

- [AttributedString.Index](attributedstring/index.md)
  A type that represents the position of a character or code unit within an attributed string.
- [func removeSubrange(some RangeExpression<AttributedString.Index>)](attributedstring/removesubrange(_:).md)
  Removes a range of characters from the attributed string.
- [func replaceSubrange(some RangeExpression<AttributedString.Index>, with: some AttributedStringProtocol)](attributedstring/replacesubrange(_:with:).md)
  Replaces the contents in a range of the attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/insert(_:at:))*
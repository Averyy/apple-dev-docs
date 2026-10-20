# removeSubrange(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Removes a range of characters from the attributed string.

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
mutating func removeSubrange(_ range: some RangeExpression<AttributedString.Index>)
```

## Parameters

- `range`: The range to remove.

## See Also

### Modifying an Attributed String
- [func insert(some AttributedStringProtocol, at: AttributedString.Index)](./insert%28_,at%29.md)
  Inserts the specified string at a specific index in the attributed string.
- [AttributedString.Index](./index.md)
  A type that represents the position of a character or code unit within an attributed string.
- [func replaceSubrange(some RangeExpression<AttributedString.Index>, with: some AttributedStringProtocol)](./replacesubrange%28_,with%29.md)
  Replaces the contents in a range of the attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/removesubrange(_:))*
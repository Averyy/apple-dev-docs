# advanced(by:)

**Framework**: Foundation  
**Kind**: method

Returns a new data buffer created by removing the given number of bytes from the front of the original buffer.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func advanced(by amount: Int) -> Data
```

#### Return Value

A newly created data buffer that is shorter by the given amount than the original.

## Parameters

- `amount`: The number of bytes to strip from the input data buffer. The value must be less than the original data buffer’s length.

## See Also

- [func dropLast(Int) -> Self.SubSequence](data/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func dropFirst(Int) -> Self.SubSequence](data/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](data/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/advanced(by:))*
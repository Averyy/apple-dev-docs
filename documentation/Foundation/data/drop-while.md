# drop(while:)

**Framework**: Foundation  
**Kind**: method

Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func drop(while predicate: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence
```

#### Discussion

> **Note**: O(), where  is the length of the collection.

## Parameters

- `predicate`: A closure that takes an element of the   sequence as its argument and returns   if the element should   be skipped or   if it should be included. Once the predicate   returns   it will not be called again.

## See Also

- [func dropLast(Int) -> Self.SubSequence](data/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func dropFirst(Int) -> Self.SubSequence](data/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func advanced(by: Int) -> Data](data/advanced(by:).md)
  Returns a new data buffer created by removing the given number of bytes from the front of the original buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/drop(while:))*
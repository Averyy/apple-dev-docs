# prefix(while:)

**Framework**: Foundation  
**Kind**: method

Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.

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
func prefix(while predicate: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence
```

#### Discussion

> **Note**: O(), where  is the length of the collection.

O(), where  is the length of the collection.

## Parameters

- `predicate`: A closure that takes an element of the   sequence as its argument and returns   if the element should   be included or   if it should be excluded. Once the predicate   returns   it will not be called again.

## See Also

- [func filter((Self.Element) throws -> Bool) rethrows -> Self](data/filter(_:).md)
  Returns a new collection of the same type containing, in order, the elements of the original collection that satisfy the given predicate.
- [func prefix(Int) -> Self.SubSequence](data/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](data/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](data/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func suffix(Int) -> Self.SubSequence](data/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
- [func suffix(from: Self.Index) -> Self.SubSequence](data/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/prefix(while:))*
# prefix(while:)

**Framework**: TabularData  
**Kind**: method

Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.

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
func prefix(while predicate: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence
```

#### Discussion

> **Note**: O(), where  is the length of the collection.

## Parameters

- `predicate`: A closure that takes an element of the   sequence as its argument and returns   if the element should   be included or   if it should be excluded. Once the predicate   returns   it will not be called again.

## See Also

- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](column/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropFirst(Int) -> Self.SubSequence](column/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func prefix(Int) -> Self.SubSequence](column/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](column/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(through: Self.Index) -> Self.SubSequence](column/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func suffix(Int) -> Self.SubSequence](column/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
- [func suffix(from: Self.Index) -> Self.SubSequence](column/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](column/subscript(_:)-2eycv.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/column/prefix(while:))*
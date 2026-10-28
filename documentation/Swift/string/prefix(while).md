# prefix(while:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func prefix(while predicate: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence
```

## Discussion

> **Complexity**: O(*n*), where *n* is the length of the collection.

## Parameters

- `predicate`: A closure that takes an element of the sequence as its argument and returns `true` if the element should be included or `false` if it should be excluded. Once the predicate returns `false` it will not be called again.

## See Also

### Getting Substrings
- [subscript(Range<String.Index>) -> Substring](./subscript%28_%29-2so14.md)
  Accesses a contiguous subrange of the collection’s elements.
- [subscript<R>(R) -> Self.SubSequence](./subscript%28_%29-4h7s3.md)
  Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript(UnboundedRange) -> Self.SubSequence](./subscript%28_%29-4al9c.md)
- [func prefix(Int) -> Self.SubSequence](./prefix%28_%29.md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](./prefix%28through%29.md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](./prefix%28upto%29.md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func suffix(Int) -> Self.SubSequence](./suffix%28_%29.md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
- [func suffix(from: Self.Index) -> Self.SubSequence](./suffix%28from%29.md)
  Returns a subsequence from the specified position to the end of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/prefix(while:))*
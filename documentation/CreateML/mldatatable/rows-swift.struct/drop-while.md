# drop(while:)

**Framework**: Create ML  
**Kind**: method

Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func drop(while predicate: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence
```

#### Discussion

> **Note**: O(), where  is the length of the collection.

## Parameters

- `predicate`: A closure that takes an element of the   sequence as its argument and returns   if the element should   be skipped or   if it should be included. Once the predicate   returns   it will not be called again.

## See Also

- [func dropFirst(Int) -> Self.SubSequence](mldatatable/rows-swift.struct/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func dropLast(Int) -> Self.SubSequence](mldatatable/rows-swift.struct/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/rows-swift.struct/drop(while:))*
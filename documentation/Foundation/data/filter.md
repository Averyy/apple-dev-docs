# filter(_:)

**Framework**: Foundation  
**Kind**: method

Returns a new collection of the same type containing, in order, the elements of the original collection that satisfy the given predicate.

**Availability**:
- Mac Catalyst 13.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+
- Swift 4.0+
- Swift 4.0+

## Declaration

```swift
func filter(_ isIncluded: (Self.Element) throws -> Bool) rethrows -> Self
```

#### Return Value

A collection of the elements that `isIncluded` allowed.

#### Discussion

In this example, `filter(_:)` is used to include only names shorter than five characters.

```None
let cast = ["Vivien", "Marlon", "Kim", "Karl"]
let shortNames = cast.filter { $0.count < 5 }
print(shortNames)
// Prints "["Kim", "Karl"]"
```

> **Note**: O(), where  is the length of the collection.

## Parameters

- `isIncluded`: A closure that takes an element of the   sequence as its argument and returns a Boolean value indicating   whether the element should be included in the returned collection.

## See Also

- [func prefix(Int) -> Self.SubSequence](data/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](data/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](data/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](data/prefix(while:).md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func suffix(Int) -> Self.SubSequence](data/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
- [func suffix(from: Self.Index) -> Self.SubSequence](data/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/filter(_:))*
# suffix(_:)

**Framework**: Realitykit  
**Kind**: method

Returns a subsequence, up to the given maximum length, containing the final elements of the collection.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
func suffix(_ maxLength: Int) -> Self.SubSequence
```

#### Return Value

A subsequence terminating at the end of the collection with at most `maxLength` elements.

#### Discussion

If the maximum length exceeds the number of elements in the collection, the result contains all the elements in the collection.

```None
let numbers = [1, 2, 3, 4, 5]
print(numbers.suffix(2))
// Prints "[4, 5]"
print(numbers.suffix(10))
// Prints "[1, 2, 3, 4, 5]"
```

> **Note**: O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the length of the collection.

## Parameters

- `maxLength`: The maximum number of elements to return. The   value of   must be greater than or equal to zero.

## See Also

- [func filter(Predicate<Self.Element>) throws -> [Self.Element]](scene/anchorcollection/filter(_:)-4j9lz.md)
- [func filter((Self.Element) throws -> Bool) rethrows -> [Self.Element]](scene/anchorcollection/filter(_:)-9loo9.md)
  Returns an array containing, in order, the elements of the sequence that satisfy the given predicate.
- [func prefix(Int) -> Self.SubSequence](scene/anchorcollection/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](scene/anchorcollection/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](scene/anchorcollection/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](scene/anchorcollection/prefix(while:).md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func suffix(from: Self.Index) -> Self.SubSequence](scene/anchorcollection/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
- [func randomElement() -> Self.Element?](scene/anchorcollection/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](scene/anchorcollection/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/anchorcollection/suffix(_:))*
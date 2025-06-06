# prefix(while:)

**Framework**: RealityKit  
**Kind**: method

Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

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

- [func filter(Predicate<Self.Element>) throws -> [Self.Element]](scene/anchorcollection/filter(_:)-4j9lz.md)
- [func filter((Self.Element) throws -> Bool) rethrows -> [Self.Element]](scene/anchorcollection/filter(_:)-9loo9.md)
  Returns an array containing, in order, the elements of the sequence that satisfy the given predicate.
- [func prefix(Int) -> Self.SubSequence](scene/anchorcollection/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](scene/anchorcollection/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](scene/anchorcollection/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func suffix(Int) -> Self.SubSequence](scene/anchorcollection/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
- [func suffix(from: Self.Index) -> Self.SubSequence](scene/anchorcollection/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
- [func randomElement() -> Self.Element?](scene/anchorcollection/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](scene/anchorcollection/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/anchorcollection/prefix(while:))*
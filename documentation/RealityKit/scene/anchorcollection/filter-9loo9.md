# filter(_:)

**Framework**: RealityKit  
**Kind**: method

Returns an array containing, in order, the elements of the sequence that satisfy the given predicate.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
func filter(_ isIncluded: (Self.Element) throws -> Bool) rethrows -> [Self.Element]
```

#### Return Value

An array of the elements that `isIncluded` allowed.

#### Discussion

In this example, `filter(_:)` is used to include only names shorter than five characters.

```None
let cast = ["Vivien", "Marlon", "Kim", "Karl"]
let shortNames = cast.filter { $0.count < 5 }
print(shortNames)
// Prints "["Kim", "Karl"]"
```

> **Note**: O(), where  is the length of the sequence.

O(), where  is the length of the sequence.

## Parameters

- `isIncluded`: A closure that takes an element of the   sequence as its argument and returns a Boolean value indicating   whether the element should be included in the returned array.

## See Also

- [func filter(Predicate<Self.Element>) throws -> [Self.Element]](scene/anchorcollection/filter(_:)-4j9lz.md)
- [func prefix(Int) -> Self.SubSequence](scene/anchorcollection/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](scene/anchorcollection/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](scene/anchorcollection/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](scene/anchorcollection/prefix(while:).md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func suffix(Int) -> Self.SubSequence](scene/anchorcollection/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
- [func suffix(from: Self.Index) -> Self.SubSequence](scene/anchorcollection/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
- [func randomElement() -> Self.Element?](scene/anchorcollection/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](scene/anchorcollection/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/anchorcollection/filter(_:)-9loo9)*
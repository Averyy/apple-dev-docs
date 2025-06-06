# contains(_:)

**Framework**: RealityKit  
**Kind**: method

Returns a Boolean value indicating whether the sequence contains the given element.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
func contains(_ element: Self.Element) -> Bool
```

#### Return Value

`true` if the element was found in the sequence; otherwise, `false`.

#### Discussion

This example checks to see whether a favorite actor is in an array storing a movie’s cast.

```None
let cast = ["Vivien", "Marlon", "Kim", "Karl"]
print(cast.contains("Marlon"))
// Prints "true"
print(cast.contains("James"))
// Prints "false"
```

> **Note**: O(), where  is the length of the sequence.

O(), where  is the length of the sequence.

## Parameters

- `element`: The element to find in the sequence.

## See Also

- [func contains(where: (Self.Element) throws -> Bool) rethrows -> Bool](entity/childcollection/contains(where:).md)
  Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [func allSatisfy((Self.Element) throws -> Bool) rethrows -> Bool](entity/childcollection/allsatisfy(_:).md)
  Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [var first: Self.Element?](entity/childcollection/first.md)
  The first element of the collection.
- [func first(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](entity/childcollection/first(where:).md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func max(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](entity/childcollection/max(by:).md)
  Returns the maximum element in the sequence, using the given predicate as the comparison between elements.
- [func min(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](entity/childcollection/min(by:).md)
  Returns the minimum element in the sequence, using the given predicate as the comparison between elements.
- [func randomElement() -> Self.Element?](entity/childcollection/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](entity/childcollection/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/childcollection/contains(_:))*
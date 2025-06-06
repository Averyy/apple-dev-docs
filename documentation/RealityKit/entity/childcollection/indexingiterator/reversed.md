# reversed()

**Framework**: RealityKit  
**Kind**: method

Returns an array containing the elements of this sequence in reverse order.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
func reversed() -> [Self.Element]
```

#### Return Value

An array containing the elements of this sequence in reverse order.

#### Discussion

The sequence must be finite.

> **Note**: O(), where  is the length of the sequence.

O(), where  is the length of the sequence.

## See Also

- [func sorted() -> [Self.Element]](entity/childcollection/indexingiterator/sorted.md)
  Returns the elements of the sequence, sorted.
- [func sorted(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> [Self.Element]](entity/childcollection/indexingiterator/sorted(by:).md)
  Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [func shuffled() -> [Self.Element]](entity/childcollection/indexingiterator/shuffled.md)
  Returns the elements of the sequence, shuffled.
- [func shuffled<T>(using: inout T) -> [Self.Element]](entity/childcollection/indexingiterator/shuffled(using:).md)
  Returns the elements of the sequence, shuffled using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/childcollection/indexingiterator/reversed())*
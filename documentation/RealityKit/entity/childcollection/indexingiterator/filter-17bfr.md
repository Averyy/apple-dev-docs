# filter(_:)

**Framework**: RealityKit  
**Kind**: method

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
func filter(_ predicate: Predicate<Self.Element>) throws -> [Self.Element]
```

## See Also

- [func filter((Self.Element) throws -> Bool) rethrows -> [Self.Element]](entity/childcollection/indexingiterator/filter(_:)-3ihv7.md)
  Returns an array containing, in order, the elements of the sequence that satisfy the given predicate.
- [func prefix(Int) -> PrefixSequence<Self>](entity/childcollection/indexingiterator/prefix(_:).md)
  Returns a sequence, up to the specified maximum length, containing the initial elements of the sequence.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> [Self.Element]](entity/childcollection/indexingiterator/prefix(while:).md)
  Returns a sequence containing the initial, consecutive elements that satisfy the given predicate.
- [func suffix(Int) -> [Self.Element]](entity/childcollection/indexingiterator/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/childcollection/indexingiterator/filter(_:)-17bfr)*
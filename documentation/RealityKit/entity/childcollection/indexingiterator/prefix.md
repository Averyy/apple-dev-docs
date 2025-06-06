# prefix(_:)

**Framework**: Realitykit  
**Kind**: method

Returns a sequence, up to the specified maximum length, containing the initial elements of the sequence.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
func prefix(_ maxLength: Int) -> PrefixSequence<Self>
```

#### Return Value

A sequence starting at the beginning of this sequence with at most `maxLength` elements.

#### Discussion

If the maximum length exceeds the number of elements in the sequence, the result contains all the elements in the sequence.

```None
let numbers = [1, 2, 3, 4, 5]
print(numbers.prefix(2))
// Prints "[1, 2]"
print(numbers.prefix(10))
// Prints "[1, 2, 3, 4, 5]"
```

> **Note**: O(1)

## Parameters

- `maxLength`: The maximum number of elements to return. The   value of   must be greater than or equal to zero.

## See Also

- [func filter(Predicate<Self.Element>) throws -> [Self.Element]](entity/childcollection/indexingiterator/filter(_:)-17bfr.md)
- [func filter((Self.Element) throws -> Bool) rethrows -> [Self.Element]](entity/childcollection/indexingiterator/filter(_:)-3ihv7.md)
  Returns an array containing, in order, the elements of the sequence that satisfy the given predicate.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> [Self.Element]](entity/childcollection/indexingiterator/prefix(while:).md)
  Returns a sequence containing the initial, consecutive elements that satisfy the given predicate.
- [func suffix(Int) -> [Self.Element]](entity/childcollection/indexingiterator/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/childcollection/indexingiterator/prefix(_:))*
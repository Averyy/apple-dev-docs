# filter(_:)

**Framework**: Realitykit  
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

## Parameters

- `isIncluded`: A closure that takes an element of the   sequence as its argument and returns a Boolean value indicating   whether the element should be included in the returned array.

## See Also

- [func filter(Predicate<Self.Element>) throws -> [Self.Element]](entity/childcollection/indexingiterator/filter(_:)-17bfr.md)
- [func prefix(Int) -> PrefixSequence<Self>](entity/childcollection/indexingiterator/prefix(_:).md)
  Returns a sequence, up to the specified maximum length, containing the initial elements of the sequence.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> [Self.Element]](entity/childcollection/indexingiterator/prefix(while:).md)
  Returns a sequence containing the initial, consecutive elements that satisfy the given predicate.
- [func suffix(Int) -> [Self.Element]](entity/childcollection/indexingiterator/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/childcollection/indexingiterator/filter(_:)-3ihv7)*
# joined(separator:)

**Framework**: RealityKit  
**Kind**: method

Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
func joined(separator: String = "") -> String
```

#### Return Value

A single, concatenated string.

#### Discussion

The following example shows how an array of strings can be joined to a single, comma-separated string:

```None
let cast = ["Vivien", "Marlon", "Kim", "Karl"]
let list = cast.joined(separator: ", ")
print(list)
// Prints "Vivien, Marlon, Kim, Karl"
```

## Parameters

- `separator`: A string to insert between each of the elements   in this sequence. The default separator is an empty string.

## See Also

- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [ArraySlice<Self.Element>]](entity/childcollection/indexingiterator/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the sequence, in order, that don’t contain elements satisfying the given predicate. Elements that are used to split the sequence are not returned as part of any subsequence.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [ArraySlice<Self.Element>]](entity/childcollection/indexingiterator/split(separator:maxsplits:omittingemptysubsequences:).md)
  Returns the longest possible subsequences of the sequence, in order, around elements equal to the given element.
- [func joined() -> FlattenSequence<Self>](entity/childcollection/indexingiterator/joined.md)
  Returns the elements of this sequence of sequences, concatenated.
- [func joined<Separator>(separator: Separator) -> JoinedSequence<Self>](entity/childcollection/indexingiterator/joined(separator:)-8q64h.md)
  Returns the concatenated elements of this sequence of sequences, inserting the given separator between each element.
- [Entity.ChildCollection.IndexingIterator.SubSequence](entity/childcollection/indexingiterator/subsequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/childcollection/indexingiterator/joined(separator:)-35cxx)*
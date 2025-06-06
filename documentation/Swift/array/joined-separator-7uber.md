# joined(separator:)

**Framework**: Swift  
**Kind**: method

Returns the concatenated elements of this sequence of sequences, inserting the given separator between each element.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func joined<Separator>(separator: Separator) -> JoinedSequence<Self> where Separator : Sequence, Separator.Element == Self.Element.Element
```

#### Return Value

The joined sequence of elements.

#### Discussion

This example shows how an array of `[Int]` instances can be joined, using another `[Int]` instance as the separator:

```swift
let nestedNumbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
let joined = nestedNumbers.joined(separator: [-1, -2])
print(Array(joined))
// Prints "[1, 2, 3, -1, -2, 4, 5, 6, -1, -2, 7, 8, 9]"
```

## Parameters

- `separator`: A sequence to insert between each of this   sequence’s elements.

## See Also

- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](array/split(separator:maxsplits:omittingemptysubsequences:)-3dgmv.md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](array/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
- [func joined() -> FlattenSequence<Self>](array/joined.md)
  Returns the elements of this sequence of sequences, concatenated.
- [func joined(separator: String) -> String](array/joined(separator:)-5do1g.md)
  Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.
- [func joined(separator: String) -> String](array/joined(separator:)-1ckod.md)
  Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/joined(separator:)-7uber)*
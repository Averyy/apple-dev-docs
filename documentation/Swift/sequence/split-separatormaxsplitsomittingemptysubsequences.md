# split(separator:maxSplits:omittingEmptySubsequences:)

**Framework**: Swift  
**Kind**: method

Returns the longest possible subsequences of the sequence, in order, around elements equal to the given element.

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
func split(separator: Self.Element, maxSplits: Int = Int.max, omittingEmptySubsequences: Bool = true) -> [ArraySlice<Self.Element>]
```

#### Return Value

An array of subsequences, split from this sequence’s elements.

#### Discussion

The resulting array consists of at most `maxSplits + 1` subsequences. Elements that are used to split the sequence are not returned as part of any subsequence.

The following examples show the effects of the `maxSplits` and `omittingEmptySubsequences` parameters when splitting a string at each space character (” “). The first use of `split` returns each word that was originally separated by one or more spaces.

```swift
let line = "BLANCHE:   I don't want realism. I want magic!"
print(line.split(separator: " ")
          .map(String.init))
// Prints "["BLANCHE:", "I", "don\'t", "want", "realism.", "I", "want", "magic!"]"
```

The second example passes `1` for the `maxSplits` parameter, so the original string is split just once, into two new strings.

```swift
print(line.split(separator: " ", maxSplits: 1)
          .map(String.init))
// Prints "["BLANCHE:", "  I don\'t want realism. I want magic!"]"
```

The final example passes `false` for the `omittingEmptySubsequences` parameter, so the returned array contains empty strings where spaces were repeated.

```swift
print(line.split(separator: " ", omittingEmptySubsequences: false)
          .map(String.init))
// Prints "["BLANCHE:", "", "", "I", "don\'t", "want", "realism.", "I", "want", "magic!"]"
```

> **Note**: O(), where  is the length of the sequence.

## Parameters

- `separator`: The element that should be split upon.
- `maxSplits`: The maximum number of times to split the sequence, or one   less than the number of subsequences to return. If    subsequences are returned, the last one is a suffix of the original   sequence containing the remaining elements.   must be   greater than or equal to zero. The default value is  .
- `omittingEmptySubsequences`: If  , an empty subsequence is   returned in the result for each consecutive pair of    elements in the sequence and for each instance of   at the   start or end of the sequence. If  , only nonempty subsequences   are returned. The default value is  .

## See Also

- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [ArraySlice<Self.Element>]](sequence/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the sequence, in order, that don’t contain elements satisfying the given predicate. Elements that are used to split the sequence are not returned as part of any subsequence.
- [func joined() -> FlattenSequence<Self>](sequence/joined.md)
  Returns the elements of this sequence of sequences, concatenated.
- [func joined(separator: String) -> String](sequence/joined(separator:)-5zjyj.md)
  Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.
- [func joined<Separator>(separator: Separator) -> JoinedSequence<Self>](sequence/joined(separator:)-7w47r.md)
  Returns the concatenated elements of this sequence of sequences, inserting the given separator between each element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/sequence/split(separator:maxsplits:omittingemptysubsequences:))*
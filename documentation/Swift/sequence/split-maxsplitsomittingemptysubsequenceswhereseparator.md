# split(maxSplits:omittingEmptySubsequences:whereSeparator:)

**Framework**: Swift  
**Kind**: method

Returns the longest possible subsequences of the sequence, in order, that don’t contain elements satisfying the given predicate. Elements that are used to split the sequence are not returned as part of any subsequence.

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
func split(maxSplits: Int = Int.max, omittingEmptySubsequences: Bool = true, whereSeparator isSeparator: (Self.Element) throws -> Bool) rethrows -> [ArraySlice<Self.Element>]
```

#### Return Value

An array of subsequences, split from this sequence’s elements.

#### Discussion

The following examples show the effects of the `maxSplits` and `omittingEmptySubsequences` parameters when splitting a string using a closure that matches spaces. The first use of `split` returns each word that was originally separated by one or more spaces.

```swift
let line = "BLANCHE:   I don't want realism. I want magic!"
print(line.split(whereSeparator: { $0 == " " })
          .map(String.init))
// Prints "["BLANCHE:", "I", "don\'t", "want", "realism.", "I", "want", "magic!"]"
```

The second example passes `1` for the `maxSplits` parameter, so the original string is split just once, into two new strings.

```swift
print(
   line.split(maxSplits: 1, whereSeparator: { $0 == " " })
                  .map(String.init))
// Prints "["BLANCHE:", "  I don\'t want realism. I want magic!"]"
```

The final example passes `true` for the `allowEmptySlices` parameter, so the returned array contains empty strings where spaces were repeated.

```swift
print(
    line.split(
        omittingEmptySubsequences: false,
        whereSeparator: { $0 == " " }
    ).map(String.init))
// Prints "["BLANCHE:", "", "", "I", "don\'t", "want", "realism.", "I", "want", "magic!"]"
```

> **Note**: O(), where  is the length of the sequence.

## Parameters

- `maxSplits`: The maximum number of times to split the sequence, or one   less than the number of subsequences to return. If    subsequences are returned, the last one is a suffix of the original   sequence containing the remaining elements.   must be   greater than or equal to zero. The default value is  .
- `omittingEmptySubsequences`: If  , an empty subsequence is   returned in the result for each pair of consecutive elements   satisfying the   predicate and for each element at the   start or end of the sequence satisfying the   predicate.   If  , only nonempty subsequences are returned. The default   value is  .
- `isSeparator`: A closure that returns   if its argument should be   used to split the sequence; otherwise,  .

## See Also

- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [ArraySlice<Self.Element>]](sequence/split(separator:maxsplits:omittingemptysubsequences:).md)
  Returns the longest possible subsequences of the sequence, in order, around elements equal to the given element.
- [func joined() -> FlattenSequence<Self>](sequence/joined.md)
  Returns the elements of this sequence of sequences, concatenated.
- [func joined(separator: String) -> String](sequence/joined(separator:)-5zjyj.md)
  Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.
- [func joined<Separator>(separator: Separator) -> JoinedSequence<Self>](sequence/joined(separator:)-7w47r.md)
  Returns the concatenated elements of this sequence of sequences, inserting the given separator between each element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/sequence/split(maxsplits:omittingemptysubsequences:whereseparator:))*
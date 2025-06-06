# split(maxSplits:omittingEmptySubsequences:whereSeparator:)

**Framework**: Swift  
**Kind**: method

Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.

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
func split(maxSplits: Int = Int.max, omittingEmptySubsequences: Bool = true, whereSeparator isSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]
```

#### Return Value

An array of subsequences, split from this collection’s elements.

#### Discussion

The resulting array consists of at most `maxSplits + 1` subsequences. Elements that are used to split the sequence are not returned as part of any subsequence.

The following examples show the effects of the `maxSplits` and `omittingEmptySubsequences` parameters when splitting a string using a closure that matches spaces. The first use of `split` returns each word that was originally separated by one or more spaces.

```swift
let line = "BLANCHE:   I don't want realism. I want magic!"
print(line.split(whereSeparator: { $0 == " " }))
// Prints "["BLANCHE:", "I", "don\'t", "want", "realism.", "I", "want", "magic!"]"
```

The second example passes `1` for the `maxSplits` parameter, so the original string is split just once, into two new strings.

```swift
print(line.split(maxSplits: 1, whereSeparator: { $0 == " " }))
// Prints "["BLANCHE:", "  I don\'t want realism. I want magic!"]"
```

The final example passes `false` for the `omittingEmptySubsequences` parameter, so the returned array contains empty strings where spaces were repeated.

```swift
print(line.split(omittingEmptySubsequences: false, whereSeparator: { $0 == " " }))
// Prints "["BLANCHE:", "", "", "I", "don\'t", "want", "realism.", "I", "want", "magic!"]"
```

> **Note**: O(), where  is the length of the collection.

## Parameters

- `maxSplits`: The maximum number of times to split the collection, or   one less than the number of subsequences to return. If    subsequences are returned, the last one is a suffix   of the original collection containing the remaining elements.    must be greater than or equal to zero. The default value   is  .
- `omittingEmptySubsequences`: If  , an empty subsequence is   returned in the result for each pair of consecutive elements   satisfying the   predicate and for each element at the   start or end of the collection satisfying the    predicate. The default value is  .
- `isSeparator`: A closure that takes an element as an argument and   returns a Boolean value indicating whether the collection should be   split at that element.

## See Also

- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](string/split(separator:maxsplits:omittingemptysubsequences:).md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/split(maxsplits:omittingemptysubsequences:whereseparator:))*
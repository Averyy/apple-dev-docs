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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/lazyprefixwhilesequence/iterator/split(separator:maxsplits:omittingemptysubsequences:))*
# split(maxSplits:omittingEmptySubsequences:separator:)

**Framework**: Swift  
**Kind**: method

Returns the longest possible subsequences of the collection, in order, around subsequence that match the regex created by the given closure.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func split(maxSplits: Int = Int.max, omittingEmptySubsequences: Bool = true, @RegexComponentBuilder separator: () -> some RegexComponent) -> [Self.SubSequence]
```

#### Return Value

A collection of substrings, split from this collection’s elements.

## Parameters

- `maxSplits`: The maximum number of times to split the collection,   or one less than the number of subsequences to return.
- `omittingEmptySubsequences`: If  , an empty subsequence is   returned in the result for each consecutive pair of matches   and for each match at the start or end of the collection. If   , only nonempty subsequences are returned.
- `separator`: A closure that returns a regex to be split upon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/bidirectionalcollection/split(maxsplits:omittingemptysubsequences:separator:))*
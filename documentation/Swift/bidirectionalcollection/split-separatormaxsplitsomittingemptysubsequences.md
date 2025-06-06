# split(separator:maxSplits:omittingEmptySubsequences:)

**Framework**: Swift  
**Kind**: method

Returns the longest possible subsequences of the collection, in order, around elements equal to the given separator.

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
func split(separator: some RegexComponent, maxSplits: Int = .max, omittingEmptySubsequences: Bool = true) -> [Self.SubSequence]
```

#### Return Value

A collection of substrings, split from this collection’s elements.

## Parameters

- `separator`: A regex describing elements to be split upon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/bidirectionalcollection/split(separator:maxsplits:omittingemptysubsequences:))*
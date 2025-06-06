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
func split<C>(separator: C, maxSplits: Int = .max, omittingEmptySubsequences: Bool = true) -> [Self.SubSequence] where C : Collection, Self.Element == C.Element
```

#### Return Value

A collection of subsequences, split from this collection’s elements.

## Parameters

- `separator`: The element to be split upon.

## See Also

- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](collection/split(separator:maxsplits:omittingemptysubsequences:)-6c22.md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](collection/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/collection/split(separator:maxsplits:omittingemptysubsequences:)-9esbr)*
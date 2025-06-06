# sort(using:)

**Framework**: MusicKit  
**Kind**: method

Sorts the collection using the given array of `SortComparator`s to compare elements.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
mutating func sort<S, Comparator>(using comparators: S) where S : Sequence, Comparator : SortComparator, Comparator == S.Element, Self.Element == Comparator.Compared
```

## Parameters

- `comparators`: An array of comparators used to compare elements. The   first comparator specifies the primary comparator to be used in   sorting the sequence’s elements. Any subsequent comparators are used   to further refine the order of elements with equal values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/applicationmusicplayer/queue-swift.class/entries-swift.struct/sort(using:)-2vim9)*
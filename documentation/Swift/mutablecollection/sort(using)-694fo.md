# sort(using:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Sorts the collection using the given comparator to compare elements.

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
mutating func sort<Comparator>(using comparator: Comparator) where Comparator : SortComparator, Self.Element == Comparator.Compared
```

Available when `Self` conforms to `RandomAccessCollection`.

## Parameters

- `comparator`: The sort comparator used to compare elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mutablecollection/sort(using:)-694fo)*
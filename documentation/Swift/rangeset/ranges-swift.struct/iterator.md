# RangeSet.Ranges.Iterator

**Framework**: Swift  
**Kind**: typealias  
**Role**: Type Alias

A type that provides the sequence’s iteration interface and encapsulates its iteration state.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
typealias Iterator = IndexingIterator<RangeSet<Bound>.Ranges>
```

Available when `Bound` conforms to `Comparable`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/rangeset/ranges-swift.struct/iterator)*
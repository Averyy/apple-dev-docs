# Range.Iterator

**Framework**: Swift  
**Kind**: typealias  
**Role**: Type Alias

A type that provides the sequence’s iteration interface and encapsulates its iteration state.

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
typealias Iterator = IndexingIterator<Range<Bound>>
```

Available when `Bound` conforms to `Strideable` and `Bound.Stride` conforms to `SignedInteger`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/range/iterator)*
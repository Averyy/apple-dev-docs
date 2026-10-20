# DiscontiguousSlice.Iterator

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
typealias Iterator = IndexingIterator<DiscontiguousSlice<Base>>
```

Available when `Base` conforms to `Collection`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/discontiguousslice/iterator)*
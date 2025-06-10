# index(before:)

**Framework**: Swift  
**Kind**: method

A value less than or equal to the number of elements in the collection.

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
func index(before i: LazyMapSequence<Base, Element>.Index) -> LazyMapSequence<Base, Element>.Index
```

#### Discussion

> **Note**: O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the length of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/lazymapsequence/index(before:))*
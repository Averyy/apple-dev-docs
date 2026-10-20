# makeIterator()

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Returns an iterator over the elements of this sequence.

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
func makeIterator() -> LazyFilterSequence<Base>.Iterator
```

Available when `Base` conforms to `Sequence`.

#### Discussion

> **Complexity**: O(1).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/lazyfiltersequence/makeiterator())*
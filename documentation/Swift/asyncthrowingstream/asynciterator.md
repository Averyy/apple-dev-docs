# AsyncThrowingStream.AsyncIterator

**Framework**: Swift  
**Kind**: typealias  
**Role**: Type Alias

The type of asynchronous iterator that produces elements of this asynchronous sequence.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
typealias AsyncIterator = AsyncThrowingStream<Element, Failure>.Iterator
```

Available when `Failure` conforms to `Error`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncthrowingstream/asynciterator)*
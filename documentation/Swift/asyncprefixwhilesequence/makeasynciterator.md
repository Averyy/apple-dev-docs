# makeAsyncIterator()

**Framework**: Swift  
**Kind**: method

Creates the asynchronous iterator that produces elements of this asynchronous sequence.

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
func makeAsyncIterator() -> AsyncPrefixWhileSequence<Base>.Iterator
```

#### Return Value

An instance of the `AsyncIterator` type used to produce elements of the asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncprefixwhilesequence/makeasynciterator())*
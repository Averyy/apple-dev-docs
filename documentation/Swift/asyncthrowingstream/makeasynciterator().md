# makeAsyncIterator()

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

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
func makeAsyncIterator() -> AsyncThrowingStream<Element, Failure>.Iterator
```

Available when `Failure` conforms to `Error`.

## See Also

### Creating an Iterator
- [AsyncThrowingStream.Iterator](./iterator.md)
  The asynchronous iterator for iterating an asynchronous stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncthrowingstream/makeasynciterator())*
# makeAsyncIterator()

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

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
func makeAsyncIterator() -> Self.AsyncIterator
```

#### Return Value

An instance of the `AsyncIterator` type used to produce elements of the asynchronous sequence.

## See Also

- [associatedtype AsyncIterator : AsyncIteratorProtocol](asyncsequence/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
- [protocol AsyncIteratorProtocol](asynciteratorprotocol.md)
  A type that asynchronously supplies the values of a sequence one at a time.
- [associatedtype Element](asyncsequence/element.md)
  The type of element produced by this asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncsequence/makeasynciterator())*
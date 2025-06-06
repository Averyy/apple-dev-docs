# Element

**Framework**: Swift  
**Kind**: associatedtype  
**Required**: Yes

The type of element produced by this asynchronous sequence.

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
associatedtype Element where Self.Element == Self.AsyncIterator.Element
```

## See Also

- [func makeAsyncIterator() -> Self.AsyncIterator](asyncsequence/makeasynciterator.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.
- [associatedtype AsyncIterator : AsyncIteratorProtocol](asyncsequence/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
- [protocol AsyncIteratorProtocol](asynciteratorprotocol.md)
  A type that asynchronously supplies the values of a sequence one at a time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncsequence/element)*
# makeAsyncIterator()

**Framework**: ExtensionFoundation  
**Kind**: method  
**Role**: Instance Method

Creates the asynchronous iterator that produces elements of this asynchronous sequence.

**Availability**:
- macOS 13.0+ - Deprecated in 26.0

> **Deprecated**: Replaced with AppExtensionPoint.Monitor

## Declaration

```swift
func makeAsyncIterator() -> AppExtensionIdentity.Identities.AsyncIterator
```

## Return Value

An instance of the `AsyncIterator` type used to produce elements of the asynchronous sequence.

## See Also

### Iterating the Sequence
- [func next() async -> [AppExtensionIdentity]?](./asynciterator/next%28%29.md)
  Asynchronously advances to the next element and returns it.
- [AppExtensionIdentity.Identities.AsyncIterator](./asynciterator.md)
  The type of the asynchronous iterator created by this asynchronous sequence.
- [AppExtensionIdentity.Identities.Element](./element.md)
  The type of element produced by this asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionidentity/identities/makeasynciterator())*
# AppExtensionIdentity.Identities.Element

**Framework**: ExtensionFoundation  
**Kind**: typealias  
**Role**: Type Alias

The type of element produced by this asynchronous sequence.

**Availability**:
- macOS 13.0+ - Deprecated in 26.0

> **Deprecated**: Replaced with AppExtensionPoint.Monitor

## Declaration

```swift
typealias Element = [AppExtensionIdentity]
```

## See Also

### Iterating the Sequence
- [func next() async -> [AppExtensionIdentity]?](./asynciterator/next%28%29.md)
  Asynchronously advances to the next element and returns it.
- [AppExtensionIdentity.Identities.AsyncIterator](./asynciterator.md)
  The type of the asynchronous iterator created by this asynchronous sequence.
- [func makeAsyncIterator() -> AppExtensionIdentity.Identities.AsyncIterator](./makeasynciterator%28%29.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionidentity/identities/element)*
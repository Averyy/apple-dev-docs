# AppExtensionIdentity.Identities.AsyncIterator

**Framework**: ExtensionFoundation  
**Kind**: struct  
**Role**: Structure

The type of the asynchronous iterator created by this asynchronous sequence.

**Availability**:
- macOS 13.0+ - Deprecated in 26.0

> **Deprecated**: Replaced with AppExtensionPoint.Monitor

## Declaration

```swift
struct AsyncIterator
```

## Topics

### Iterating Extensions
- [AppExtensionIdentity.Identities.Element](./element.md)
  The type of element produced by this asynchronous sequence.
- [func next() async -> [AppExtensionIdentity]?](./asynciterator/next%28%29.md)
  Asynchronously advances to the next element and returns it.

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../../../Swift/asynciteratorprotocol.md)

## See Also

### Iterating the Sequence
- [func next() async -> [AppExtensionIdentity]?](./asynciterator/next%28%29.md)
  Asynchronously advances to the next element and returns it.
- [AppExtensionIdentity.Identities.Element](./element.md)
  The type of element produced by this asynchronous sequence.
- [func makeAsyncIterator() -> AppExtensionIdentity.Identities.AsyncIterator](./makeasynciterator%28%29.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionidentity/identities/asynciterator)*
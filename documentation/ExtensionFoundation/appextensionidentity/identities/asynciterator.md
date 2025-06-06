# AppExtensionIdentity.Identities.AsyncIterator

**Framework**: ExtensionFoundation  
**Kind**: struct

The type of the asynchronous iterator created by this asynchronous sequence.

**Availability**:
- macOS 13.0+

## Declaration

```swift
struct AsyncIterator
```

## Topics

### Iterating Extensions
- [AppExtensionIdentity.Identities.Element](appextensionidentity/identities/element.md)
  The type of element produced by this asynchronous sequence.
- [func next() async -> [AppExtensionIdentity]?](appextensionidentity/identities/asynciterator/next.md)
  Asynchronously advances to the next element and returns it.

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../Swift/AsyncIteratorProtocol.md)

## See Also

- [func next() async -> [AppExtensionIdentity]?](appextensionidentity/identities/asynciterator/next.md)
  Asynchronously advances to the next element and returns it.
- [AppExtensionIdentity.Identities.Element](appextensionidentity/identities/element.md)
  The type of element produced by this asynchronous sequence.
- [func makeAsyncIterator() -> AppExtensionIdentity.Identities.AsyncIterator](appextensionidentity/identities/makeasynciterator.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionidentity/identities/asynciterator)*
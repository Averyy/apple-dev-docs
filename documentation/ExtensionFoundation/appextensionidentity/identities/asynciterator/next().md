# next()

**Framework**: ExtensionFoundation  
**Kind**: method  
**Role**: Instance Method

Asynchronously advances to the next element and returns it.

**Availability**:
- macOS 13.0+ - Deprecated in 26.0

> **Deprecated**: Replaced with AppExtensionPoint.Monitor

## Declaration

```swift
mutating func next() async -> [AppExtensionIdentity]?
```

#### Return Value

The next element, if it exists, or `nil` to signal the end of the sequence.

## See Also

### Iterating the Sequence
- [AppExtensionIdentity.Identities.AsyncIterator](../asynciterator.md)
  The type of the asynchronous iterator created by this asynchronous sequence.
- [AppExtensionIdentity.Identities.Element](../element.md)
  The type of element produced by this asynchronous sequence.
- [func makeAsyncIterator() -> AppExtensionIdentity.Identities.AsyncIterator](../makeasynciterator%28%29.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionidentity/identities/asynciterator/next())*
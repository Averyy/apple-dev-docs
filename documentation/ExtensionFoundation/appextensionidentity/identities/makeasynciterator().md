# makeAsyncIterator()

**Framework**: ExtensionFoundation  
**Kind**: method

Creates the asynchronous iterator that produces elements of this asynchronous sequence.

**Availability**:
- macOS 13.0+

## Declaration

```swift
func makeAsyncIterator() -> AppExtensionIdentity.Identities.AsyncIterator
```

#### Return Value

An instance of the `AsyncIterator` type used to produce elements of the asynchronous sequence.

## See Also

- [func next() async -> [AppExtensionIdentity]?](appextensionidentity/identities/asynciterator/next.md)
  Asynchronously advances to the next element and returns it.
- [AppExtensionIdentity.Identities.AsyncIterator](appextensionidentity/identities/asynciterator.md)
  The type of the asynchronous iterator created by this asynchronous sequence.
- [AppExtensionIdentity.Identities.Element](appextensionidentity/identities/element.md)
  The type of element produced by this asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionidentity/identities/makeasynciterator())*
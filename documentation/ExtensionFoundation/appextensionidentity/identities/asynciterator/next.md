# next()

**Framework**: ExtensionFoundation  
**Kind**: method

Asynchronously advances to the next element and returns it.

**Availability**:
- macOS 13.0+

## Declaration

```swift
mutating func next() async -> [AppExtensionIdentity]?
```

#### Return Value

The next element, if it exists, or `nil` to signal the end of the sequence.

## See Also

- [AppExtensionIdentity.Identities.AsyncIterator](appextensionidentity/identities/asynciterator.md)
  The type of the asynchronous iterator created by this asynchronous sequence.
- [AppExtensionIdentity.Identities.Element](appextensionidentity/identities/element.md)
  The type of element produced by this asynchronous sequence.
- [func makeAsyncIterator() -> AppExtensionIdentity.Identities.AsyncIterator](appextensionidentity/identities/makeasynciterator.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionidentity/identities/asynciterator/next())*
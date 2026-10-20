# AppExtensionIdentity.Identities

**Framework**: ExtensionFoundation  
**Kind**: struct  
**Role**: Structure

An asynchronous sequence that returns the enabled extensions that match provided constraints.

**Availability**:
- macOS 13.0+ - Deprecated in 26.0

> **Deprecated**: Replaced with AppExtensionPoint.Monitor

## Declaration

```swift
struct Identities
```

## Topics

### Iterating the Sequence
- [func next() async -> [AppExtensionIdentity]?](./identities/asynciterator/next%28%29.md)
  Asynchronously advances to the next element and returns it.
- [AppExtensionIdentity.Identities.AsyncIterator](./identities/asynciterator.md)
  The type of the asynchronous iterator created by this asynchronous sequence.
- [AppExtensionIdentity.Identities.Element](./identities/element.md)
  The type of element produced by this asynchronous sequence.
- [func makeAsyncIterator() -> AppExtensionIdentity.Identities.AsyncIterator](./identities/makeasynciterator%28%29.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.

## Relationships

### Conforms To
- [AsyncSequence](../../Swift/asyncsequence.md)

## See Also

### Deprecated
- [AppExtensionIdentity.Availability](./availability.md)
  An object that contains information about available extensions.
- [static var availabilityUpdates: AsyncStream<AppExtensionIdentity.Availability>](./availabilityupdates.md)
- [static func matching(appExtensionPointIDs: String...) throws -> AppExtensionIdentity.Identities](./matching%28appextensionpointids%29.md)
  The asynchronous sequence of extension identities which target the specified extension point identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionidentity/identities)*
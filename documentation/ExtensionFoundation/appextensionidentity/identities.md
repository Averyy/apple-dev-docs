# AppExtensionIdentity.Identities

**Framework**: ExtensionFoundation  
**Kind**: struct

An asynchronous sequence that returns the enabled extensions that match provided constraints.

**Availability**:
- macOS 13.0+

## Declaration

```swift
struct Identities
```

## Topics

### Iterating the Sequence
- [func next() async -> [AppExtensionIdentity]?](appextensionidentity/identities/asynciterator/next.md)
  Asynchronously advances to the next element and returns it.
- [AppExtensionIdentity.Identities.AsyncIterator](appextensionidentity/identities/asynciterator.md)
  The type of the asynchronous iterator created by this asynchronous sequence.
- [AppExtensionIdentity.Identities.Element](appextensionidentity/identities/element.md)
  The type of element produced by this asynchronous sequence.
- [func makeAsyncIterator() -> AppExtensionIdentity.Identities.AsyncIterator](appextensionidentity/identities/makeasynciterator.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)

## See Also

- [AppExtensionIdentity.Availability](appextensionidentity/availability.md)
  An object that contains information about available extensions.
- [static var availabilityUpdates: AsyncStream<AppExtensionIdentity.Availability>](appextensionidentity/availabilityupdates.md)
- [static func matching(appExtensionPointIDs: String...) throws -> AppExtensionIdentity.Identities](appextensionidentity/matching(appextensionpointids:).md)
  The asynchronous sequence of extension identities which target the specified extension point identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionidentity/identities)*
# matching(appExtensionPointIDs:)

**Framework**: ExtensionFoundation  
**Kind**: method  
**Role**: Type Method

The asynchronous sequence of extension identities which target the specified extension point identifiers.

**Availability**:
- macOS 13.0+ - Deprecated in 26.0

> **Deprecated**: Replaced with AppExtensionPoint.Monitor

## Declaration

```swift
static func matching(appExtensionPointIDs: String...) throws -> AppExtensionIdentity.Identities
```

## See Also

### Deprecated
- [AppExtensionIdentity.Availability](./availability.md)
  An object that contains information about available extensions.
- [static var availabilityUpdates: AsyncStream<AppExtensionIdentity.Availability>](./availabilityupdates.md)
- [AppExtensionIdentity.Identities](./identities.md)
  An asynchronous sequence that returns the enabled extensions that match provided constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionidentity/matching(appextensionpointids:))*
# matching(appExtensionPointIDs:)

**Framework**: ExtensionFoundation  
**Kind**: method

The asynchronous sequence of extension identities which target the specified extension point identifiers.

**Availability**:
- macOS 13.0+

## Declaration

```swift
static func matching(appExtensionPointIDs: String...) throws -> AppExtensionIdentity.Identities
```

## See Also

- [AppExtensionIdentity.Availability](appextensionidentity/availability.md)
  An object that contains information about available extensions.
- [static var availabilityUpdates: AsyncStream<AppExtensionIdentity.Availability>](appextensionidentity/availabilityupdates.md)
- [AppExtensionIdentity.Identities](appextensionidentity/identities.md)
  An asynchronous sequence that returns the enabled extensions that match provided constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionidentity/matching(appextensionpointids:))*
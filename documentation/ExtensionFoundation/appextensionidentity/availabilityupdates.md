# availabilityUpdates

**Framework**: ExtensionFoundation  
**Kind**: property  
**Role**: Type Property

**Availability**:
- macOS 13.0+ - Deprecated in 26.0

> **Deprecated**: Replaced with AppExtensionPoint.Monitor

## Declaration

```swift
static var availabilityUpdates: AsyncStream<AppExtensionIdentity.Availability> { get }
```

## See Also

### Deprecated
- [AppExtensionIdentity.Availability](./availability.md)
  An object that contains information about available extensions.
- [static func matching(appExtensionPointIDs: String...) throws -> AppExtensionIdentity.Identities](./matching%28appextensionpointids%29.md)
  The asynchronous sequence of extension identities which target the specified extension point identifiers.
- [AppExtensionIdentity.Identities](./identities.md)
  An asynchronous sequence that returns the enabled extensions that match provided constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionidentity/availabilityupdates)*
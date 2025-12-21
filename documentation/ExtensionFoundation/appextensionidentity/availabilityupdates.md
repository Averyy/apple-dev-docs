# availabilityUpdates

**Framework**: ExtensionFoundation  
**Kind**: property

**Availability**:
- macOS 13.0+

## Declaration

```swift
static var availabilityUpdates: AsyncStream<AppExtensionIdentity.Availability> { get }
```

## See Also

- [AppExtensionIdentity.Availability](appextensionidentity/availability.md)
  An object that contains information about available extensions.
- [static func matching(appExtensionPointIDs: String...) throws -> AppExtensionIdentity.Identities](appextensionidentity/matching(appextensionpointids:).md)
  The asynchronous sequence of extension identities which target the specified extension point identifiers.
- [AppExtensionIdentity.Identities](appextensionidentity/identities.md)
  An asynchronous sequence that returns the enabled extensions that match provided constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionidentity/availabilityupdates)*
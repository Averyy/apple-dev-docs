# AppExtensionIdentity.Availability

**Framework**: ExtensionFoundation  
**Kind**: struct

An object that contains information about available extensions.

**Availability**:
- macOS 13.0+

## Declaration

```swift
struct Availability
```

## Topics

### Creating an Availability Object
- [init()](appextensionidentity/availability/init.md)
  Creates an app extension identity availability object.
### Accessing Availability Information
- [var description: String](appextensionidentity/availability/description.md)
  A string describing the extensions availability.
- [var totalCount: Int](appextensionidentity/availability/totalcount.md)
  The number of extensions not yet approved for hosting by the current app.
- [let disabledCount: Int](appextensionidentity/availability/disabledcount.md)
  The number of extensions disabled for hosting in the current app.
- [let enabledCount: Int](appextensionidentity/availability/enabledcount.md)
  The number of extensions enabled for hostng in the current app.
- [let unapprovedCount: Int](appextensionidentity/availability/unapprovedcount.md)
  The number of extensions not yet approved for hosing by the current app

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static var availabilityUpdates: AsyncStream<AppExtensionIdentity.Availability>](appextensionidentity/availabilityupdates.md)
- [static func matching(appExtensionPointIDs: String...) throws -> AppExtensionIdentity.Identities](appextensionidentity/matching(appextensionpointids:).md)
  The asynchronous sequence of extension identities which target the specified extension point identifiers.
- [AppExtensionIdentity.Identities](appextensionidentity/identities.md)
  An asynchronous sequence that returns the enabled extensions that match provided constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionidentity/availability)*
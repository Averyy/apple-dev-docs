# AppExtensionIdentity.Availability

**Framework**: ExtensionFoundation  
**Kind**: struct  
**Role**: Structure

An object that contains information about available extensions.

**Availability**:
- macOS 13.0+ - Deprecated in 26.0

> **Deprecated**: Replaced with AppExtensionPoint.Monitor

## Declaration

```swift
struct Availability
```

## Topics

### Creating an Availability Object
- [init()](./availability/init%28%29.md)
  Creates an app extension identity availability object.
### Accessing Availability Information
- [var description: String](./availability/description.md)
  A string describing the extensions availability.
- [var totalCount: Int](./availability/totalcount.md)
  The number of extensions not yet approved for hosting by the current app.
- [let disabledCount: Int](./availability/disabledcount.md)
  The number of extensions disabled for hosting in the current app.
- [let enabledCount: Int](./availability/enabledcount.md)
  The number of extensions enabled for hostng in the current app.
- [let unapprovedCount: Int](./availability/unapprovedcount.md)
  The number of extensions not yet approved for hosing by the current app

## Relationships

### Conforms To
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Deprecated
- [static var availabilityUpdates: AsyncStream<AppExtensionIdentity.Availability>](./availabilityupdates.md)
- [static func matching(appExtensionPointIDs: String...) throws -> AppExtensionIdentity.Identities](./matching%28appextensionpointids%29.md)
  The asynchronous sequence of extension identities which target the specified extension point identifiers.
- [AppExtensionIdentity.Identities](./identities.md)
  An asynchronous sequence that returns the enabled extensions that match provided constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionidentity/availability)*
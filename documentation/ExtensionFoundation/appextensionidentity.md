# AppExtensionIdentity

**Framework**: ExtensionFoundation  
**Kind**: struct

An object that uniquely identifies an app extension.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 13.0+
- tvOS 26.0+ (Beta)
- visionOS 1.1+
- watchOS 26.0+ (Beta)

## Declaration

```swift
struct AppExtensionIdentity
```

## Topics

### Identifying the Process
- [var bundleIdentifier: String](appextensionidentity/bundleidentifier.md)
  The bundle identifier for the extension.
- [var extensionPointIdentifier: String](appextensionidentity/extensionpointidentifier.md)
  A unique identifier for the extension point this extension targets.
- [var localizedName: String](appextensionidentity/localizedname.md)
  A localized, human-readable name for the extension.
- [AppExtensionIdentity.Identities](appextensionidentity/identities.md)
  An asynchronous sequence that returns the enabled extensions that match provided constraints.
### Monitoring Extensions
- [AppExtensionIdentity.Availability](appextensionidentity/availability.md)
  An object that contains information about available extensions.
- [static var availabilityUpdates: AsyncStream<AppExtensionIdentity.Availability>](appextensionidentity/availabilityupdates.md)
### Comparing Extensions
- [func hash(into: inout Hasher)](appextensionidentity/hash(into:).md)
  Hashes the essential components of the extension by feeding them into the given hash function.
- [static func == (AppExtensionIdentity, AppExtensionIdentity) -> Bool](appextensionidentity/==(_:_:).md)
  Indicates whether two extensions are equal
### Type Methods
- [static func matching(appExtensionPointIDs: String...) throws -> AppExtensionIdentity.Identities](appextensionidentity/matching(appextensionpointids:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol AppExtension](appextension.md)
  Declares a type used by app extensions.
- [protocol AppExtensionConfiguration](appextensionconfiguration.md)
  An object that holds configuration options for an app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionidentity)*
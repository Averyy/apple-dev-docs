# AppExtensionIdentity

**Framework**: ExtensionFoundation  
**Kind**: struct

A type that uniquely identifies an app extension on the system.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 13.0+
- tvOS 26.0+
- visionOS 1.1+
- watchOS 26.0+

## Declaration

```swift
struct AppExtensionIdentity
```

## Mentions

- [Discovering app extensions from your app](discovering-app-extensions-from-your-app.md)

#### Overview

Use this type to identify an app extension on the system and connect to it. You don’t create this type directly. Instead, you use the [`AppExtensionPoint.Monitor`](appextensionpoint/monitor.md) type to retrieve instances of this type for the available app extensions.

## Topics

### Identifying the process
- [var bundleIdentifier: String](appextensionidentity/bundleidentifier.md)
  The bundle identifier of the app extension.
- [var extensionPointIdentifier: String](appextensionidentity/extensionpointidentifier.md)
  The extension point of your host app that the app extension supports.
- [var localizedName: String](appextensionidentity/localizedname.md)
  The localized, human-readable name of the app extension.
### Comparing app extensions
- [func hash(into: inout Hasher)](appextensionidentity/hash(into:).md)
  Hashes the essential components of the extension by feeding them into the given hash function.
- [static func == (AppExtensionIdentity, AppExtensionIdentity) -> Bool](appextensionidentity/==(_:_:).md)
  Returns a Boolean value that indicates whether two identities are equal.
### Deprecated
- [AppExtensionIdentity.Availability](appextensionidentity/availability.md)
  An object that contains information about available extensions.
- [static var availabilityUpdates: AsyncStream<AppExtensionIdentity.Availability>](appextensionidentity/availabilityupdates.md)
- [static func matching(appExtensionPointIDs: String...) throws -> AppExtensionIdentity.Identities](appextensionidentity/matching(appextensionpointids:).md)
  The asynchronous sequence of extension identities which target the specified extension point identifiers.
- [AppExtensionIdentity.Identities](appextensionidentity/identities.md)
  An asynchronous sequence that returns the enabled extensions that match provided constraints.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Discovering app extensions from your app](discovering-app-extensions-from-your-app.md)
  Find the app extensions that match your host app’s extension points and are available to use.
- [struct AppExtensionProcess](appextensionprocess.md)
  A type the host app creates to launch and manage an app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionidentity)*
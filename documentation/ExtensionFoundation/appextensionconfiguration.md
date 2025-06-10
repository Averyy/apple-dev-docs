# AppExtensionConfiguration

**Framework**: ExtensionFoundation  
**Kind**: protocol

An object that holds configuration options for an app extension.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.1+
- watchOS 9.0+

## Declaration

```swift
@MainActor
@preconcurrency protocol AppExtensionConfiguration : Sendable
```

## Topics

### Accepting Connection Requests
- [func accept(connection: NSXPCConnection) -> Bool](appextensionconfiguration/accept(connection:).md)
  A method the system calls when a host app tries to connect.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [ConnectionHandler](connectionhandler.md)

## See Also

- [struct AppExtensionIdentity](appextensionidentity.md)
  An object that uniquely identifies an app extension.
- [protocol AppExtension](appextension.md)
  Declares a type used by app extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionconfiguration)*
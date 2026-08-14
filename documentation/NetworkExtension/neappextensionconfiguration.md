# NEAppExtensionConfiguration

**Framework**: Network Extension  
**Kind**: class

A class that defines configuration options for use in NetworkExtension app extensions.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency class NEAppExtensionConfiguration
```

#### Overview

This class conforms to `NEAppExtensionConfigurationProtocol` and [`AppExtensionConfiguration`](https://developer.apple.com/documentation/extensionfoundation/appextensionconfiguration) from the [`ExtensionFoundation`](https://developer.apple.com/documentation/extensionfoundation) framework. It exists only for use by the framework; you don’t need to use its methods and properties directly.

## Topics

### Communicating over XPC
- [func accept(connection: NSXPCConnection) -> Bool](neappextensionconfiguration/accept(connection:).md)
  Accepts incoming XPC connections from the host process.

## Relationships

### Inherited By
- [NEHotspotAuthenticationProviderConfiguration](nehotspotauthenticationproviderconfiguration.md)
- [NEHotspotEvaluationProviderConfiguration](nehotspotevaluationproviderconfiguration.md)
- [NEURLFilterControlProviderConfiguration](neurlfiltercontrolproviderconfiguration.md)
### Conforms To
- [AppExtensionConfiguration](../extensionfoundation/appextensionconfiguration.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappextensionconfiguration)*
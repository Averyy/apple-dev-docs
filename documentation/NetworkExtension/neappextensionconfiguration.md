# NEAppExtensionConfiguration

**Framework**: Network Extension  
**Kind**: class

A class that defines configuration options for use in NetworkExtension app extensions.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency class NEAppExtensionConfiguration
```

#### Overview

This class conforms to [`NEAppExtensionConfigurationProtocol`](neappextensionconfigurationprotocol.md) and [`AppExtensionConfiguration`](https://developer.apple.com/documentation/ExtensionFoundation/AppExtensionConfiguration) from the [`ExtensionFoundation`](https://developer.apple.com/documentation/ExtensionFoundation) framework. It exists only for use by the framework; you don’t need to use its methods and properties directly.

## Topics

### Setting up the extension
- [func setup(reply: (Bool) -> Void)](neappextensionconfiguration/setup(reply:).md)
  Sets up the app extension.
### Communicating over XPC
- [func accept(connection: NSXPCConnection) -> Bool](neappextensionconfiguration/accept(connection:).md)
  Accepts incoming XPC connections from the host process.
- [var xpcConnection: NSXPCConnection?](neappextensionconfiguration/xpcconnection.md)
  The XPC connection to the host process.
### Accessing the app extension
- [let appex: any NEAppExtension](neappextensionconfiguration/appex.md)
  The framework accesses this property. You don’t need to use it in your app extension.

## Relationships

### Inherited By
- [NEHotspotAuthenticationProviderConfiguration](nehotspotauthenticationproviderconfiguration.md)
- [NEHotspotEvaluationProviderConfiguration](nehotspotevaluationproviderconfiguration.md)
- [NEURLFilterControlProviderConfiguration](neurlfiltercontrolproviderconfiguration.md)
### Conforms To
- [AppExtensionConfiguration](../ExtensionFoundation/AppExtensionConfiguration.md)
- [NEAppExtensionConfigurationProtocol](neappextensionconfigurationprotocol.md)
- [NEAppExtensionXPCProtocol](neappextensionxpcprotocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol NEAppExtension](neappextension.md)
  A protocol that defines common functionality for other extension protocols in the NetworkExtension framework.
- [protocol NEAppExtensionConfigurationProtocol](neappextensionconfigurationprotocol.md)
  A protocol to provide configuration options to NetworkExtension app extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappextensionconfiguration)*
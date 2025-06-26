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

This class conforms to `NEAppExtensionConfigurationProtocol` and [`AppExtensionConfiguration`](https://developer.apple.com/documentation/ExtensionFoundation/AppExtensionConfiguration) from the [`ExtensionFoundation`](https://developer.apple.com/documentation/ExtensionFoundation) framework. It exists only for use by the framework; you don’t need to use its methods and properties directly.

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
- [AppExtensionConfiguration](../ExtensionFoundation/AppExtensionConfiguration.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappextensionconfiguration)*
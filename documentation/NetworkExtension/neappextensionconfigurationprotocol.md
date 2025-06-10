# NEAppExtensionConfigurationProtocol

**Framework**: Network Extension  
**Kind**: protocol

A protocol to provide configuration options to NetworkExtension app extensions.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
protocol NEAppExtensionConfigurationProtocol : AppExtensionConfiguration
```

#### Overview

This protocol extends [`AppExtensionConfiguration`](https://developer.apple.com/documentation/ExtensionFoundation/AppExtensionConfiguration) from the [`ExtensionFoundation`](https://developer.apple.com/documentation/ExtensionFoundation) framework.

## Relationships

### Inherits From
- [AppExtensionConfiguration](../ExtensionFoundation/AppExtensionConfiguration.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [NEAppExtensionConfiguration](neappextensionconfiguration.md)
- [NEHotspotAuthenticationProviderConfiguration](nehotspotauthenticationproviderconfiguration.md)
- [NEHotspotEvaluationProviderConfiguration](nehotspotevaluationproviderconfiguration.md)
- [NEURLFilterControlProviderConfiguration](neurlfiltercontrolproviderconfiguration.md)

## See Also

- [protocol NEAppExtension](neappextension.md)
  A protocol that defines common functionality for other extension protocols in the NetworkExtension framework.
- [class NEAppExtensionConfiguration](neappextensionconfiguration.md)
  A class that defines configuration options for use in NetworkExtension app extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappextensionconfigurationprotocol)*
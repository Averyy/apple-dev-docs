# NEAppExtension

**Framework**: Network Extension  
**Kind**: protocol

A protocol that defines common functionality for other extension protocols in the NetworkExtension framework.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
protocol NEAppExtension : AppExtension
```

#### Overview

This protocol conforms to the [`AppExtension`](https://developer.apple.com/documentation/ExtensionFoundation/AppExtension) protocol in the [`ExtensionFoundation`](https://developer.apple.com/documentation/ExtensionFoundation) framework. The [`NEURLFilterControlProvider`](neurlfiltercontrolprovider.md) protocol conforms to this protocol, as do the Hotspot Helper extension protocols, [`NEHotspotAuthenticationProvider`](nehotspotauthenticationprovider.md) and [`NEHotspotEvaluationProvider`](nehotspotevaluationprovider.md).

## Relationships

### Inherits From
- [AppExtension](../ExtensionFoundation/AppExtension.md)
### Inherited By
- [NEHotspotAuthenticationProvider](nehotspotauthenticationprovider.md)
- [NEHotspotEvaluationProvider](nehotspotevaluationprovider.md)
- [NEURLFilterControlProvider](neurlfiltercontrolprovider.md)

## See Also

- [protocol NEAppExtensionConfigurationProtocol](neappextensionconfigurationprotocol.md)
  A protocol to provide configuration options to NetworkExtension app extensions.
- [class NEAppExtensionConfiguration](neappextensionconfiguration.md)
  A class that defines configuration options for use in NetworkExtension app extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappextension)*
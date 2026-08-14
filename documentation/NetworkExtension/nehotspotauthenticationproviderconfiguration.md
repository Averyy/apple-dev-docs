# NEHotspotAuthenticationProviderConfiguration

**Framework**: Network Extension  
**Kind**: class

A class that defines configuration options for use in NetworkExtension authentication providers.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency class NEHotspotAuthenticationProviderConfiguration
```

## Relationships

### Inherits From
- [NEAppExtensionConfiguration](neappextensionconfiguration.md)
### Conforms To
- [AppExtensionConfiguration](../extensionfoundation/appextensionconfiguration.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class NEHotspotManager](nehotspotmanager.md)
  A class that you use to enable or disable the hotspot evaluation and authentication provider extensions.
- [protocol NEHotspotEvaluationProvider](nehotspotevaluationprovider.md)
  A protocol that defines methods and properties your extension implements to handle evaluate and filter scan list commands.
- [protocol NEHotspotAuthenticationProvider](nehotspotauthenticationprovider.md)
  A protocol that defines methods that your extension adopts to start and stop the extension, and to handle commands to authenticate with the hotspot network.
- [class NEHotspotEvaluationProviderConfiguration](nehotspotevaluationproviderconfiguration.md)
  A class that defines configuration options for use in NetworkExtension evaluation providers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotauthenticationproviderconfiguration)*
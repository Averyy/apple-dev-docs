# AccessoryDataProviderConfiguration

**Framework**: Accessory Transport Extension  
**Kind**: protocol

A protocol that configures and manages communication between the extension and the system.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)

## Declaration

```swift
protocol AccessoryDataProviderConfiguration : AppExtensionConfiguration
```

#### Overview

The [`AccessoryDataProvider`](accessorydataprovider.md) protocol uses this configuration type to establish communication channels with the system.

## Relationships

### Inherits From
- [AppExtensionConfiguration](../ExtensionFoundation/AppExtensionConfiguration.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Receiving iOS notifications on an accessory](../AccessoryNotifications/receiving-ios-notifications-on-an-accessory.md)
  Create custom app extensions that manage notifications for your accessory.
- [protocol AccessoryDataProvider](accessorydataprovider.md)
  A protocol for an extension that receives iOS system notifications and curates their data for your accessory.
- [protocol AccessoryTransportSecurity](accessorytransportsecurity.md)
  A protocol for an extension that handles the cryptography of messages to your accessory.
- [protocol AccessoryTransportSecurityConfiguration](accessorytransportsecurityconfiguration.md)
  A protocol that configures and manages communication between your security extension and the system.
- [Accessory Notifications](../AccessoryNotifications/AccessoryNotifications.md)
  Receive forwarded iOS system notifications on an accessory that you develop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorydataproviderconfiguration)*
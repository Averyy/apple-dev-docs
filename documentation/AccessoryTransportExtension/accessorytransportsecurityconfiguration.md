# AccessoryTransportSecurityConfiguration

**Framework**: Accessory Transport Extension  
**Kind**: protocol

A protocol that configures and manages communication between your security extension and the system.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)
- Mac Catalyst 26.5+ (Beta)

## Declaration

```swift
protocol AccessoryTransportSecurityConfiguration : AppExtensionConfiguration
```

#### Overview

The [`AccessoryTransportSecurity`](accessorytransportsecurity.md) protocol uses this configuration to establish communication with the system.

## Relationships

### Inherits From
- [AppExtensionConfiguration](../ExtensionFoundation/AppExtensionConfiguration.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Receiving iOS notifications on an accessory](receiving-ios-notifications-on-an-accessory.md)
  Create custom app extensions that manage iOS system notifications for your accessory.
- [protocol AccessoryDataProvider](accessorydataprovider.md)
  A protocol for an extension that receives iOS system notifications and curates their data for your accessory.
- [protocol AccessoryDataProviderConfiguration](accessorydataproviderconfiguration.md)
  A protocol that configures and manages communication between the extension and the system.
- [protocol AccessoryTransportSecurity](accessorytransportsecurity.md)
  A protocol for an extension that handles cryptographic key exchange with your accessory.
- [Accessory Notifications](../AccessoryNotifications/AccessoryNotifications.md)
  Receive forwarded iOS system notifications on an accessory that you develop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsecurityconfiguration)*
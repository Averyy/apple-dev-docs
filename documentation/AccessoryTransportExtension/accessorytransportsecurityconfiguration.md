# AccessoryTransportSecurityConfiguration

**Framework**: Accessory Transport Extension  
**Kind**: protocol  
**Role**: Protocol

A protocol that configures and manages communication between your security extension and the system.

**Availability**:
- iOS 26.5+

## Declaration

```swift
protocol AccessoryTransportSecurityConfiguration : AppExtensionConfiguration
```

## Overview

The [`AccessoryTransportSecurity`](./accessorytransportsecurity.md) protocol uses this configuration to establish communication with the system.

## Relationships

### Inherits From
- [AppExtensionConfiguration](../ExtensionFoundation/appextensionconfiguration.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Notification and Live Activity forwarding
- [Receiving iOS notifications on an accessory](./receiving-ios-notifications-on-an-accessory.md)
  Create custom app extensions that manage iOS system notifications for your accessory.
- [Receiving Live Activity updates and alerts on an accessory](../AccessoryLiveActivities/receiving-live-activities-on-an-accessory.md)
  Enable your accessory to receive forwarded Live Activities by updating your data provider extension.
- [Forwarding notifications to your accessory using the internet transport type](./forwarding-notifications-to-your-accessory-using-the-internet-transport-type.md)
  Send notification data to your accessory over the internet when Bluetooth connectivity is unavailable.
- [protocol AccessoryDataProvider](./accessorydataprovider.md)
  A protocol for an extension that provides your accessory’s data for one or more of the framework’s features.
- [protocol AccessoryDataProviderConfiguration](./accessorydataproviderconfiguration.md)
  A protocol that configures and manages communication between the extension and the system.
- [protocol AccessoryTransportSecurity](./accessorytransportsecurity.md)
  A protocol for an extension that handles cryptographic key exchange with your accessory.
- [Accessory Notifications](../AccessoryNotifications/AccessoryNotifications.md)
  Receive forwarded iOS system notifications on an accessory that you develop.
- [Accessory Live Activities](../AccessoryLiveActivities/AccessoryLiveActivities.md)
  Forward Live Activity alerts from iPhone to an accessory you develop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsecurityconfiguration)*
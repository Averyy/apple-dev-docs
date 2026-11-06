# Accessory Transport Extension

**Framework**: Accessory Transport Extension  
**Kind**: module  
**Role**: Framework

Transfer data securely to connected accessories that you develop.

**Availability**:
- iOS 26.2+

## Overview

Use the Accessory Transport Extension framework to securely transfer information to an accessory that you develop. First, establish a connection with your accessory using [AccessorySetupKit](../AccessorySetupKit/AccessorySetupKit.md). Then, implement extensions for the features your app needs. The number and type of extensions, and their data semantics, depend on your app’s and accessory’s use case.

The framework carries each kind of data between your accessory and your app as a *feature* — for example, notification forwarding, [`LiveActivityForwarding`](../AccessoryLiveActivities/liveactivityforwarding.md), [`AudioAccessoryHeadTracking`](../AudioAccessoryKit/audioaccessoryheadtracking.md), or background work with [`AccessoryWorker`](./accessoryworker.md). The framework defines the set of features; your app declares the ones it supports in its data provider extension. For more information, see [Accessory features](./accessory-features.md).

> ❗ **Important**: This framework is available only for iOS. The framework ignores calls for apps built with Mac Catalyst, and iOS apps that run on visionOS or on Mac computers with Apple silicon.
>
> You can develop and test an app that uses this framework on devices in any region. Customer installations of your app can only use the framework on devices located in the EU that are signed in with an Apple Account with an EU country or region.

## Share a Wi-Fi network with an accessory

Implement the [`AccessoryTransportAppExtension`](./accessorytransportappextension.md) protocol in an extension to share Wi-Fi networks with your accessory. The system calls your extension’s [`accept(sessionRequest:)`](./accessorytransportappextension/accept%28sessionrequest%29.md) method when it’s ready to start. After accepting the session request, your extension connects to the accessory using [`ASAccessorySession`](../AccessorySetupKit/asaccessorysession.md) and delivers Wi-Fi network data using [`WINetworkSharingProvider`](../WiFiInfrastructure/winetworksharingprovider.md).

## Forward notifications and Live Activities to an accessory

Using this framework along with [Accessory Notifications](../AccessoryNotifications/AccessoryNotifications.md), your app can receive iOS system notifications to send alerts to people on a connected accessory that you develop. Implement three extensions to maintain security and encapsulation:

1. [`AccessoryDataProvider`](./accessorydataprovider.md) receives and curates the content of a given notification.
2. The system encrypts the notification data using keys you provide in your [`AccessoryTransportSecurity`](./accessorytransportsecurity.md) extension.
3. The system delivers the encrypted data to your [`AccessoryTransportAppExtension`](./accessorytransportappextension.md) for transmission to the accessory.

Your transport extension sends the encrypted data to your accessory, but can’t decipher the notification’s content.

[Accessory Live Activities](../AccessoryLiveActivities/AccessoryLiveActivities.md) forwarding uses the same three extensions. Add the [`LiveActivityForwarding`](../AccessoryLiveActivities/liveactivityforwarding.md) capability to the [`AccessoryDataProvider`](./accessorydataprovider.md) extension you already implement for notifications, and Live Activity updates and alerts travel the same encrypted path to your accessory.

## Run tasks in the background

With [`AccessoryWorker`](./accessoryworker.md), your app can exchange information with your accessory in the background without waiting for a person to open your app. If someone adjusts a setting on the accessory, for instance, that change reaches the iPhone quietly. When the person opens the companion app, the UI can reflect what happened on the accessory right away.

Your app defines the purpose of the exchanged data and its format; the system carries the data between your extensions in the background. When your accessory has something to report, your transport extension receives the update and passes it to your data provider extension, which saves the result for the companion app to read at next launch.

## Topics

### Wi-Fi network sharing
- [protocol AccessoryTransportAppExtension](./accessorytransportappextension.md)
  A protocol for an extension that transmits data to an accessory you develop.
- [protocol AccessoryTransportExtensionConfiguration](./accessorytransportextensionconfiguration.md)
  An interface that enables you to configure and manage communication between your extension and the system.
- [class AccessoryTransportSession](./accessorytransportsession.md)
  A class that manages a transport session between the extension and the system.
- [Wi-Fi Infrastructure](../WiFiInfrastructure/WiFiInfrastructure.md)
  Share Wi-Fi network credentials securely between devices and connected accessories.
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
- [protocol AccessoryTransportSecurityConfiguration](./accessorytransportsecurityconfiguration.md)
  A protocol that configures and manages communication between your security extension and the system.
- [Accessory Notifications](../AccessoryNotifications/AccessoryNotifications.md)
  Receive forwarded iOS system notifications on an accessory that you develop.
- [Accessory Live Activities](../AccessoryLiveActivities/AccessoryLiveActivities.md)
  Forward Live Activity alerts from iPhone to an accessory you develop.
### Transport messaging and security
- [struct AccessoryMessage](./accessorymessage.md)
  A structure that represents a message to send to an accessory.
- [class AccessorySecuritySession](./accessorysecuritysession.md)
  A class that manages a security session between the extension and the system.
- [struct TransportMessage](./transportmessage.md)
  A structure that represents a message for transmission between the system and an accessory.
- [struct SecurityMessage](./securitymessage.md)
  A structure that carries key material for a secure channel between the system and an accessory.
- [enum AccessoryTransport](./accessorytransport.md)
  Transport methods for communicating with an accessory.
### Feature catalog
- [Accessory features](./accessory-features.md)
  Declare and handle the features that carry data between your accessory and your app.
### Background work
- [Sending data to an accessory in the background](./sending-data-to-an-accessory-in-the-background.md)
  Move data between your accessory and your app when a person’s device is asleep or your app is in the background.
- [struct AccessoryWorker](./accessoryworker.md)
  A feature that carries data between your data provider and transport extensions.
- [struct AccessoryGPUWorker](./accessorygpuworker.md)
  A feature for GPU work that carries data between your data provider and transport extensions.
### Protocols
- [protocol AccessoryFeatureAuthorizing](./accessoryfeatureauthorizing.md)
  A feature that is authorized separately on each accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AccessoryTransportExtension)*
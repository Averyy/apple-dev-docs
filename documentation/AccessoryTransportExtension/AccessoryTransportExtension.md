# Accessory Transport Extension

**Framework**: Accessory Transport Extension  
**Kind**: module

Transfer data securely to connected accessories that you develop.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+

#### Overview

Use the Accessory Transport Extension framework to securely transfer information to an accessory that you develop. First, establish a connection with your accessory using [`AccessorySetupKit`](https://developer.apple.com/documentation/AccessorySetupKit). Then, you can share Wi-Fi networks with your accessory using [`Wi-Fi Infrastructure`](https://developer.apple.com/documentation/WiFiInfrastructure), or forward iOS system notifications to your accessory using [`Accessory Notifications`](https://developer.apple.com/documentation/AccessoryNotifications).

For information about automatic routing of audio to accessories, see [`AudioAccessoryKit`](https://developer.apple.com/documentation/AudioAccessoryKit).

> ❗ **Important**: This framework is available only for iOS. The framework ignores calls for apps built with Mac Catalyst, and iOS apps that run on visionOS or on Macs with Apple silicon. You can develop and test an app that uses this framework on devices in any region. Customer installations of your app can only use the framework on devices located in the EU that are signed in with an Apple Account with an EU country or region.

#### Share a Wi Fi Network with an Accessory

Implement the [`AccessoryTransportAppExtension`](accessorytransportappextension.md) protocol in an extension to share Wi-Fi networks with your accessory. The system calls your extension’s [`accept(sessionRequest:)`](accessorytransportappextension/accept(sessionrequest:).md) method when it’s ready to start. After accepting the session request, your extension connects to the accessory using [`ASAccessorySession`](https://developer.apple.com/documentation/AccessorySetupKit/ASAccessorySession) and delivers Wi-Fi network data using [`WINetworkSharingProvider`](https://developer.apple.com/documentation/WiFiInfrastructure/WINetworkSharingProvider).

#### Forward Ios System Notifications to an Accessory

Using the Accessory Transport Extension framework with [`Accessory Notifications`](https://developer.apple.com/documentation/AccessoryNotifications), your app can receive iOS system notifications to send alerts to people on a connected accessory that you develop. The workflow requires three extensions to maintain security and encapsulation. Implement [`AccessoryDataProvider`](accessorydataprovider.md) to receive and curate the content of a given notification. The system encrypts the notification data using keys you provide in your [`AccessoryTransportSecurity`](accessorytransportsecurity.md) extension. Then, the system delivers the encrypted data to your [`AccessoryTransportAppExtension`](accessorytransportappextension.md) for transmission to the accessory. Your transport extension sends the encrypted data to your accessory, but is unable to decipher the notification’s content.

## Topics

### Essentials
- [com.apple.developer.accessory-transport-extension](../BundleResources/Entitlements/com.apple.developer.accessory-transport-extension.md)
  A Boolean value that indicates whether your app can exchange sensitive information with a connected accessory.
### Wi-Fi network sharing
- [protocol AccessoryTransportAppExtension](accessorytransportappextension.md)
  A protocol for an extension that transmits data to an accessory you develop.
- [protocol AccessoryTransportExtensionConfiguration](accessorytransportextensionconfiguration.md)
  An interface that enables you to configure and manage communication between your extension and the system.
- [class AccessoryTransportSession](accessorytransportsession.md)
  A class that manages a transport session between the extension and the system.
- [Wi-Fi Infrastructure](../WiFiInfrastructure/WiFiInfrastructure.md)
  Share Wi-Fi network credentials securely between devices and connected accessories.
### Notification forwarding
- [Receiving iOS notifications on an accessory](../AccessoryNotifications/receiving-ios-notifications-on-an-accessory.md)
  Create custom app extensions that manage notifications for your accessory.
- [protocol AccessoryDataProvider](accessorydataprovider.md)
  A protocol for an extension that receives iOS system notifications and curates their data for your accessory.
- [protocol AccessoryDataProviderConfiguration](accessorydataproviderconfiguration.md)
  A protocol that configures and manages communication between the extension and the system.
- [protocol AccessoryTransportSecurity](accessorytransportsecurity.md)
  A protocol for an extension that handles the cryptography of messages to your accessory.
- [protocol AccessoryTransportSecurityConfiguration](accessorytransportsecurityconfiguration.md)
  A protocol that configures and manages communication between your security extension and the system.
- [Accessory Notifications](../AccessoryNotifications/AccessoryNotifications.md)
  Receive forwarded iOS system notifications on an accessory that you develop.
### Data and sessions
- [protocol AccessoryFeature](accessoryfeature.md)
  A protocol that defines a capability for an accessory data provider extension.
- [protocol AccessoryFeatureSession](accessoryfeaturesession.md)
  A protocol that manages a session for a specific feature capability.
- [struct AccessoryMessage](accessorymessage.md)
  A structure that represents a message to send to an accessory.
- [class AccessorySecuritySession](accessorysecuritysession.md)
  A class that manages a security session between the extension and the system.
- [struct AccessorySecurity](accessorysecurity.md)
  Types of security events and cryptography operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AccessoryTransportExtension)*
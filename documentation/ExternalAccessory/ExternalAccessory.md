# External Accessory

**Framework**: Externalaccessory  
**Kind**: module

Communicate with accessories that connect to a device with the Apple Lightning connector, or with Bluetooth wireless technology.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

#### Overview

Use the External Accessory framework to set up and manage a connection to an MFi accessory your iOS app supports. The framework supports hardware that connects to an iOS or iPadOS device physically through an Apple Lightning or a 30-pin connector, or wirelessly with Bluetooth technology. The framework notifies your app when the accessory connects or disconnects from the user’s device. While connected, you communicate directly with the accessory using any hardware protocols the device supports.

> **Note**:  iPad and iPhone apps running on a Mac with Apple silicon can’t connect to external accessories using this framework. You may continue to link apps to this framework and run other features on Apple silicon.

The manufacturer of an MFi accessory decides which third-party apps may communicate with their accessories. If you’re developing an app, work with the manufacturer to obtain the information you need to communicate with their hardware. For example, obtain the specifications for the communication protocols the device supports.

For more information about how to connect to external accessories, see [`External Accessory Programming Topics`](https://developer.apple.comhttps://developer.apple.com/library/archive/featuredarticles/ExternalAccessoryPT/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009502).

## Topics

### Essentials
- [UISupportedExternalAccessoryProtocols](../BundleResources/Information-Property-List/UISupportedExternalAccessoryProtocols.md)
  The protocols that the app uses to communicate with external accessory hardware.
- [class EAAccessoryManager](eaaccessorymanager.md)
  The object you use to identify connected accessories, and begin delivery of connection and disconnection notifications.
### Accessory Communication
- [class EAAccessory](eaaccessory.md)
  An object that contains information about a single, connected hardware accessory.
- [class EASession](easession.md)
  The object you use to manage communications between your app and a connected hardware accessory.
### Wi-Fi Accessory Configuration
- [Wireless Accessory Configuration Entitlement](../BundleResources/Entitlements/com.apple.external-accessory.wireless-configuration.md)
  A Boolean value that indicates whether your app may configure MFi Wi-Fi accessories.
- [class EAWiFiUnconfiguredAccessoryBrowser](eawifiunconfiguredaccessorybrowser.md)
  An object you use to scan for wireless accessories and configure them for use with the user’s app.
- [class EAWiFiUnconfiguredAccessory](eawifiunconfiguredaccessory.md)
  An object that provides information about an unconfigured MFi Wireless Accessory Configuration accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ExternalAccessory)*
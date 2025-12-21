# AccessoryTransportExtension

**Framework**: AccessoryTransportExtension  
**Kind**: module

Exchange sensitive information with a connected accessory.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+

#### Overview

Use the Accessory Transport Extension framework to send sensitive information to accessories you’ve discovered and set up with [`AccessorySetupKit`](https://developer.apple.com/documentation/AccessorySetupKit). You can use the [`Wi-Fi Infrastructure`](https://developer.apple.com/documentation/WiFiInfrastructure) framework if you need to share a WiFi network to the accessory.

> **Note**: The Accessory Transport Extension framework is available for iOS. For apps built with Catalyst for macOS, and for iOS apps running on visionOS or on Mac computers with Apple silicon, calls to the framework do nothing.

You implement this functionality in an app extension that conforms to the [`AccessoryTransportAppExtension`](accessorytransportappextension.md) protocol. To add an accessory transport app extension, select your project from the Xcode project navigator, create a new target with File > New > Target, and choose the “Accessory Transport” template.

The framework calls your extension’s [`accept(sessionRequest:)`](accessorytransportappextension/accept(sessionrequest:).md) method when the accessory is ready to begin a transport session. Implement this method to inspect the received [`AccessoryTransportSession.Request`](accessorytransportsession/request.md) and then call [`accept(_:)`](accessorytransportsession/request/accept(_:).md) or [`reject(error:)`](accessorytransportsession/request/reject(error:).md) on the request.

After you accept a session from an accessory, your extension is responsible for directly connecting to the accessory and delivering data to it. The code included in the Accessory Transport template provides an event handler that creates an [`ASAccessorySession`](https://developer.apple.com/documentation/AccessorySetupKit/ASAccessorySession) and responds to accessory activation by setting up a [`WINetworkSharingProvider`](https://developer.apple.com/documentation/WiFiInfrastructure/WINetworkSharingProvider) for the accessory. You can use this to send data to the accessory.

> ❗ **Important**: You may develop and test Accessory Transport Extension apps on devices in all regions. People using your app must have an account registered in the European Union (EU), and their device must be located within the EU.

## Topics

### Essentials
- [com.apple.developer.accessory-transport-extension](../BundleResources/Entitlements/com.apple.developer.accessory-transport-extension.md)
  A Boolean value that indicates whether your app can exchange sensitive information with a connected accessory.
### App extensions
- [protocol AccessoryTransportAppExtension](accessorytransportappextension.md)
  A protocol that defines the behavior of the app extension and how it handles requests.
- [protocol AccessoryTransportExtensionConfiguration](accessorytransportextensionconfiguration.md)
  An interface you use to configure and manage communication between the extension and the host process.
### Transport sessions
- [class AccessoryTransportSession](accessorytransportsession.md)
  A class that manages a session between the extension and host process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AccessoryTransportExtension)*
# DeviceDiscoveryUI

**Framework**: DeviceDiscoveryUI  
**Kind**: module

Display an interface that lets people connect iOS, iPadOS, tvOS, watchOS, and Mac Catalyst apps over peer-to-peer networks.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 16.0+

#### Overview

The DeviceDiscoveryUI framework provides a secure, encrypted pairing mechanism to enable communications between your iOS, iPadOS, tvOS, watchOS, and Mac Catalyst apps, or between apps and accessories using peer-to-peer networks. For example, someone might control a tvOS game from their iPad or Apple Watch with  [`NSApplicationServices`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsapplicationservices) and a connection using the Network framework’s [`NWListener`](https://developer.apple.com/documentation/network/nwlistener), or a file-sharing app might connect two iOS devices– or an iOS device and an accessory – without a direct internet connection using a fully peer-to-peer network through [`Wi-Fi Aware`](https://developer.apple.com/documentation/wifiaware).

The DeviceDiscoveryUI and AccessorySetupKit frameworks enable wireless pairing between apps, and between apps and devices. Use DeviceDiscoveryUI to enable pairing from app to app and from apps to another device; the framework supports pairing with Apple and third-party devices. For pairing to enable the setup of hardware devices, use the AccessorySetupKit framework. It provides capabilities that help accessory makers to enable people to onboard and set up accessories quickly. For more information, see [`AccessorySetupKit`](https://developer.apple.com/documentation/accessorysetupkit).

#### Describe Your Service and Present the Pairing Interface

To create an app-to-app or app-to-device connection, start by defining the services your app provides. The following example shows how to describe a named network service an app provides — the *publisher* — and demonstrates how to use a [`DevicePairingView`](devicepairingview.md)  to present a pairing interface using SwiftUI that waits for a peer or *subscriber*.

```swift
    import DeviceDiscoveryUI
    import WiFiAware
    import SwiftUI

    // Check the device supports Wi-Fi Aware.
    guard WACapabilities.supportedFeatures.contains(.wifiAware) else { return }

    // Define the publishable service, such as a file service, that you declared 
    // in your app's Information Property List. This example shows a single service, 
    // but your app can publish multiple services simultaneously.
    extension WAPublishableService {
        public static var fileService: WAPublishableService {
            allServices["_file-service._tcp"]!
        }
    }

    // Invoke Listener UI that waits for client connections.
    DevicePairingView(.wifiAware(.connecting(to: .fileService, from: .selected([])))) {
        // Provide a view to display before launching System UI.
    } fallback: {
        // Provide a view in case of error.
    }
```

In the client, use DeviceDiscoveryUI to present a view that lists available devices, and then use the [`Network`](https://developer.apple.com/documentation/network) or [`Wi-Fi Aware`](https://developer.apple.com/documentation/wifiaware) frameworks to create the listeners and the connections, and to send and receive messages. The following example shows how to configure the client or *subscriber* app to browse for a published service.

This view displays a list of all the devices to which your app can connect, or app-to-app connections using Wi-Fi Aware that provide the specified service.

```swift
    // Check if the device supports Wi-Fi Aware.
    guard WACapabilities.supportedFeatures.contains(.wifiAware) else { return }

    // A service that an app can subscribe to that you declared in your app's 
    // Information Property List.
    // This example shows a single service, but your app can subscribe to 
    // multiple services simultaneously.
    extension WASubscribableService {
        public static var fileService: WASubscribableService {
            allServices["_file-service._tcp"]!
        }

    // Show device browser UI.
    DevicePicker(.wifiAware(.connecting(to: .selected([]), from: .fileService))) { endpoint in
        // Processes the paired network endpoint.
    } label: {
        // Provides a view to display before launching system UI.
    } fallback: {
        // Provide a view in case of error.
    }    
```

DeviceDiscoveryUI provides several advantages over creating a connection using the [`Network`](https://developer.apple.com/documentation/network) framework directly. DeviceDiscoveryUI automatically sets up an optimized, encrypted connection between versions of your app running on different devices. It helps preserve people’s privacy by providing access to iOS, iPadOS, and watchOS devices only through secure peer-to-peer connections. Also, because the system securely manages the connection, people don’t need to authorize full access to their local network.

#### Plan for Apple Tv Specific Behavior

When using DeviceDiscoveryUI with Apple TV, the following requirements apply:

- In tvOS, DeviceDiscoveryUI supports only AppleTV 4K, and only using the application service that uses [`NSApplicationServices`](https://developer.apple.com/documentation/bundleresources/information-property-list/nsapplicationservices) keys and the Network framework’s [`NWListener`](https://developer.apple.com/documentation/network/nwlistener), not [`Wi-Fi Aware`](https://developer.apple.com/documentation/wifiaware) to define the application services for your app.
- Your tvOS app can connect to only one device at a time.
- Your tvOS app can only connect to other copies of your app running on iOS, iPadOS, or watchOS.
- You must distribute your app as a universal purchase, so that all copies of your app share the same bundle ID. For more information, see [`Offering Universal Purchase`](https://developer.apple.comhttps://developer.apple.com/support/universal-purchase/).

When someone selects a device, the system attempts to launch your app on that device. If your app is already installed, the system asks the person using the app if they want to authorize a connection between the two devices through a pairing dialog. If your app isn’t installed, the system prompts the person to install it.

DeviceDiscoveryUI uses the iCloud account of the default account on Apple TV. If Apple TV has more than one account profile, the one that manages Family Sharing is the default. DeviceDiscoveryUI only shows devices logged into that person’s iCloud account, or accounts from the person’s Family Sharing group.

For more information on connecting tvOS apps to other devices, see [`Connecting a tvOS app to other devices over the local network`](connecting-a-tvos-app-to-other-devices-over-the-local-network.md).

## Topics

### Publishing service availability
- [Building peer-to-peer apps](../wifiaware/building-peer-to-peer-apps.md)
  Communicate with nearby devices over a secure, high-throughput, low-latency connection by using Wi-Fi Aware.
- [struct DevicePairingView](devicepairingview.md)
  A control that allows a user to become discoverable and advertise to local devices.
- [class DDDevicePairingViewController](dddevicepairingviewcontroller.md)
  A UIKit view that displays and manages the device discovery and pairing process.
- [struct DDDevicePairingAccess](dddevicepairingaccess.md)
  Specifies the access level requested for device discovery.
- [NSApplicationServices](../bundleresources/information-property-list/nsapplicationservices.md)
  A list of service providers and the devices that they support.
### Pairing with nearby devices
- [struct DevicePicker](devicepicker.md)
  A SwiftUI view that displays other devices on the network, and creates an encrypted connection to a copy of your app running on that device.
- [class DDDevicePickerViewController](dddevicepickerviewcontroller.md)
  A UIKit view that displays other devices on the network, and creates an encrypted connection to a copy of your app running on that device.
- [struct DevicePickerSupportedAction](devicepickersupportedaction.md)
  An environment value that indicates whether the current device supports device discovery.
- [Connecting a tvOS app to other devices over the local network](connecting-a-tvos-app-to-other-devices-over-the-local-network.md)
  Display a view in your tvOS app that lists available iOS, iPadOS, and watchOS devices that the user can connect to over their local network.

## See Also

- [Network](../network/network.md)
  Create network connections to send and receive data using transport and security protocols.
- [Wi-Fi Aware](../wifiaware/wifiaware.md)
  Securely pair and connect to external devices over peer-to-peer Wi-Fi.
- [AccessorySetupKit](../accessorysetupkit/accessorysetupkit.md)
  Enable privacy-preserving discovery and configuration of accessories.
- [Accessory Design Guidelines for Apple Devices](https://developer.apple.comhttps://developer.apple.com/accessories/Accessory-Design-Guidelines.pdf)


---

*[View on Apple Developer](https://developer.apple.com/documentation/DeviceDiscoveryUI)*
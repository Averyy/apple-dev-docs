# startDeviceDiscovery()

**Framework**: Media Device  
**Kind**: method  
**Required**: Yes

Called when a user action requires discovered devices to be displayed.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
func startDeviceDiscovery()
```

## Mentions

- [Creating a media device extension](creating-a-media-device-extension.md)

#### Discussion

Use the `Network`, `WiFiAware`, or `CoreBluetooth` frameworks for service discovery.

> **Note**: During discovery, your extension will have local area network access, to include direct connections over WiFiAware and Bluetooth. It will not be permitted to connect to the internet or addresses outside the local network.

As devices are found, report them to the system by calling [`foundDevice(_:)`](mediadeviceroutingmanager/founddevice(_:).md) on the routing manager. When a previously discovered device is no longer available, call [`lostDevice(_:)`](mediadeviceroutingmanager/lostdevice(_:).md). If discovery fails unexpectedly, call [`discoveryFailed(_:)`](mediadeviceroutingmanager/discoveryfailed(_:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediadeviceextension/startdevicediscovery())*
# init(displayName:category:protocolType:identifier:)

**Framework**: DeviceDiscoveryExtension  
**Kind**: init

Creates an object that describes a discovered device.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
init(displayName: String, category: DDDevice.Category, protocolType: UTType, identifier: String)
```

#### Discussion

As an example `identifier` for Bluetooth devices, your extension can use the device’s local name (see [`CBAdvertisementDataLocalNameKey`](https://developer.apple.com/documentation/CoreBluetooth/CBAdvertisementDataLocalNameKey)).

## Parameters

- `displayName`: A name for the device to display to the user.
- `category`: An option that determines the icon that the picker UI displays for the device.
- `protocolType`: A custom universal type that describes the device’s manner of communication with the extension.
- `identifier`: A unique identifier for the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddevice/init(displayname:category:protocoltype:identifier:))*
# identifier

**Framework**: DeviceDiscoveryExtension  
**Kind**: property

A unique identifier for the device.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
var identifier: String { get set }
```

#### Discussion

As an example [`identifier`](dddevice/identifier.md) for Bluetooth devices, your extension can use the device’s local name (see [`CBAdvertisementDataLocalNameKey`](https://developer.apple.com/documentation/CoreBluetooth/CBAdvertisementDataLocalNameKey)).

## See Also

- [var displayName: String](dddevice/displayname.md)
  A name for the device to display to the user.
- [var category: DDDevice.Category](dddevice/category-swift.property.md)
  An option that determies the icon that the picker UI displays for the device.
- [DDDevice.Category](dddevice/category-swift.enum.md)
  An option that determines the icon for the device in the picker UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddevice/identifier)*
# NSBluetoothAlwaysUsageDescription

**Framework**: Bundle Resources  
**Kind**: typealias

A message that tells the user why the app needs access to Bluetooth.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 11.0+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

#### Discussion

This key is required if your app uses the device’s Bluetooth interface.

> ❗ **Important**:  If your app has a deployment target earlier than iOS 13, add the [`NSBluetoothPeripheralUsageDescription`](information-property-list/nsbluetoothperipheralusagedescription.md) key to your app’s [`Information Property List`](information-property-list.md) file in addition to this key.

## See Also

- [NSBluetoothPeripheralUsageDescription](information-property-list/nsbluetoothperipheralusagedescription.md)
  A message that tells the user why the app is requesting the ability to connect to Bluetooth peripherals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsbluetoothalwaysusagedescription)*
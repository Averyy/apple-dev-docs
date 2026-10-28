# NSBluetoothPeripheralUsageDescription

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A message that tells people why the app is requesting the ability to connect to Bluetooth peripherals.

**Availability**:
- iOS 6.0+ - Deprecated in 13.0
- iPadOS 6.0+ - Deprecated in 13.0

## Details

- **Name**: `NSBluetoothPeripheralUsageDescription` (Privacy - Bluetooth Peripheral Usage Description)
- **Type**: string

## Discussion

For apps with a deployment target of iOS 13 and later, use [`NSBluetoothAlwaysUsageDescription`](./nsbluetoothalwaysusagedescription.md) instead.

For deployment targets earlier than iOS 13, add both [`NSBluetoothAlwaysUsageDescription`](./nsbluetoothalwaysusagedescription.md) and [`NSBluetoothPeripheralUsageDescription`](./nsbluetoothperipheralusagedescription.md) to your app’s [`Information Property List`](../information-property-list.md) file. Devices running earlier versions of iOS rely on [`NSBluetoothPeripheralUsageDescription`](./nsbluetoothperipheralusagedescription.md), while devices running later versions rely on [`NSBluetoothAlwaysUsageDescription`](./nsbluetoothalwaysusagedescription.md).

> ❗ **Important**:  This key is required if your app uses APIs that access Bluetooth peripherals and has a deployment target earlier than iOS 13.

## See Also

### Bluetooth
- [NSBluetoothAlwaysUsageDescription](./nsbluetoothalwaysusagedescription.md)
  A message that tells people why the app needs access to Bluetooth.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsbluetoothperipheralusagedescription)*
# NSAccessorySetupKitSupports

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

An array of strings that indicates the wireless technologies AccessorySetupKit uses when discovering and configuring accessories.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Details

- **Name**: `NSAccessorySetupKitSupports` (AccessorySetupKit - Supports)
- **Type**: array of string 

## Possible Values

- `Bluetooth`: Include this string if your app uses Bluetooth to set up accessories.
- `WiFi`: Include this string if your app uses Wi-Fi to set up accessories.

#### Discussion

If you use the `Bluetooth` value in your array, also add the following keys and values to your information property list:

- [`NSAccessorySetupBluetoothCompanyIdentifiers`](./nsaccessorysetupbluetoothcompanyidentifiers.md)
- [`NSAccessorySetupBluetoothNames`](./nsaccessorysetupbluetoothnames.md)
- [`NSAccessorySetupBluetoothServices`](./nsaccessorysetupbluetoothservices.md)

## See Also

### Accessories
- [NSAccessorySetupBluetoothCompanyIdentifiers](./nsaccessorysetupbluetoothcompanyidentifiers.md)
  An array of strings that represent the Bluetooth company identifiers for accessories that your app configures.
- [NSAccessorySetupBluetoothNames](./nsaccessorysetupbluetoothnames.md)
  An array of strings that represent the Bluetooth device names or substrings for accessories that your app configures.
- [NSAccessorySetupBluetoothServices](./nsaccessorysetupbluetoothservices.md)
  An array of strings that represent the hexadecimal values of Bluetooth SIG-defined services or custom services for accessories your app configures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsaccessorysetupkitsupports)*
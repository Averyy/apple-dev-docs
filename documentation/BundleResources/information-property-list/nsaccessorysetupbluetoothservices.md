# NSAccessorySetupBluetoothServices

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

An array of strings that represent the hexadecimal values of Bluetooth SIG-defined services or custom services for accessories your app configures.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Details

- **Name**: `NSAccessorySetupBluetoothServices` (AccessorySetupKit - Bluetooth Services)
- **Type**: array of string 

## Discussion

Each value is a 16- or 128-bit UUID that represents either a Bluetooth Special Interest Group (SIG)-registered service or a custom service.

## See Also

### Accessories
- [NSAccessorySetupKitSupports](./nsaccessorysetupkitsupports.md)
  An array of strings that indicates the wireless technologies AccessorySetupKit uses when discovering and configuring accessories.
- [NSAccessorySetupBluetoothCompanyIdentifiers](./nsaccessorysetupbluetoothcompanyidentifiers.md)
  An array of strings that represent the Bluetooth company identifiers for accessories that your app configures.
- [NSAccessorySetupBluetoothNames](./nsaccessorysetupbluetoothnames.md)
  An array of strings that represent the Bluetooth device names or substrings for accessories that your app configures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsaccessorysetupbluetoothservices)*
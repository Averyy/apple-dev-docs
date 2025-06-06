# CBCentralManagerScanOptionSolicitedServiceUUIDsKey

**Framework**: Core Bluetooth  
**Kind**: var

An array of service UUIDs that you want to scan for.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let CBCentralManagerScanOptionSolicitedServiceUUIDsKey: String
```

#### Discussion

The array is an instance of [`NSArray`](https://developer.apple.com/documentation/Foundation/NSArray), and uses [`CBUUID`](cbuuid.md) objects to represent the UUIDs to scan for.

Specifying this scan option causes the central manager to also scan for peripherals soliciting any of the services contained in the array.

## See Also

- [let CBCentralManagerScanOptionAllowDuplicatesKey: String](cbcentralmanagerscanoptionallowduplicateskey.md)
  A Boolean value that specifies whether the scan should run without duplicate filtering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerscanoptionsolicitedserviceuuidskey)*
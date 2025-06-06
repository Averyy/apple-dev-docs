# isScanning

**Framework**: Core Bluetooth  
**Kind**: property

A Boolean value that indicates whether the central is currently scanning.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isScanning: Bool { get }
```

## See Also

- [func scanForPeripherals(withServices: [CBUUID]?, options: [String : Any]?)](cbcentralmanager/scanforperipherals(withservices:options:).md)
  Scans for peripherals that are advertising services.
- [Peripheral Scanning Options](peripheral-scanning-options.md)
  Keys used to pass options when scanning for peripherals.
- [func stopScan()](cbcentralmanager/stopscan.md)
  Asks the central manager to stop scanning for peripherals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/isscanning)*
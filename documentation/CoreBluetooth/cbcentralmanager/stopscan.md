# stopScan()

**Framework**: Core Bluetooth  
**Kind**: method

Asks the central manager to stop scanning for peripherals.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func stopScan()
```

## See Also

- [func scanForPeripherals(withServices: [CBUUID]?, options: [String : Any]?)](cbcentralmanager/scanforperipherals(withservices:options:).md)
  Scans for peripherals that are advertising services.
- [Peripheral Scanning Options](peripheral-scanning-options.md)
  Keys used to pass options when scanning for peripherals.
- [var isScanning: Bool](cbcentralmanager/isscanning.md)
  A Boolean value that indicates whether the central is currently scanning.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/stopscan())*
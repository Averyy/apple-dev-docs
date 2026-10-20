# isScanning

**Framework**: Core Bluetooth  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, assign, readonly) BOOL isScanning;
```

## See Also

### Scanning or Stopping Scans of Peripherals
- [func scanForPeripherals(withServices: [CBUUID]?, options: [String : Any]?)](./scanforperipherals%28withservices,options%29.md)
  Scans for peripherals that are advertising services.
- [Peripheral Scanning Options](../peripheral-scanning-options.md)
  Keys used to pass options when scanning for peripherals.
- [func stopScan()](./stopscan%28%29.md)
  Asks the central manager to stop scanning for peripherals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/isscanning)*
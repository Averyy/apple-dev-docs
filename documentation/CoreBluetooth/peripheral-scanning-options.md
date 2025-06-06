# Peripheral Scanning Options

**Framework**: Core Bluetooth

Keys used to pass options when scanning for peripherals.

## Topics

### Constants
- [let CBCentralManagerScanOptionAllowDuplicatesKey: String](cbcentralmanagerscanoptionallowduplicateskey.md)
  A Boolean value that specifies whether the scan should run without duplicate filtering.
- [let CBCentralManagerScanOptionSolicitedServiceUUIDsKey: String](cbcentralmanagerscanoptionsolicitedserviceuuidskey.md)
  An array of service UUIDs that you want to scan for.

## See Also

- [func scanForPeripherals(withServices: [CBUUID]?, options: [String : Any]?)](cbcentralmanager/scanforperipherals(withservices:options:).md)
  Scans for peripherals that are advertising services.
- [func stopScan()](cbcentralmanager/stopscan.md)
  Asks the central manager to stop scanning for peripherals.
- [var isScanning: Bool](cbcentralmanager/isscanning.md)
  A Boolean value that indicates whether the central is currently scanning.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/peripheral-scanning-options)*
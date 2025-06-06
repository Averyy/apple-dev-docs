# scanForPeripherals(withServices:options:)

**Framework**: Core Bluetooth  
**Kind**: method

Scans for peripherals that are advertising services.

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
func scanForPeripherals(withServices serviceUUIDs: [CBUUID]?, options: [String : Any]? = nil)
```

#### Discussion

You can provide an array of [`CBUUID`](cbuuid.md) objects — representing service UUIDs — in the `serviceUUIDs` parameter. When you do, the central manager returns only peripherals that advertise the services you specify. If the `serviceUUIDs` parameter is `nil`, this method returns all discovered peripherals, regardless of their supported services.

> **Note**:  The recommended practice is to populate the `serviceUUIDs` parameter rather than leaving it `nil`.

 The recommended practice is to populate the `serviceUUIDs` parameter rather than leaving it `nil`.

If the central manager is actively scanning with one set of parameters and it receives another set to scan, the new parameters override the previous set. When the central manager discovers a peripheral, it calls the [`centralManager(_:didDiscover:advertisementData:rssi:)`](cbcentralmanagerdelegate/centralmanager(_:diddiscover:advertisementdata:rssi:).md) method of its delegate object.

Your app can scan for Bluetooth devices in the background by specifying the `bluetooth-central` background mode. To do this, your app must explicitly scan for one or more services by specifying them in the `serviceUUIDs` parameter. The [`CBCentralManager`](cbcentralmanager.md) scan option has no effect while scanning in the background.

## Parameters

- `serviceUUIDs`: An array of   objects that the app is interested in. Each   object represents the UUID of a service that a peripheral advertises.
- `options`: A dictionary of options for customizing the scan. For available options, see  .

## See Also

- [Peripheral Scanning Options](peripheral-scanning-options.md)
  Keys used to pass options when scanning for peripherals.
- [func stopScan()](cbcentralmanager/stopscan.md)
  Asks the central manager to stop scanning for peripherals.
- [var isScanning: Bool](cbcentralmanager/isscanning.md)
  A Boolean value that indicates whether the central is currently scanning.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/scanforperipherals(withservices:options:))*
# retrieveConnectedPeripherals(withServices:)

**Framework**: Core Bluetooth  
**Kind**: method

Returns a list of the peripherals connected to the system whose services match a given set of criteria.

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
func retrieveConnectedPeripherals(withServices serviceUUIDs: [CBUUID]) -> [CBPeripheral]
```

#### Return Value

A list of the peripherals that are currently connected to the system and that contain any of the services specified in the `serviceUUID` parameter.

#### Discussion

The list of connected peripherals can include those that other apps have connected. You need to connect these peripherals locally using the [`connect(_:options:)`](cbcentralmanager/connect(_:options:).md) method before using them.

## Parameters

- `serviceUUIDs`: A list of service UUIDs, represented by   objects.

## See Also

- [func retrievePeripherals(withIdentifiers: [UUID]) -> [CBPeripheral]](cbcentralmanager/retrieveperipherals(withidentifiers:).md)
  Returns a list of known peripherals by their identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/retrieveconnectedperipherals(withservices:))*
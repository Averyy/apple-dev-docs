# retrievePeripherals(withIdentifiers:)

**Framework**: Core Bluetooth  
**Kind**: method

Returns a list of known peripherals by their identifiers.

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
func retrievePeripherals(withIdentifiers identifiers: [UUID]) -> [CBPeripheral]
```

#### Return Value

A list of peripherals that the central manager is able to match to the provided identifiers.

## Parameters

- `identifiers`: A list of peripheral identifiers (represented by   objects) from which   objects can be retrieved.

## See Also

- [func retrieveConnectedPeripherals(withServices: [CBUUID]) -> [CBPeripheral]](cbcentralmanager/retrieveconnectedperipherals(withservices:).md)
  Returns a list of the peripherals connected to the system whose services match a given set of criteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/retrieveperipherals(withidentifiers:))*
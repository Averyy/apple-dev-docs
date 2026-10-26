# init(bluetoothIdentifier:iAP2Identifier:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a head unit object with the specified Bluetooth and iAP2 identifiers.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(bluetoothIdentifier: String?, iAP2Identifier: String?)
```

```objc
- (instancetype) initWithBluetoothIdentifier:(NSString *) bluetoothIdentifier iAP2Identifier:(NSString *) iAP2Identifier;
```

#### Discussion

The system uses these identifiers to match a vehicle in the user’s My Vehicles collection with its physical counterpart. You can’t change these values after initialization.

## Parameters

- `bluetoothIdentifier`: The Bluetooth identifier of the vehicle’s physical head unit.
- `iAP2Identifier`: The iAP2 identifier of the vehicle’s physical head unit. This is the same value as the external accessory’s [`serialNumber`](../../../ExternalAccessory/eaaccessory/serialnumber.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incar/headunit-swift.class/init(bluetoothidentifier:iap2identifier:))*
# serviceUUIDs

**Framework**: Core Bluetooth  
**Kind**: property  
**Role**: Type Property

An array that represents service identifiers to match.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static let serviceUUIDs: CBConnectionEventMatchingOption
```

```c
extern CBConnectionEventMatchingOption const CBConnectionEventMatchingOptionServiceUUIDs;
```

#### Discussion

A connected peer with any matching service UUIDs results in a call to [`centralManager(_:connectionEventDidOccur:for:)`](../cbcentralmanagerdelegate/centralmanager%28_,connectioneventdidoccur,for%29.md).

## See Also

### Matching Options
- [static let peripheralUUIDs: CBConnectionEventMatchingOption](./peripheraluuids.md)
  An array of UUID objects that represents peripherals to match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbconnectioneventmatchingoption/serviceuuids)*
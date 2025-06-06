# peripheralUUIDs

**Framework**: Core Bluetooth  
**Kind**: property

An array of UUID objects that represents peripherals to match.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static let peripheralUUIDs: CBConnectionEventMatchingOption
```

#### Discussion

A connected peer with any matching peripheral UUIDs results in a call to [`centralManager(_:connectionEventDidOccur:for:)`](cbcentralmanagerdelegate/centralmanager(_:connectioneventdidoccur:for:).md).

## See Also

- [static let serviceUUIDs: CBConnectionEventMatchingOption](cbconnectioneventmatchingoption/serviceuuids.md)
  An array that represents service identifiers to match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbconnectioneventmatchingoption/peripheraluuids)*
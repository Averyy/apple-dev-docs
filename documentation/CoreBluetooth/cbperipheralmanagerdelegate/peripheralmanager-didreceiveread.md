# peripheralManager(_:didReceiveRead:)

**Framework**: Core Bluetooth  
**Kind**: method

Tells the delegate that a local peripheral received an Attribute Protocol (ATT) read request for a characteristic with a dynamic value.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func peripheralManager(_ peripheral: CBPeripheralManager, didReceiveRead request: CBATTRequest)
```

#### Discussion

When you receive this callback, call the [`respond(to:withResult:)`](cbperipheralmanager/respond(to:withresult:).md) method of the [`CBPeripheralManager`](cbperipheralmanager.md) class exactly once to respond to the read request.

## Parameters

- `peripheral`: The peripheral manager that received the request.
- `request`: A   object that represents a request to read a characteristic’s value.

## See Also

- [func peripheralManager(CBPeripheralManager, didReceiveWrite: [CBATTRequest])](cbperipheralmanagerdelegate/peripheralmanager(_:didreceivewrite:).md)
  Tells the delegate that a local peripheral device received an Attribute Protocol (ATT) write request for a characteristic with a dynamic value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/peripheralmanager(_:didreceiveread:))*
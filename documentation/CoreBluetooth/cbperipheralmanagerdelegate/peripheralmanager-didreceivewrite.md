# peripheralManager(_:didReceiveWrite:)

**Framework**: Core Bluetooth  
**Kind**: method

Tells the delegate that a local peripheral device received an Attribute Protocol (ATT) write request for a characteristic with a dynamic value.

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
optional func peripheralManager(_ peripheral: CBPeripheralManager, didReceiveWrite requests: [CBATTRequest])
```

#### Discussion

In the same way that you respond to a read request, each time you receive this callback, call the [`respond(to:withResult:)`](cbperipheralmanager/respond(to:withresult:).md) method of the [`CBPeripheralManager`](cbperipheralmanager.md) class exactly once. If the `requests` parameter contains multiple requests, treat them as you would a single request—if you can’t fulfill an individual request, you shouldn’t fulfill any of them. Instead, call the [`respond(to:withResult:)`](cbperipheralmanager/respond(to:withresult:).md) method immediately, and provide a result that indicates the cause of the failure.

When you respond to a write request, note that the first parameter of the [`respond(to:withResult:)`](cbperipheralmanager/respond(to:withresult:).md) method expects a single [`CBATTRequest`](cbattrequest.md) object, even though you received an array of them from the [`peripheralManager(_:didReceiveWrite:)`](cbperipheralmanagerdelegate/peripheralmanager(_:didreceivewrite:).md) method. To respond properly, pass in the first request of the `requests` array.

## Parameters

- `peripheral`: The peripheral manager that received the request.
- `requests`: A list of one or more   objects, each representing a request to write the value of a characteristic.

## See Also

- [func peripheralManager(CBPeripheralManager, didReceiveRead: CBATTRequest)](cbperipheralmanagerdelegate/peripheralmanager(_:didreceiveread:).md)
  Tells the delegate that a local peripheral received an Attribute Protocol (ATT) read request for a characteristic with a dynamic value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/peripheralmanager(_:didreceivewrite:))*
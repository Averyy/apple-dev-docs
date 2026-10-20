# respond(to:withResult:)

**Framework**: Core Bluetooth  
**Kind**: method  
**Role**: Instance Method

Responds to a read or write request from a connected central.

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
func respond(to request: CBATTRequest, withResult result: CBATTError.Code)
```

```objc
- (void) respondToRequest:(CBATTRequest *) request withResult:(CBATTError) result;
```

#### Discussion

When the peripheral manager receives a request from a connected central to read or write a characteristic’s value, it calls the [`peripheralManager(_:didReceiveRead:)`](../cbperipheralmanagerdelegate/peripheralmanager%28_,didreceiveread%29.md) or [`peripheralManager(_:didReceiveWrite:)`](../cbperipheralmanagerdelegate/peripheralmanager%28_,didreceivewrite%29.md) method of its delegate object. To respond to the corresponding read or write request, you call this method whenever you recevie one of these delegate method callbacks.

## Parameters

- `request`: The read or write request received from the connected central. For more information about read and write requests, see [`CBATTRequest`](../cbattrequest.md).
- `result`: The result of attempting to fulfill the request. For a list of possible results, see [Deprecated Constants](../deprecated-constants.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/respond(to:withresult:))*
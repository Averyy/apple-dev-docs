# peripheralManagerDidStartAdvertising(_:error:)

**Framework**: Core Bluetooth  
**Kind**: method  
**Role**: Instance Method

Tells the delegate the peripheral manager started advertising the local peripheral device’s data.

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
optional func peripheralManagerDidStartAdvertising(_ peripheral: CBPeripheralManager, error: (any Error)?)
```

```objc
- (void) peripheralManagerDidStartAdvertising:(CBPeripheralManager *) peripheral error:(NSError *) error;
```

#### Discussion

Core Bluetooth calls this method when your app calls the [`startAdvertising(_:)`](../cbperipheralmanager/startadvertising%28_%29.md) method to advertise the local peripheral device’s data. If successful, the `error` parameter is `nil`. If a problem prevents advertising the data, the `error` parameter returns the cause of the failure.

## Parameters

- `peripheral`: The peripheral manager that is starting advertising.
- `error`: The reason the call failed, or `nil` if no error occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/peripheralmanagerdidstartadvertising(_:error:))*
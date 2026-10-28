# add(_:)

**Framework**: Core Bluetooth  
**Kind**: method  
**Role**: Instance Method

Publishes a service and any of its associated characteristics and characteristic descriptors to the local GATT database.

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
func add(_ service: CBMutableService)
```

```objc
- (void) addService:(CBMutableService *) service;
```

## Discussion

When you add a service to the database, the peripheral manager calls the [`peripheralManager(_:didAdd:error:)`](../cbperipheralmanagerdelegate/peripheralmanager%28_,didadd,error%29.md) method of its delegate object. If the service contains any included services, you must first publish them.

## Parameters

- `service`: The service you want to publish.

## See Also

### Adding and Removing Services
- [func remove(CBMutableService)](./remove%28_%29.md)
  Removes a specified published service from the local GATT database.
- [func removeAllServices()](./removeallservices%28%29.md)
  Removes all published services from the local GATT database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/add(_:))*
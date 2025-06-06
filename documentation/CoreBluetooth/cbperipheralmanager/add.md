# add(_:)

**Framework**: Core Bluetooth  
**Kind**: method

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

#### Discussion

When you add a service to the database, the peripheral manager calls the [`peripheralManager(_:didAdd:error:)`](cbperipheralmanagerdelegate/peripheralmanager(_:didadd:error:).md) method of its delegate object. If the service contains any included services, you must first publish them.

## Parameters

- `service`: The service you want to publish.

## See Also

- [func remove(CBMutableService)](cbperipheralmanager/remove(_:).md)
  Removes a specified published service from the local GATT database.
- [func removeAllServices()](cbperipheralmanager/removeallservices.md)
  Removes all published services from the local GATT database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/add(_:))*
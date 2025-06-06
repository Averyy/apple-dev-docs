# remove(_:)

**Framework**: Core Bluetooth  
**Kind**: method

Removes a specified published service from the local GATT database.

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
func remove(_ service: CBMutableService)
```

#### Discussion

Because apps on the local peripheral device share the GATT database, more than one instance of a service may exist in the database. As a result, this method removes only the instance of the service that your app added to the database (using the [`add(_:)`](cbperipheralmanager/add(_:).md) method). If any other services contains this service, you must first remove them.

## Parameters

- `service`: The service you want to remove.

## See Also

- [func add(CBMutableService)](cbperipheralmanager/add(_:).md)
  Publishes a service and any of its associated characteristics and characteristic descriptors to the local GATT database.
- [func removeAllServices()](cbperipheralmanager/removeallservices.md)
  Removes all published services from the local GATT database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/remove(_:))*
# init(type:properties:value:permissions:)

**Framework**: Core Bluetooth  
**Kind**: init

Creates a mutable characteristic with specified permissions, properties, and value.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+

## Declaration

```swift
init(type UUID: CBUUID, properties: CBCharacteristicProperties, value: Data?, permissions: CBAttributePermissions)
```

#### Return Value

A newly initialized mutable characteristic.

#### Discussion

If you specify a value for the characteristic, the characteristic caches the value and sets its properties and permissions to [`read`](cbcharacteristicproperties/read.md) and [`readable`](cbattributepermissions/readable.md), respectively. Therefore, if you need the value of a characteristic to be writeable, or if you expect the value to change during the lifetime of the published service to which the characteristic belongs, you must specify the value as `nil`. This ensures that the characteristic treats the value dynamically. With a dynamic value, the peripheral manager requests the value whenever the peripheral manager receives a read or write request from a central. The peripheral does this by calling the [`peripheralManager(_:didReceiveRead:)`](cbperipheralmanagerdelegate/peripheralmanager(_:didreceiveread:).md) and [`peripheralManager(_:didReceiveWrite:)`](cbperipheralmanagerdelegate/peripheralmanager(_:didreceivewrite:).md) methods of its delegate object, respectively.

For more information, see [`Core Bluetooth Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/CoreBluetooth_concepts/AboutCoreBluetooth/Introduction.html#//apple_ref/doc/uid/TP40013257).

## Parameters

- `UUID`: A 128-bit UUID that identifies the characteristic.
- `properties`: The properties of the characteristic.
- `value`: The characteristic value to cache. If  , the value is dynamic and the peripheral manager fetches it on demand.
- `permissions`: The permissions of the characteristic value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbmutablecharacteristic/init(type:properties:value:permissions:))*
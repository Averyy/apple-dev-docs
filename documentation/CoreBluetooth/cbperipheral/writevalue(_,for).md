# writeValue(_:for:)

**Framework**: Core Bluetooth  
**Kind**: method  
**Role**: Instance Method

Writes the value of a characteristic descriptor.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func writeValue(_ data: Data, for descriptor: CBDescriptor)
```

```objc
- (void) writeValue:(NSData *) data forDescriptor:(CBDescriptor *) descriptor;
```

## Discussion

When you call this method to write the value of a characteristic descriptor, the peripheral calls the [`peripheral(_:didWriteValueFor:error:)`](../cbperipheraldelegate/peripheral%28_,didwritevaluefor,error%29-1ybl3.md) method of its delegate object.

This method copies the `data` passed into the data parameter, and you can dispose of it after the method returns.

You can’t use this method to write the value of a client configuration descriptor (represented by the [`CBUUIDClientCharacteristicConfigurationString`](../cbuuidclientcharacteristicconfigurationstring.md) constant), which describes the configuration of notification or indications for a characteristic’s value. If you want to manage notifications or indications for a characteristic’s value, you must use the [`setNotifyValue(_:for:)`](./setnotifyvalue%28_,for%29.md) method instead.

## Parameters

- `data`: The value to write.
- `descriptor`: The descriptor containing the value to write.

## See Also

### Writing Characteristic and Descriptor Values
- [func writeValue(Data, for: CBCharacteristic, type: CBCharacteristicWriteType)](./writevalue%28_,for,type%29.md)
  Writes the value of a characteristic.
- [func maximumWriteValueLength(for: CBCharacteristicWriteType) -> Int](./maximumwritevaluelength%28for%29.md)
  The maximum amount of data, in bytes, you can send to a characteristic in a single write type.
- [enum CBCharacteristicWriteType](../cbcharacteristicwritetype.md)
  Values representing the possible write types to a characteristic’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheral/writevalue(_:for:))*
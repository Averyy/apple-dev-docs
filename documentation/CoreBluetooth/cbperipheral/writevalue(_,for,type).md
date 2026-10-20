# writeValue(_:for:type:)

**Framework**: Core Bluetooth  
**Kind**: method  
**Role**: Instance Method

Writes the value of a characteristic.

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
func writeValue(_ data: Data, for characteristic: CBCharacteristic, type: CBCharacteristicWriteType)
```

```objc
- (void) writeValue:(NSData *) data forCharacteristic:(CBCharacteristic *) characteristic type:(CBCharacteristicWriteType) type;
```

#### Discussion

When you call this method to write the value of a characteristic, the peripheral calls the [`peripheral(_:didWriteValueFor:error:)`](../cbperipheraldelegate/peripheral%28_,didwritevaluefor,error%29-4f5ea.md) method of its delegate object only if you specified the write type as [`CBCharacteristicWriteType.withResponse`](../cbcharacteristicwritetype/withresponse.md). The response you receive through the [`peripheral(_:didWriteValueFor:error:)`](../cbperipheraldelegate/peripheral%28_,didwritevaluefor,error%29-4f5ea.md) delegate method indicates whether the write was successful; if the write failed, it details the cause of the failure in an error.

On the other hand, if you specify the write type as [`CBCharacteristicWriteType.withoutResponse`](../cbcharacteristicwritetype/withoutresponse.md), Core Bluetooth attempts to write the value but doesn’t guarantee success. If the write doesn’t succeed in this case, you aren’t notified and you don’t receive an error indicating the cause of the failure.

Use the [`write`](../cbcharacteristicproperties/write.md) and [`writeWithoutResponse`](../cbcharacteristicproperties/writewithoutresponse.md) members of the characteristic’s [`properties`](../cbcharacteristic/properties.md) enumeration to determine which kinds of writes you can perform.

This method copies the data passed into the `data` parameter, and you can dispose of it after the method returns.

## Parameters

- `data`: The value to write.
- `characteristic`: The characteristic containing the value to write.
- `type`: The type of write to execute. For a list of the possible types of writes to a characteristic’s value, see [`CBCharacteristicWriteType`](../cbcharacteristicwritetype.md).

## See Also

### Writing Characteristic and Descriptor Values
- [func writeValue(Data, for: CBDescriptor)](./writevalue%28_,for%29.md)
  Writes the value of a characteristic descriptor.
- [func maximumWriteValueLength(for: CBCharacteristicWriteType) -> Int](./maximumwritevaluelength%28for%29.md)
  The maximum amount of data, in bytes, you can send to a characteristic in a single write type.
- [enum CBCharacteristicWriteType](../cbcharacteristicwritetype.md)
  Values representing the possible write types to a characteristic’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheral/writevalue(_:for:type:))*
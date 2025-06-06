# readValue(for:)

**Framework**: Core Bluetooth  
**Kind**: method

Retrieves the value of a specified characteristic.

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
func readValue(for characteristic: CBCharacteristic)
```

#### Discussion

When you call this method to read the value of a characteristic, the peripheral calls the [`peripheral(_:didUpdateValueFor:error:)`](cbperipheraldelegate/peripheral(_:didupdatevaluefor:error:)-1xyna.md) method of its delegate object. If the peripheral successfully reads the value of the characteristic, you can access it through the characteristic’s [`value`](cbcharacteristic/value.md) property.

Not all characteristics have a readable value. You can determine whether a characteristic’s value is readable by accessing the relevant properties of the [`CBCharacteristicProperties`](cbcharacteristicproperties.md) enumeration.

## Parameters

- `characteristic`: The characteristic whose value you want to read.

## See Also

- [func readValue(for: CBDescriptor)](cbperipheral/readvalue(for:)-91hhp.md)
  Retrieves the value of a specified characteristic descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheral/readvalue(for:)-6u2kr)*
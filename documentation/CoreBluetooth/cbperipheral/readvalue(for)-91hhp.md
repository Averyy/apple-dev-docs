# readValue(for:)

**Framework**: Core Bluetooth  
**Kind**: method  
**Role**: Instance Method

Retrieves the value of a specified characteristic descriptor.

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
func readValue(for descriptor: CBDescriptor)
```

```objc
- (void) readValueForDescriptor:(CBDescriptor *) descriptor;
```

#### Discussion

When you call this method to read the value of a characteristic descriptor, the peripheral calls the [`peripheral(_:didUpdateValueFor:error:)`](../cbperipheraldelegate/peripheral%28_,didupdatevaluefor,error%29-1t3wm.md) method of its delegate object. If the peripheral successfully retrieves the value of the characteristic descriptor, you can access it through the characteristic descriptor’s [`value`](../cbdescriptor/value.md) property.

## Parameters

- `descriptor`: The characteristic descriptor whose value you want to read.

## See Also

### Reading Characteristic and Descriptor Values
- [func readValue(for: CBCharacteristic)](./readvalue%28for%29-6u2kr.md)
  Retrieves the value of a specified characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheral/readvalue(for:)-91hhp)*
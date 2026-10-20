# name

**Framework**: Core Bluetooth  
**Kind**: property  
**Role**: Instance Property

The name of the peripheral.

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
var name: String? { get }
```

```objc
@property (retain, readonly, nullable) NSString * name;
```

#### Discussion

Use this property to retrieve a human-readable name of the peripheral. A peripheral may have two different name types: one that the device advertises and another that the device publishes in its database as its Bluetooth low energy Generic Access Profile (GAP) device name. If a peripheral has both types of names, this property returns its GAP device name.

## Topics

### Related Documentation
- [func peripheralDidUpdateName(CBPeripheral)](../cbperipheraldelegate/peripheraldidupdatename%28_%29.md)
  Tells the delegate that a peripheral’s name changed.

## See Also

### Identifying a Peripheral
- [var delegate: (any CBPeripheralDelegate)?](./delegate.md)
  The delegate object specified to receive peripheral events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheral/name)*
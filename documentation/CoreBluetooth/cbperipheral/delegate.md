# delegate

**Framework**: Core Bluetooth  
**Kind**: property

The delegate object specified to receive peripheral events.

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
weak var delegate: (any CBPeripheralDelegate)? { get set }
```

#### Discussion

For information about how to implement your peripheral delegate, see [`CBPeripheralDelegate`](cbperipheraldelegate.md).

## See Also

- [var name: String?](cbperipheral/name.md)
  The name of the peripheral.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheral/delegate)*
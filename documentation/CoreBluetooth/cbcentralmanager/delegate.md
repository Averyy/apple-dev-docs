# delegate

**Framework**: Core Bluetooth  
**Kind**: property

The delegate object that you want to receive central manager events.

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
weak var delegate: (any CBCentralManagerDelegate)? { get set }
```

#### Discussion

For information about how to implement your central manager delegate, see [`CBCentralManagerDelegate`](cbcentralmanagerdelegate.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/delegate)*
# init()

**Framework**: Core Bluetooth  
**Kind**: init

Initializes the peripheral manager without a delegate.

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
convenience init()
```

## See Also

- [convenience init(delegate: (any CBPeripheralManagerDelegate)?, queue: dispatch_queue_t?)](cbperipheralmanager/init(delegate:queue:).md)
  Initializes the peripheral manager with a specified delegate and dispatch queue.
- [init(delegate: (any CBPeripheralManagerDelegate)?, queue: dispatch_queue_t?, options: [String : Any]?)](cbperipheralmanager/init(delegate:queue:options:).md)
  Initializes the peripheral manager with a specified delegate, dispatch queue, and initialization options.
- [var delegate: (any CBPeripheralManagerDelegate)?](cbperipheralmanager/delegate.md)
  The delegate object specified to receive peripheral events.
- [Peripheral Manager Initialization Options](peripheral-manager-initialization-options.md)
  Keys used to specify options when creating a peripheral manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/init())*
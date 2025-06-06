# init(delegate:queue:options:)

**Framework**: Core Bluetooth  
**Kind**: init

Initializes the peripheral manager with a specified delegate, dispatch queue, and initialization options.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+

## Declaration

```swift
init(delegate: (any CBPeripheralManagerDelegate)?, queue: dispatch_queue_t?, options: [String : Any]? = nil)
```

#### Return Value

Returns a newly initialized peripheral manager.

#### Discussion

This method is the designated initializer for the [`CBPeripheralManager`](cbperipheralmanager.md) class.

## Parameters

- `delegate`: The delegate to receive the peripheral role events.
- `queue`: The dispatch queue for dispatching the peripheral role events. If the value is  , the peripheral manager dispatches peripheral role events using the main queue.
- `options`: An optional dictionary containing initialization options for a peripheral manager. For available options, see  .

## See Also

- [convenience init()](cbperipheralmanager/init.md)
  Initializes the peripheral manager without a delegate.
- [convenience init(delegate: (any CBPeripheralManagerDelegate)?, queue: dispatch_queue_t?)](cbperipheralmanager/init(delegate:queue:).md)
  Initializes the peripheral manager with a specified delegate and dispatch queue.
- [var delegate: (any CBPeripheralManagerDelegate)?](cbperipheralmanager/delegate.md)
  The delegate object specified to receive peripheral events.
- [Peripheral Manager Initialization Options](peripheral-manager-initialization-options.md)
  Keys used to specify options when creating a peripheral manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/init(delegate:queue:options:))*
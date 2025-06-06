# init(delegate:queue:)

**Framework**: Core Bluetooth  
**Kind**: init

Initializes the peripheral manager with a specified delegate and dispatch queue.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+

## Declaration

```swift
convenience init(delegate: (any CBPeripheralManagerDelegate)?, queue: dispatch_queue_t?)
```

#### Return Value

Returns a newly initialized peripheral manager.

#### Discussion

For more information, see [`Core Bluetooth Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/CoreBluetooth_concepts/AboutCoreBluetooth/Introduction.html#//apple_ref/doc/uid/TP40013257).

## Parameters

- `delegate`: The delegate to receive the peripheral role events.
- `queue`: The dispatch queue for dispatching the peripheral role events. If the value is  , the peripheral manager dispatches peripheral role events using the main queue.

## See Also

- [convenience init()](cbperipheralmanager/init.md)
  Initializes the peripheral manager without a delegate.
- [init(delegate: (any CBPeripheralManagerDelegate)?, queue: dispatch_queue_t?, options: [String : Any]?)](cbperipheralmanager/init(delegate:queue:options:).md)
  Initializes the peripheral manager with a specified delegate, dispatch queue, and initialization options.
- [var delegate: (any CBPeripheralManagerDelegate)?](cbperipheralmanager/delegate.md)
  The delegate object specified to receive peripheral events.
- [Peripheral Manager Initialization Options](peripheral-manager-initialization-options.md)
  Keys used to specify options when creating a peripheral manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/init(delegate:queue:))*
# init(delegate:queue:)

**Framework**: Core Bluetooth  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithDelegate:(id<CBPeripheralManagerDelegate>) delegate queue:(dispatch_queue_t) queue;
```

#### Return Value

Returns a newly initialized peripheral manager.

#### Discussion

For more information, see [Core Bluetooth Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/CoreBluetooth_concepts/AboutCoreBluetooth/Introduction.html#//apple_ref/doc/uid/TP40013257).

## Parameters

- `delegate`: The delegate to receive the peripheral role events.
- `queue`: The dispatch queue for dispatching the peripheral role events. If the value is `nil`, the peripheral manager dispatches peripheral role events using the main queue.

## See Also

### Initializing a Peripheral Manager
- [convenience init()](./init%28%29.md)
  Initializes the peripheral manager without a delegate.
- [init(delegate: (any CBPeripheralManagerDelegate)?, queue: dispatch_queue_t?, options: [String : Any]?)](./init%28delegate,queue,options%29.md)
  Initializes the peripheral manager with a specified delegate, dispatch queue, and initialization options.
- [var delegate: (any CBPeripheralManagerDelegate)?](./delegate.md)
  The delegate object specified to receive peripheral events.
- [Peripheral Manager Initialization Options](../peripheral-manager-initialization-options.md)
  Keys used to specify options when creating a peripheral manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/init(delegate:queue:))*
# init(delegate:queue:options:)

**Framework**: Core Bluetooth  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithDelegate:(id<CBPeripheralManagerDelegate>) delegate queue:(dispatch_queue_t) queue options:(NSDictionary<NSString *,id> *) options;
```

## Return Value

Returns a newly initialized peripheral manager.

## Discussion

This method is the designated initializer for the [`CBPeripheralManager`](../cbperipheralmanager.md) class.

## Parameters

- `delegate`: The delegate to receive the peripheral role events.
- `queue`: The dispatch queue for dispatching the peripheral role events. If the value is `nil`, the peripheral manager dispatches peripheral role events using the main queue.
- `options`: An optional dictionary containing initialization options for a peripheral manager. For available options, see [Peripheral Manager Initialization Options](../peripheral-manager-initialization-options.md).

## See Also

### Initializing a Peripheral Manager
- [convenience init()](./init%28%29.md)
  Initializes the peripheral manager without a delegate.
- [convenience init(delegate: (any CBPeripheralManagerDelegate)?, queue: dispatch_queue_t?)](./init%28delegate,queue%29.md)
  Initializes the peripheral manager with a specified delegate and dispatch queue.
- [var delegate: (any CBPeripheralManagerDelegate)?](./delegate.md)
  The delegate object specified to receive peripheral events.
- [Peripheral Manager Initialization Options](../peripheral-manager-initialization-options.md)
  Keys used to specify options when creating a peripheral manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/init(delegate:queue:options:))*
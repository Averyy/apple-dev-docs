# delegate

**Framework**: Core Bluetooth  
**Kind**: property  
**Role**: Instance Property

The delegate object specified to receive peripheral events.

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
weak var delegate: (any CBPeripheralManagerDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<CBPeripheralManagerDelegate> delegate;
```

#### Discussion

For information about how to implement your peripheral manager delegate, see [`CBPeripheralManagerDelegate`](../cbperipheralmanagerdelegate.md).

## See Also

### Initializing a Peripheral Manager
- [convenience init()](./init%28%29.md)
  Initializes the peripheral manager without a delegate.
- [convenience init(delegate: (any CBPeripheralManagerDelegate)?, queue: dispatch_queue_t?)](./init%28delegate,queue%29.md)
  Initializes the peripheral manager with a specified delegate and dispatch queue.
- [init(delegate: (any CBPeripheralManagerDelegate)?, queue: dispatch_queue_t?, options: [String : Any]?)](./init%28delegate,queue,options%29.md)
  Initializes the peripheral manager with a specified delegate, dispatch queue, and initialization options.
- [Peripheral Manager Initialization Options](../peripheral-manager-initialization-options.md)
  Keys used to specify options when creating a peripheral manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/delegate)*
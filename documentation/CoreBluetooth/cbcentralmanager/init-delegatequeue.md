# init(delegate:queue:)

**Framework**: Core Bluetooth  
**Kind**: init

Initializes the central manager with a specified delegate and dispatch queue.

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
convenience init(delegate: (any CBCentralManagerDelegate)?, queue: dispatch_queue_t?)
```

#### Return Value

Returns a newly initialized central manager.

#### Discussion

For more information, see [`Core Bluetooth Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/CoreBluetooth_concepts/AboutCoreBluetooth/Introduction.html#//apple_ref/doc/uid/TP40013257).

## Parameters

- `delegate`: The delegate that receives central events.
- `queue`: The dispatch queue used to dispatch the central role events. If the value is  , the central manager dispatches central role events using the main queue.

## See Also

- [convenience init()](cbcentralmanager/init.md)
  Initializes the central manager without a delegate.
- [init(delegate: (any CBCentralManagerDelegate)?, queue: dispatch_queue_t?, options: [String : Any]?)](cbcentralmanager/init(delegate:queue:options:).md)
  Initializes the central manager with specified delegate, dispatch queue, and initialization options.
- [Central Manager Initialization Options](central-manager-initialization-options.md)
  Keys used to pass options when initializing a central manager.
- [Central Manager State Restoration Options](central-manager-state-restoration-options.md)
  Keys used to pass state restoration options to the central manager initializer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/init(delegate:queue:))*
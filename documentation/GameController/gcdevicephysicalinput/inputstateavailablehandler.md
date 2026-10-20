# inputStateAvailableHandler

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The block that the profile calls when Game Controller adds an input state to the queue.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var inputStateAvailableHandler: ((any GCDevicePhysicalInput) -> Void)? { get set }
```

```objc
@property (atomic, copy, nullable) void (^inputStateAvailableHandler)(id<GCDevicePhysicalInput>physicalInput);
```

## Mentions

- [Handling input events](../handling-input-events.md)

#### Discussion

Set this property to track every element value change, not just the current value. When Game Controller invokes the handler, invoke the [`nextInputState()`](./nextinputstate%28%29.md) method repeatedly to get all the buffered changes until the queue is empty.

To get just the current element value, use the [`elementValueDidChangeHandler`](./elementvaluedidchangehandler.md) property instead.

## See Also

### Handling device input
- [func nextInputState() -> (any GCDevicePhysicalInputState & GCDevicePhysicalInputStateDiff)?](./nextinputstate%28%29.md)
  Returns the next input state from the queue.
- [var inputStateQueueDepth: Int](./inputstatequeuedepth.md)
  The maximum number of input values that the queue stores.
- [func capture() -> any GCDevicePhysicalInputState](./capture%28%29.md)
  Returns a snapshot of the physical device inputs.
- [var elementValueDidChangeHandler: ((any GCDevicePhysicalInput, any GCPhysicalInputElement) -> Void)?](./elementvaluedidchangehandler.md)
  A block that the profile calls when an element’s value changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdevicephysicalinput/inputstateavailablehandler)*
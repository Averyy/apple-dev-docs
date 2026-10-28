# nextInputState()

**Framework**: Game Controller  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the next input state from the queue.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func nextInputState() -> (any GCDevicePhysicalInputState & GCDevicePhysicalInputStateDiff)?
```

```objc
- (id<GCDevicePhysicalInputState,GCDevicePhysicalInputStateDiff>) nextInputState;
```

## Mentions

- [Handling input events](../handling-input-events.md)

## Return Value

The next input state in the queue or `nil` if the queue is empty.

## Discussion

This method removes the next input state from the queue.

## See Also

### Handling device input
- [var inputStateAvailableHandler: ((any GCDevicePhysicalInput) -> Void)?](./inputstateavailablehandler.md)
  The block that the profile calls when Game Controller adds an input state to the queue.
- [var inputStateQueueDepth: Int](./inputstatequeuedepth.md)
  The maximum number of input values that the queue stores.
- [func capture() -> any GCDevicePhysicalInputState](./capture%28%29.md)
  Returns a snapshot of the physical device inputs.
- [var elementValueDidChangeHandler: ((any GCDevicePhysicalInput, any GCPhysicalInputElement) -> Void)?](./elementvaluedidchangehandler.md)
  A block that the profile calls when an element’s value changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdevicephysicalinput/nextinputstate())*
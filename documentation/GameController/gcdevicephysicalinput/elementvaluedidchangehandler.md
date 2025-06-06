# elementValueDidChangeHandler

**Framework**: Game Controller  
**Kind**: property  
**Required**: Yes

A block that the profile calls when an element’s value changes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var elementValueDidChangeHandler: ((any GCDevicePhysicalInput, any GCPhysicalInputElement) -> Void)? { get set }
```

## Mentions

- [Handling input events](handling-input-events.md)

#### Discussion

Use this property to get the latest state of the element. If multiple elements change, Game Controller invokes this block for each element that changes. The block’s parameters are:

> ❗ **Important**:  To track every element value change, set the [`inputStateAvailableHandler`](gcdevicephysicalinput/inputstateavailablehandler.md) property instead and use the [`nextInputState()`](gcdevicephysicalinput/nextinputstate().md) method to get all the buffered changes.

 To track every element value change, set the [`inputStateAvailableHandler`](gcdevicephysicalinput/inputstateavailablehandler.md) property instead and use the [`nextInputState()`](gcdevicephysicalinput/nextinputstate().md) method to get all the buffered changes.

## See Also

- [func nextInputState() -> (any GCDevicePhysicalInputState & GCDevicePhysicalInputStateDiff)?](gcdevicephysicalinput/nextinputstate.md)
  Returns the next input state from the queue.
- [var inputStateAvailableHandler: ((any GCDevicePhysicalInput) -> Void)?](gcdevicephysicalinput/inputstateavailablehandler.md)
  The block that the profile calls when Game Controller adds an input state to the queue.
- [var inputStateQueueDepth: Int](gcdevicephysicalinput/inputstatequeuedepth.md)
  The maximum number of input values that the queue stores.
- [func capture() -> any GCDevicePhysicalInputState](gcdevicephysicalinput/capture.md)
  Returns a snapshot of the physical device inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdevicephysicalinput/elementvaluedidchangehandler)*
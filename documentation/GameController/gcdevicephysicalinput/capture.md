# capture()

**Framework**: Game Controller  
**Kind**: method  
**Required**: Yes

Returns a snapshot of the physical device inputs.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func capture() -> any GCDevicePhysicalInputState
```

## Mentions

- [Handling input events](handling-input-events.md)

#### Return Value

A new instance containing the current state of the physical device input.

## See Also

- [func nextInputState() -> (any GCDevicePhysicalInputState & GCDevicePhysicalInputStateDiff)?](gcdevicephysicalinput/nextinputstate.md)
  Returns the next input state from the queue.
- [var inputStateAvailableHandler: ((any GCDevicePhysicalInput) -> Void)?](gcdevicephysicalinput/inputstateavailablehandler.md)
  The block that the profile calls when Game Controller adds an input state to the queue.
- [var inputStateQueueDepth: Int](gcdevicephysicalinput/inputstatequeuedepth.md)
  The maximum number of input values that the queue stores.
- [var elementValueDidChangeHandler: ((any GCDevicePhysicalInput, any GCPhysicalInputElement) -> Void)?](gcdevicephysicalinput/elementvaluedidchangehandler.md)
  A block that the profile calls when an element’s value changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdevicephysicalinput/capture())*
# inputStateQueueDepth

**Framework**: Game Controller  
**Kind**: property  
**Required**: Yes

The maximum number of input values that the queue stores.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var inputStateQueueDepth: Int { get set }
```

#### Discussion

When the queue reaches this limit, Game Controller starts removing the oldest input states from the queue. The default value for this property is `1` which indicates no buffering.

## See Also

- [func nextInputState() -> (any GCDevicePhysicalInputState & GCDevicePhysicalInputStateDiff)?](gcdevicephysicalinput/nextinputstate.md)
  Returns the next input state from the queue.
- [var inputStateAvailableHandler: ((any GCDevicePhysicalInput) -> Void)?](gcdevicephysicalinput/inputstateavailablehandler.md)
  The block that the profile calls when Game Controller adds an input state to the queue.
- [func capture() -> any GCDevicePhysicalInputState](gcdevicephysicalinput/capture.md)
  Returns a snapshot of the physical device inputs.
- [var elementValueDidChangeHandler: ((any GCDevicePhysicalInput, any GCPhysicalInputElement) -> Void)?](gcdevicephysicalinput/elementvaluedidchangehandler.md)
  A block that the profile calls when an element’s value changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdevicephysicalinput/inputstatequeuedepth)*
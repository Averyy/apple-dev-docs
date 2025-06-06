# nextInputState()

**Framework**: Game Controller  
**Kind**: method

Returns the next input state of the racing wheel from the queue.

**Availability**:
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
func nextInputState() -> (any GCRacingWheelInputState & GCDevicePhysicalInputStateDiff)?
```

#### Return Value

The next input state in the queue or `nil` if the queue is empty.

#### Discussion

This method removes the next input state from the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcracingwheelinput/nextinputstate())*
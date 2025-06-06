# nextInputState()

**Framework**: Game Controller  
**Kind**: method

Returns the next device input state from the queue.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func nextInputState() -> (any GCControllerInputState & GCDevicePhysicalInputStateDiff)?
```

#### Return Value

The next input state in the queue or `nil` if the queue is empty.

## See Also

- [func capture() -> GCControllerInputState](gccontrollerliveinput/capture.md)
  Returns a snapshot of the physical device inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerliveinput/nextinputstate())*
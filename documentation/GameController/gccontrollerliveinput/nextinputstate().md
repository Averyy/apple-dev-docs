# nextInputState()

**Framework**: Game Controller  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (GCControllerInputState<GCDevicePhysicalInputStateDiff> *) nextInputState;
```

#### Return Value

The next input state in the queue or `nil` if the queue is empty.

## See Also

### Handling device input
- [func capture() -> GCControllerInputState](./capture%28%29.md)
  Returns a snapshot of the physical device inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerliveinput/nextinputstate())*
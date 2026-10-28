# capture()

**Framework**: Game Controller  
**Kind**: method  
**Role**: Instance Method

Returns a snapshot of the physical device inputs.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func capture() -> GCControllerInputState
```

```objc
- (GCControllerInputState *) capture;
```

## Return Value

A new instance containing the current state of the physical device input.

## See Also

### Handling device input
- [func nextInputState() -> (any GCControllerInputState & GCDevicePhysicalInputStateDiff)?](./nextinputstate%28%29.md)
  Returns the next device input state from the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerliveinput/capture())*
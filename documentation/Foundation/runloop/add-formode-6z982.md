# add(_:forMode:)

**Framework**: Foundation  
**Kind**: method

Adds a port as an input source to the specified mode of the run loop.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func add(_ aPort: Port, forMode mode: RunLoop.Mode)
```

#### Discussion

This method schedules the port with the receiver. You can add a port to multiple input modes. When the receiver is running in the specified mode, it dispatches messages destined for that port to the port’s designated handler routine.

## Parameters

- `aPort`: The port to add to the receiver.
- `mode`: The mode in which to add  . You may specify a custom mode or use one of the modes listed in  .

## See Also

- [func remove(Port, forMode: RunLoop.Mode)](runloop/remove(_:formode:).md)
  Removes a port from the specified input mode of the run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/runloop/add(_:formode:)-6z982)*
# remove(_:forMode:)

**Framework**: Foundation  
**Kind**: method

Removes a port from the specified input mode of the run loop.

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
func remove(_ aPort: Port, forMode mode: RunLoop.Mode)
```

#### Discussion

If you added the port to multiple input modes, you must remove it from each mode separately.

## Parameters

- `aPort`: The port to remove from the receiver.
- `mode`: The mode from which to remove  . You may specify a custom mode or use one of the modes listed in  .

## See Also

- [func add(Port, forMode: RunLoop.Mode)](runloop/add(_:formode:)-6z982.md)
  Adds a port as an input source to the specified mode of the run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/runloop/remove(_:formode:))*
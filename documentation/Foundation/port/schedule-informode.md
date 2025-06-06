# schedule(in:forMode:)

**Framework**: Foundation  
**Kind**: method

This method should be implemented by a subclass to set up monitoring of a port when added to a given run loop in a given input mode.

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
func schedule(in runLoop: RunLoop, forMode mode: RunLoop.Mode)
```

#### Discussion

This method should not be called directly.

## Parameters

- `runLoop`: The run loop to which to add the receiver.
- `mode`: The run loop mode to which to add the receiver

## See Also

- [func remove(from: RunLoop, forMode: RunLoop.Mode)](port/remove(from:formode:).md)
  This method should be implemented by a subclass to stop monitoring of a port when removed from a give run loop in a given input mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/port/schedule(in:formode:))*
# remove(from:forMode:)

**Framework**: Foundation  
**Kind**: method

Removes the receiver from a given run loop running in a given mode.

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
func remove(from aRunLoop: RunLoop, forMode mode: RunLoop.Mode)
```

## Parameters

- `aRunLoop`: The run loop on which the receiver was scheduled.
- `mode`: The mode for the run loop.

## See Also

- [func schedule(in: RunLoop, forMode: RunLoop.Mode)](stream/schedule(in:formode:).md)
  Schedules the receiver on a given run loop in a given mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/stream/remove(from:formode:))*
# remove(from:forMode:)

**Framework**: Foundation  
**Kind**: method

Removes the receiver from the run loop mode `mode` of `runLoop`.

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
func remove(from runLoop: RunLoop, forMode mode: RunLoop.Mode)
```

#### Discussion

When the receiver is removed, the run loop stops monitoring the Mach port for incoming messages.

## Parameters

- `runLoop`: The run loop from which to remove the receiver.
- `mode`: The run loop mode from which to remove the receiver.

## See Also

- [func schedule(in: RunLoop, forMode: RunLoop.Mode)](nsmachport/schedule(in:formode:).md)
  Schedules the receiver into the run loop mode `mode` of `runLoop`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmachport/remove(from:formode:))*
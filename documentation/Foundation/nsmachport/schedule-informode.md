# schedule(in:forMode:)

**Framework**: Foundation  
**Kind**: method

Schedules the receiver into the run loop mode `mode` of `runLoop`.

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

When the receiver is scheduled, the run loop monitors the mach port for incoming messages and, when a message arrives, invokes the delegate method [`handleMachMessage(_:)`](nsmachportdelegate/handlemachmessage(_:).md).

## Parameters

- `runLoop`: The run loop to which to add the receiver.
- `mode`: The run loop mode in which to add the receiver.

## See Also

- [func remove(from: RunLoop, forMode: RunLoop.Mode)](nsmachport/remove(from:formode:).md)
  Removes the receiver from the run loop mode `mode` of `runLoop`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmachport/schedule(in:formode:))*
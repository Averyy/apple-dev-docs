# kernelStartTime

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The host time, in seconds, when the CPU begins to schedule the command buffer.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
var kernelStartTime: CFTimeInterval { get }
```

#### Discussion

You can calculate how much time the kernel spends scheduling a command buffer by subtracting this value from [`kernelEndTime`](mtlcommandbuffer/kernelendtime.md).

The kernel start and end times remain `0.0` until the GPU driver (on the CPU) schedules the command buffer to run on the GPU. Apps typically use these values after the [`waitUntilScheduled()`](mtlcommandbuffer/waituntilscheduled().md) method returns, or within a completion handler (see [`addScheduledHandler(_:)`](mtlcommandbuffer/addscheduledhandler(_:).md) and [`addCompletedHandler(_:)`](mtlcommandbuffer/addcompletedhandler(_:).md)).

## See Also

- [var kernelEndTime: CFTimeInterval](mtlcommandbuffer/kernelendtime.md)
  The host time, in seconds, when the CPU finishes scheduling the command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/kernelstarttime)*
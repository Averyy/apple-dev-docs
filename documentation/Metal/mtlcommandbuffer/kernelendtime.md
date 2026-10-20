# kernelEndTime

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The host time, in seconds, when the CPU finishes scheduling the command buffer.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
var kernelEndTime: CFTimeInterval { get }
```

```objc
@property (readonly) CFTimeInterval kernelEndTime;
```

#### Discussion

You can calculate how much time the kernel spends scheduling a command buffer by subtracting [`kernelStartTime`](./kernelstarttime.md) from this value.

The kernel start and end times remain `0.0` until the GPU driver (on the CPU) schedules the command buffer to run on the GPU. Apps typically use these values after the [`waitUntilScheduled()`](./waituntilscheduled%28%29.md) method returns, or within a completion handler (see [`addScheduledHandler(_:)`](./addscheduledhandler%28_%29.md) and [`addCompletedHandler(_:)`](./addcompletedhandler%28_%29.md)).

## See Also

### Checking scheduling times on the CPU
- [var kernelStartTime: CFTimeInterval](./kernelstarttime.md)
  The host time, in seconds, when the CPU begins to schedule the command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/kernelendtime)*
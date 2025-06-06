# gpuEndTime

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The host time, in seconds, when the GPU finishes execution of the command buffer.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
var gpuEndTime: CFTimeInterval { get }
```

#### Discussion

You can calculate how much time the GPU spends running a command buffer by subtracting [`gpuStartTime`](mtlcommandbuffer/gpustarttime.md) from this value. Both values are relative to system mach time.

The GPU start and end times remain `0.0` until the GPU finishes running the command buffer. Check this value after the [`waitUntilCompleted()`](mtlcommandbuffer/waituntilcompleted().md) method returns, or within a completion handler passed to the [`addCompletedHandler(_:)`](mtlcommandbuffer/addcompletedhandler(_:).md) method.

## See Also

- [var gpuStartTime: CFTimeInterval](mtlcommandbuffer/gpustarttime.md)
  The host time, in seconds, when the GPU starts command buffer execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/gpuendtime)*
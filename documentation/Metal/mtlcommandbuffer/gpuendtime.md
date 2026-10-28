# gpuEndTime

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
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

```objc
@property (readonly) CFTimeInterval GPUEndTime;
```

## Discussion

You can calculate how much time the GPU spends running a command buffer by subtracting [`gpuStartTime`](./gpustarttime.md) from this value. Both values are relative to system mach time.

The GPU start and end times remain `0.0` until the GPU finishes running the command buffer. Check this value after the [`waitUntilCompleted()`](./waituntilcompleted%28%29.md) method returns, or within a completion handler passed to the [`addCompletedHandler(_:)`](./addcompletedhandler%28_%29.md) method.

## See Also

### Checking execution times on the GPU
- [var gpuStartTime: CFTimeInterval](./gpustarttime.md)
  The host time, in seconds, when the GPU starts command buffer execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/gpuendtime)*
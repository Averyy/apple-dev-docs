# cumulativeIllegalInstructionExitCount

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The number of times the system terminated the app from the foreground for attempting to execute an illegal or undefined instruction.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`illegalInstructionTerminationCount`](../foregroundterminationmetric/illegalinstructionterminationcount.md) instead.

## Declaration

```swift
var cumulativeIllegalInstructionExitCount: Int { get }
```

```objc
@property (readonly) NSUInteger cumulativeIllegalInstructionExitCount;
```

## Discussion

One way to trigger this exit is by invoking a function with a misconfigured function pointer.

## See Also

### Reading the Crash Count
- [var cumulativeBadAccessExitCount: Int](./cumulativebadaccessexitcount.md)
  The number of times the system terminated the app from the foreground for attempting an invalid memory access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxforegroundexitdata/cumulativeillegalinstructionexitcount)*
# cumulativeIllegalInstructionExitCount

**Framework**: MetricKit  
**Kind**: property

The number of times the system terminated the app from the foreground for attempting to execute an illegal or undefined instruction.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var cumulativeIllegalInstructionExitCount: Int { get }
```

#### Discussion

One way to trigger this exit is by invoking a function with a misconfigured function pointer.

## See Also

- [var cumulativeBadAccessExitCount: Int](mxforegroundexitdata/cumulativebadaccessexitcount.md)
  The number of times the system terminated the app from the foreground for attempting an invalid memory access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxforegroundexitdata/cumulativeillegalinstructionexitcount)*
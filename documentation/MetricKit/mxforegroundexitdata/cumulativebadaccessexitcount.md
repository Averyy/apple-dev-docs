# cumulativeBadAccessExitCount

**Framework**: MetricKit  
**Kind**: property

The number of times the system terminated the app from the foreground for attempting an invalid memory access.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
var cumulativeBadAccessExitCount: Int { get }
```

#### Discussion

The most common reasons for this kind of termination are an attempt to access a nonexistent or reserved memory location, or to access memory in a way that’s inconsistent with the protection level, such as writing to read-only memory.

## See Also

- [var cumulativeIllegalInstructionExitCount: Int](mxforegroundexitdata/cumulativeillegalinstructionexitcount.md)
  The number of times the system terminated the app from the foreground for attempting to execute an illegal or undefined instruction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxforegroundexitdata/cumulativebadaccessexitcount)*
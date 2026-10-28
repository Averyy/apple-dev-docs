# cumulativeBadAccessExitCount

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The number of times the system terminated the app from the background for attempting an invalid memory access.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`badAccessTerminationCount`](../backgroundterminationmetric/badaccessterminationcount.md) instead.

## Declaration

```swift
var cumulativeBadAccessExitCount: Int { get }
```

```objc
@property (readonly) NSUInteger cumulativeBadAccessExitCount;
```

## Discussion

The most common reasons for this kind of termination are an attempt to access a nonexistent or reserved memory location, or to access memory in a way that’s inconsistent with the protection level, such as writing to read-only memory.

## See Also

### Reading the Crash Count
- [var cumulativeIllegalInstructionExitCount: Int](./cumulativeillegalinstructionexitcount.md)
  The number of times the system terminated the app from the background for attempting to execute an illegal or undefined instruction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxbackgroundexitdata/cumulativebadaccessexitcount)*
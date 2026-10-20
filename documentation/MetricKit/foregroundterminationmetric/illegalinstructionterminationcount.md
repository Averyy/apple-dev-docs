# illegalInstructionTerminationCount

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The number of times the system terminated the app from the foreground for attempting to execute an illegal or undefined instruction.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
let illegalInstructionTerminationCount: Int
```

## See Also

### Foreground termination counts
- [let normalTerminationCount: Int](./normalterminationcount.md)
  The number of times the application terminated normally from the foreground.
- [let memoryLimitTerminationCount: Int](./memorylimitterminationcount.md)
  The number of times the system terminated the app from the foreground for using too much memory.
- [let badAccessTerminationCount: Int](./badaccessterminationcount.md)
  The number of times the system terminated the app from the foreground for attempting an invalid memory access.
- [let abnormalTerminationCount: Int](./abnormalterminationcount.md)
  The number of times the app terminated abnormally from the foreground.
- [let watchdogTerminationCount: Int](./watchdogterminationcount.md)
  The number of times the system watchdog terminated the app from the foreground.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/foregroundterminationmetric/illegalinstructionterminationcount)*
# normalTerminationCount

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The number of times the application terminated normally from the background.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
let normalTerminationCount: Int
```

## See Also

### Background termination counts
- [let memoryLimitTerminationCount: Int](./memorylimitterminationcount.md)
  The number of times the system terminated the app from the background for using too much memory.
- [let highCPUTerminationCount: Int](./highcputerminationcount.md)
  The number of times the system terminated the app from the background for using too much CPU time.
- [let systemPressureTerminationCount: Int](./systempressureterminationcount.md)
  The number of times the system terminated the app from the background to free up memory.
- [let badAccessTerminationCount: Int](./badaccessterminationcount.md)
  The number of times the system terminated the app from the background for attempting an invalid memory access.
- [let abnormalTerminationCount: Int](./abnormalterminationcount.md)
  The number of times the app terminated abnormally from the background.
- [let illegalInstructionTerminationCount: Int](./illegalinstructionterminationcount.md)
  The number of times the system terminated the app from the background for attempting to execute an illegal or undefined instruction.
- [let watchdogTerminationCount: Int](./watchdogterminationcount.md)
  The number of times the system watchdog terminated the app from the background.
- [let fileLockTerminationCount: Int](./filelockterminationcount.md)
  The number of times the system terminated the app from the background while being suspended and having file locks.
- [let taskTimeoutTerminationCount: Int](./tasktimeoutterminationcount.md)
  The number of times the system terminated the app from the background for exceeding the allocated time for a background task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/backgroundterminationmetric/normalterminationcount)*
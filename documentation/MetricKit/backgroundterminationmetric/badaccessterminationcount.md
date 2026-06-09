# badAccessTerminationCount

**Framework**: MetricKit  
**Kind**: property

The number of times the system terminated the app from the background for attempting an invalid memory access.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
let badAccessTerminationCount: Int
```

## See Also

- [let normalTerminationCount: Int](backgroundterminationmetric/normalterminationcount.md)
  The number of times the application terminated normally from the background.
- [let memoryLimitTerminationCount: Int](backgroundterminationmetric/memorylimitterminationcount.md)
  The number of times the system terminated the app from the background for using too much memory.
- [let highCPUTerminationCount: Int](backgroundterminationmetric/highcputerminationcount.md)
  The number of times the system terminated the app from the background for using too much CPU time.
- [let systemPressureTerminationCount: Int](backgroundterminationmetric/systempressureterminationcount.md)
  The number of times the system terminated the app from the background to free up memory.
- [let abnormalTerminationCount: Int](backgroundterminationmetric/abnormalterminationcount.md)
  The number of times the app terminated abnormally from the background.
- [let illegalInstructionTerminationCount: Int](backgroundterminationmetric/illegalinstructionterminationcount.md)
  The number of times the system terminated the app from the background for attempting to execute an illegal or undefined instruction.
- [let watchdogTerminationCount: Int](backgroundterminationmetric/watchdogterminationcount.md)
  The number of times the system watchdog terminated the app from the background.
- [let fileLockTerminationCount: Int](backgroundterminationmetric/filelockterminationcount.md)
  The number of times the system terminated the app from the background while being suspended and having file locks.
- [let taskTimeoutTerminationCount: Int](backgroundterminationmetric/tasktimeoutterminationcount.md)
  The number of times the system terminated the app from the background for exceeding the allocated time for a background task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/backgroundterminationmetric/badaccessterminationcount)*
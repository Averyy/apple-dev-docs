# illegalInstructionTerminationCount

**Framework**: MetricKit  
**Kind**: property

The number of times the system terminated the app from the foreground for attempting to execute an illegal or undefined instruction.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
let illegalInstructionTerminationCount: Int
```

## See Also

- [let normalTerminationCount: Int](foregroundterminationmetric/normalterminationcount.md)
  The number of times the application terminated normally from the foreground.
- [let memoryLimitTerminationCount: Int](foregroundterminationmetric/memorylimitterminationcount.md)
  The number of times the system terminated the app from the foreground for using too much memory.
- [let badAccessTerminationCount: Int](foregroundterminationmetric/badaccessterminationcount.md)
  The number of times the system terminated the app from the foreground for attempting an invalid memory access.
- [let abnormalTerminationCount: Int](foregroundterminationmetric/abnormalterminationcount.md)
  The number of times the app terminated abnormally from the foreground.
- [let watchdogTerminationCount: Int](foregroundterminationmetric/watchdogterminationcount.md)
  The number of times the system watchdog terminated the app from the foreground.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/foregroundterminationmetric/illegalinstructionterminationcount)*
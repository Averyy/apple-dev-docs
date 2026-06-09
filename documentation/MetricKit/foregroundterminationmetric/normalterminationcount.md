# normalTerminationCount

**Framework**: MetricKit  
**Kind**: property

The number of times the application terminated normally from the foreground.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
let normalTerminationCount: Int
```

## See Also

- [let memoryLimitTerminationCount: Int](foregroundterminationmetric/memorylimitterminationcount.md)
  The number of times the system terminated the app from the foreground for using too much memory.
- [let badAccessTerminationCount: Int](foregroundterminationmetric/badaccessterminationcount.md)
  The number of times the system terminated the app from the foreground for attempting an invalid memory access.
- [let abnormalTerminationCount: Int](foregroundterminationmetric/abnormalterminationcount.md)
  The number of times the app terminated abnormally from the foreground.
- [let illegalInstructionTerminationCount: Int](foregroundterminationmetric/illegalinstructionterminationcount.md)
  The number of times the system terminated the app from the foreground for attempting to execute an illegal or undefined instruction.
- [let watchdogTerminationCount: Int](foregroundterminationmetric/watchdogterminationcount.md)
  The number of times the system watchdog terminated the app from the foreground.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/foregroundterminationmetric/normalterminationcount)*
---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/level/critical"
framework: "swift-log/Logging"
---

# Logger.Level.critical

**Framework**: swift-log/Logging  
**Kind**: case  
**Role**: Case

Appropriate for critical error conditions that usually require immediate attention.

## Declaration

```swift
case critical
```

## Mentions

- [001: Choosing log levels](../../api-001-choosingloglevels.md)
- [Understanding Loggers and Log Handlers](../../understandingloggers.md)

## Discussion

When a `critical` message is logged, the logging backend (`LogHandler`) is free to perform more heavy-weight operations to capture system state (such as capturing stack traces) to facilitate debugging.

## See Also

### Log Levels
- [Logger.Level.trace](./trace.md)
  Appropriate for messages that contain information normally of use only when tracing the execution of a program.
- [Logger.Level.debug](./debug.md)
  Appropriate for messages that contain information normally of use only when debugging a program.
- [Logger.Level.info](./info.md)
  Appropriate for informational messages.
- [Logger.Level.notice](./notice.md)
  Appropriate for conditions that are not error conditions, but that may require special handling.
- [Logger.Level.warning](./warning.md)
  Appropriate for messages that are not error conditions, but more severe than notice.
- [Logger.Level.error](./error.md)
  Appropriate for error conditions.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/level/critical)*
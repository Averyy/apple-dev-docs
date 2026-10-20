# OSLogEntryLog.Level.notice

**Framework**: OSLog  
**Kind**: case  
**Role**: Case

The log level that captures notifications.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
case notice
```

```c
OSLogEntryLogLevelNotice
```

#### Discussion

This log level captures normal `os_log` entries used to generate notifications on system errors.

## See Also

### Log Levels
- [OSLogEntryLog.Level.undefined](./undefined.md)
  The log level was never specified.
- [OSLogEntryLog.Level.debug](./debug.md)
  A log level that captures diagnostic information.
- [OSLogEntryLog.Level.info](./info.md)
  The log level that captures additional information.
- [OSLogEntryLog.Level.error](./error.md)
  The log level that captures errors.
- [OSLogEntryLog.Level.fault](./fault.md)
  The log level that captures fault information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/oslog/oslogentrylog/level-swift.enum/notice)*
# OSLogEntryLog.Level

**Framework**: OSLog  
**Kind**: enum  
**Role**: Enumeration

The log level at which the entry was generated.

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
enum Level
```

```c
enum OSLogEntryLogLevel : NSInteger;
```

## Topics

### Log Levels
- [OSLogEntryLog.Level.undefined](./level-swift.enum/undefined.md)
  The log level was never specified.
- [OSLogEntryLog.Level.debug](./level-swift.enum/debug.md)
  A log level that captures diagnostic information.
- [OSLogEntryLog.Level.info](./level-swift.enum/info.md)
  The log level that captures additional information.
- [OSLogEntryLog.Level.notice](./level-swift.enum/notice.md)
  The log level that captures notifications.
- [OSLogEntryLog.Level.error](./level-swift.enum/error.md)
  The log level that captures errors.
- [OSLogEntryLog.Level.fault](./level-swift.enum/fault.md)
  The log level that captures fault information.
### Initializers
- [init?(rawValue: Int)](./level-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing Log Levels
- [var level: OSLogEntryLog.Level](./level-swift.property.md)
  The log level of the entry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/oslog/oslogentrylog/level-swift.enum)*
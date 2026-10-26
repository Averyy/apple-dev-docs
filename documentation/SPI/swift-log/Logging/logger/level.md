---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/level"
framework: "swift-log/Logging"
---

# Logger.Level

**Framework**: swift-log/Logging  
**Kind**: enum  
**Role**: Enumeration

The log level.

## Declaration

```swift
enum Level
```

## Mentions

- [001: Choosing log levels](../api-001-choosingloglevels.md)
- [Understanding Loggers and Log Handlers](../understandingloggers.md)

#### Overview

Log levels are ordered by their severity, with `.trace` being the least severe and `.critical` being the most severe.

## Topics

### Log Levels
- [Logger.Level.trace](./level/trace.md)
  Appropriate for messages that contain information normally of use only when tracing the execution of a program.
- [Logger.Level.debug](./level/debug.md)
  Appropriate for messages that contain information normally of use only when debugging a program.
- [Logger.Level.info](./level/info.md)
  Appropriate for informational messages.
- [Logger.Level.notice](./level/notice.md)
  Appropriate for conditions that are not error conditions, but that may require special handling.
- [Logger.Level.warning](./level/warning.md)
  Appropriate for messages that are not error conditions, but more severe than notice.
- [Logger.Level.error](./level/error.md)
  Appropriate for error conditions.
- [Logger.Level.critical](./level/critical.md)
  Appropriate for critical error conditions that usually require immediate attention.
### Initializers
- [init?(rawValue: String)](./level/init%28rawvalue%29.md)
### Default Implementations
- [Comparable Implementations](./level/comparable-implementations.md)
- [CustomStringConvertible Implementations](./level/customstringconvertible-implementations.md)
- [Equatable Implementations](./level/equatable-implementations.md)
- [LosslessStringConvertible Implementations](./level/losslessstringconvertible-implementations.md)
- [RawRepresentable Implementations](./level/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- Swift.CaseIterable
- Swift.Comparable
- Swift.Copyable
- Swift.CustomStringConvertible
- Swift.Decodable
- Swift.Encodable
- Swift.Equatable
- Swift.Escapable
- Swift.Hashable
- Swift.LosslessStringConvertible
- Swift.RawRepresentable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Sending general log messages
- [func log(level: Logger.Level, @autoclosure () -> Logger.Message, metadata: @autoclosure () -> Logger.Metadata?, file: String, function: String, line: UInt)](./log%28level,_,metadata,file,function,line%29.md)
  Log a message using the log level you provide.
- [func log(level: Logger.Level, @autoclosure () -> Logger.Message, metadata: @autoclosure () -> Logger.Metadata?, source: @autoclosure () -> String?, file: String, function: String, line: UInt)](./log%28level,_,metadata,source,file,function,line%29.md)
  Log a message using the log level and source that you provide.
- [func log(level: Logger.Level, @autoclosure () -> Logger.Message, error: @autoclosure () -> (any Error)?, metadata: @autoclosure () -> Logger.Metadata?, source: @autoclosure () -> String?, file: String, function: String, line: UInt)](./log%28level,_,error,metadata,source,file,function,line%29.md)
  Log a message using the log level and source that you provide.
- [Logger.Message](./message.md)
  The content of log message.
- [typealias Metadata](./metadata.md)
  The type of the metadata storage.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/level)*
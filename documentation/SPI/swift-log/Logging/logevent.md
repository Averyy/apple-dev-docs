---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logevent"
framework: "swift-log/Logging"
---

# LogEvent

**Framework**: swift-log/Logging  
**Kind**: struct  
**Role**: Structure

A log event that contains all the information about a single log statement.

## Declaration

```swift
struct LogEvent
```

#### Overview

`LogEvent` is passed to a [`LogHandler`](./loghandler.md) via [`log(event:)`](./loghandler/log%28event%29.md) and carries every piece of data emitted at the log call site. Handlers may inspect, modify, or forward any of the event’s properties.

All properties are mutable so that handler wrappers (for example [`MultiplexLogHandler`](./multiplexloghandler.md)) can rewrite fields such as metadata or source before forwarding to downstream handlers.

## Topics

### Creating a log event
- [init(level: Logger.Level, message: Logger.Message, metadata: Logger.Metadata?, source: String?, file: String, function: String, line: UInt)](./logevent/init%28level,message,metadata,source,file,function,line%29.md)
  Creates a new log event.
- [init(level: Logger.Level, message: Logger.Message, error: (any Error)?, metadata: Logger.Metadata?, source: String?, file: String, function: String, line: UInt)](./logevent/init%28level,message,error,metadata,source,file,function,line%29.md)
  Creates a new log event.
### Inspecting a log event
- [var level: Logger.Level](./logevent/level.md)
  The log level of this event.
- [var message: Logger.Message](./logevent/message.md)
  The message of this event.
- [var error: (any Error)?](./logevent/error.md)
  The error associated with this event, if any.
- [var metadata: Logger.Metadata?](./logevent/metadata.md)
  The metadata associated with this event, if any.
- [var source: String](./logevent/source.md)
  The source where this log event originated, for example the logging module.
- [var file: String](./logevent/file.md)
  The file this log event originates from.
- [var function: String](./logevent/function.md)
  The function this log event originates from.
- [var line: UInt](./logevent/line.md)
  The line this log event originates from.

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Log Handlers
- [protocol LogHandler](./loghandler.md)
  A log handler provides an implementation of a logging backend.
- [struct MultiplexLogHandler](./multiplexloghandler.md)
  A pseudo log handler that sends messages to multiple other log handlers.
- [struct StreamLogHandler](./streamloghandler.md)
  Stream log handler presents log messages to STDERR or STDOUT.
- [struct SwiftLogNoOpLogHandler](./swiftlognooploghandler.md)
  A no-operation log handler, used when no logging is required


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logevent)*
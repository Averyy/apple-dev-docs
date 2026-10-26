---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/streamloghandler"
framework: "swift-log/Logging"
---

# StreamLogHandler

**Framework**: swift-log/Logging  
**Kind**: struct  
**Role**: Structure

Stream log handler presents log messages to STDERR or STDOUT.

## Declaration

```swift
struct StreamLogHandler
```

## Mentions

- [Understanding Loggers and Log Handlers](./understandingloggers.md)

#### Overview

This is a simple implementation of `LogHandler` that directs `Logger` output to either `stderr` or `stdout` via the factory methods.

Metadata is merged in the following order:

1. Metadata set on the log handler itself is used as the base metadata.
2. The handler’s [`metadataProvider`](./streamloghandler/metadataprovider.md) is invoked, overriding any existing keys.
3. The per-log-statement metadata is merged, overriding any previously set keys.

## Topics

### Creating a stream log handler
- [static func standardOutput(label: String) -> StreamLogHandler](./streamloghandler/standardoutput%28label%29.md)
  Creates a stream log handler that directs its output to STDOUT.
- [static func standardOutput(label: String, metadataProvider: Logger.MetadataProvider?) -> StreamLogHandler](./streamloghandler/standardoutput%28label,metadataprovider%29.md)
  Creates a stream log handler that directs its output to STDOUT using the metadata provider you provide.
- [static func standardError(label: String) -> StreamLogHandler](./streamloghandler/standarderror%28label%29.md)
  Creates a stream log handler that directs its output to STDERR.
- [static func standardError(label: String, metadataProvider: Logger.MetadataProvider?) -> StreamLogHandler](./streamloghandler/standarderror%28label,metadataprovider%29.md)
  Creates a stream log handler that directs its output to STDERR using the metadata provider you provide.
- [init(label: String, stream: any TextOutputStream & Sendable)](./streamloghandler/init%28label,stream%29.md)
  Creates a [`StreamLogHandler`](./streamloghandler.md) that directs its output to the stream you provide, using the global metadata provider from [`LoggingSystem`](./loggingsystem.md).
- [init(label: String, stream: any TextOutputStream & Sendable, metadataProvider: Logger.MetadataProvider?)](./streamloghandler/init%28label,stream,metadataprovider%29.md)
  Creates a [`StreamLogHandler`](./streamloghandler.md) that directs its output to the stream you provide, using the metadata provider you provide.
### Sending log messages
- [func log(event: LogEvent)](./streamloghandler/log%28event%29.md)
  Log a message using the log level and source that you provide.
- [func log(level: Logger.Level, message: Logger.Message, metadata: Logger.Metadata?, source: String, file: String, function: String, line: UInt)](./streamloghandler/log%28level,message,metadata,source,file,function,line%29.md)
### Updating metadata
- [subscript(metadataKey _: String) -> Logger.Metadata.Value?](./streamloghandler/subscript%28metadatakey%29.md)
  Add, change, or remove a logging metadata item.
### Inspecting a log handler
- [var logLevel: Logger.Level](./streamloghandler/loglevel.md)
  Get the log level configured for this `Logger`.
- [var metadata: Logger.Metadata](./streamloghandler/metadata.md)
  Get or set the entire metadata storage as a dictionary.
- [var metadataProvider: Logger.MetadataProvider?](./streamloghandler/metadataprovider.md)
  The metadata provider.
### Default Implementations
- [LogHandler Implementations](./streamloghandler/loghandler-implementations.md)

## Relationships

### Conforms To
- [LogHandler](./loghandler.md)
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Log Handlers
- [protocol LogHandler](./loghandler.md)
  A log handler provides an implementation of a logging backend.
- [struct LogEvent](./logevent.md)
  A log event that contains all the information about a single log statement.
- [struct MultiplexLogHandler](./multiplexloghandler.md)
  A pseudo log handler that sends messages to multiple other log handlers.
- [struct SwiftLogNoOpLogHandler](./swiftlognooploghandler.md)
  A no-operation log handler, used when no logging is required


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/streamloghandler)*
---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/swiftlognooploghandler"
framework: "swift-log/Logging"
---

# SwiftLogNoOpLogHandler

**Framework**: swift-log/Logging  
**Kind**: struct  
**Role**: Structure

A no-operation log handler, used when no logging is required

## Declaration

```swift
struct SwiftLogNoOpLogHandler
```

#### Overview

A log handler that silently discards all log messages.

## Topics

### Creating a Swift Log no-op log handler
- [init()](./swiftlognooploghandler/init%28%29.md)
  Creates a no-op log handler.
- [init(String)](./swiftlognooploghandler/init%28_%29.md)
  Creates a no-op log handler.
### Sending log messages
- [func log(event: LogEvent)](./swiftlognooploghandler/log%28event%29.md)
  A proxy that discards every log event it receives.
- [func log(level: Logger.Level, message: Logger.Message, metadata: Logger.Metadata?, source: String, file: String, function: String, line: UInt)](./swiftlognooploghandler/log%28level,message,metadata,source,file,function,line%29.md)
- [func log(level: Logging.Logger.Level, message: Logging.Logger.Message, metadata: Logging.Logger.Metadata?, file: String, function: String, line: UInt)](./swiftlognooploghandler/log%28level,message,metadata,file,function,line%29.md)
### Updating metadata
- [subscript(metadataKey _: String) -> Logger.Metadata.Value?](./swiftlognooploghandler/subscript%28metadatakey%29.md)
  Add, change, or remove a logging metadata item.
### Inspecting a log handler
- [var logLevel: Logger.Level](./swiftlognooploghandler/loglevel.md)
  Get or set the log level configured for this `Logger`.
- [var metadata: Logger.Metadata](./swiftlognooploghandler/metadata.md)
  Get or set the entire metadata storage as a dictionary.
- [var metadataProvider: Logger.MetadataProvider?](./swiftlognooploghandler/metadataprovider.md)
  Default implementation for a metadata provider that defaults to nil.
### Default Implementations
- [LogHandler Implementations](./swiftlognooploghandler/loghandler-implementations.md)

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
- [struct StreamLogHandler](./streamloghandler.md)
  Stream log handler presents log messages to STDERR or STDOUT.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/swiftlognooploghandler)*
---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger"
framework: "swift-log/Logging"
---

# Logger

**Framework**: swift-log/Logging  
**Kind**: struct  
**Role**: Structure

A Logger emits log messages using methods that correspond to a log level.

## Declaration

```swift
struct Logger
```

## Mentions

- [Understanding Loggers and Log Handlers](./understandingloggers.md)
- [SLG-NNNN: Feature name](./slg-nnnn.md)

#### Overview

`Logger` is a value type with respect to the [`Logger.Level`](./logger/level.md) and the [`Logger.Metadata`](./logger/metadata.md) (as well as the immutable `label` and the selected [`LogHandler`](./loghandler.md)). Therefore, you can pass an instance of `Logger` between libraries to preserve metadata across libraries.

The most basic usage of a `Logger` is:

```swift
logger.info("Hello World!")
```

## Topics

### Creating Loggers
- [init(label: String)](./logger/init%28label%29.md)
  Construct a logger with the label you provide to identify the creator of the logger.
- [init(label: String, metadataProvider: MetadataProvider)](./logger/init%28label,metadataprovider%29.md)
  Creates a logger using the label that identifies the creator of the logger or a non-standard log handler.
- [init(label: String, factory: (String) -> any LogHandler)](./logger/init%28label,factory%29-9uiy2.md)
  Creates a logger using the label that identifies the creator of the logger or a non-standard log handler.
- [init(label: String, factory: (String, Logger.MetadataProvider?) -> any LogHandler)](./logger/init%28label,factory%29-6iktu.md)
  Creates a logger using the label that identifies the creator of the logger or a non-standard log handler.
- [Logger.MetadataProvider](./logger/metadataprovider-swift.struct.md)
  A MetadataProvider automatically injects runtime-generated metadata to all logs emitted by a logger.
### Task-local logger
- [static var current: Logger](./logger/current.md)
  The current task-local logger.
- [func withLogger<Result, Failure>(Logger, (Logger) throws(Failure) -> Result) throws(Failure) -> Result](./withlogger%28_,_%29-3dt06.md)
  Runs `operation` with `logger` bound to the task-local context.
- [func withLogger<Result, Failure>(Logger, nonisolated(nonsending)) async throws(Failure) -> Result](./withlogger%28_,_%29-70nli.md)
  Runs `operation` with `logger` bound to the task-local context.
- [func withLogger<Result, Failure>(mergingMetadata: @autoclosure () -> Logger.Metadata, (Logger) throws(Failure) -> Result) throws(Failure) -> Result](./withlogger%28mergingmetadata,_%29-2c7dy.md)
  Runs `operation` with a copy of [`current`](./logger/current.md) that has `metadata` **layered on top of** the inherited base metadata. Keys present in `metadata` override existing keys with the same name. Other aspects (handler, log level, base metadata not in `metadata`) are preserved.
- [func withLogger<Result, Failure>(mergingMetadata: @autoclosure () -> Logger.Metadata, nonisolated(nonsending)) async throws(Failure) -> Result](./withlogger%28mergingmetadata,_%29-3eduo.md)
  Runs `operation` with a copy of [`current`](./logger/current.md) that has `metadata` **layered on top of** the inherited base metadata. Keys present in `metadata` override existing keys with the same name. Other aspects (handler, log level, base metadata not in `metadata`) are preserved.
- [func withLogger<Result, Failure>(logLevel: Logger.Level?, handler: (any LogHandler)?, metadata: @autoclosure () -> Logger.Metadata?, (Logger) throws(Failure) -> Result) throws(Failure) -> Result](./withlogger%28loglevel,handler,metadata,_%29-2pd9p.md)
  Runs `operation` with a copy of [`current`](./logger/current.md) whose aspects are **replaced** by the provided arguments. `nil` parameters leave the corresponding aspect unchanged.
- [func withLogger<Result, Failure>(logLevel: Logger.Level?, handler: (any LogHandler)?, metadata: @autoclosure () -> Logger.Metadata?, nonisolated(nonsending)) async throws(Failure) -> Result](./withlogger%28loglevel,handler,metadata,_%29-5nmw6.md)
  Runs `operation` with a copy of [`current`](./logger/current.md) whose aspects are **replaced** by the provided arguments. `nil` parameters leave the corresponding aspect unchanged.
### Sending trace log messages
- [func trace(@autoclosure () -> Logger.Message, metadata: @autoclosure () -> Logger.Metadata?, file: String, function: String, line: UInt)](./logger/trace%28_,metadata,file,function,line%29.md)
  Log a message at the ‘trace’ log level.
- [func trace(@autoclosure () -> Logger.Message, metadata: @autoclosure () -> Logger.Metadata?, source: @autoclosure () -> String?, file: String, function: String, line: UInt)](./logger/trace%28_,metadata,source,file,function,line%29.md)
  Log a message at the ‘trace’ log level with the source that you provide.
- [func trace(@autoclosure () -> Logger.Message, error: @autoclosure () -> (any Error)?, metadata: @autoclosure () -> Logger.Metadata?, source: @autoclosure () -> String?, file: String, function: String, line: UInt)](./logger/trace%28_,error,metadata,source,file,function,line%29.md)
  Log a message at the ‘trace’ log level with the source that you provide.
### Sending debug log messages
- [func debug(@autoclosure () -> Logger.Message, metadata: @autoclosure () -> Logger.Metadata?, file: String, function: String, line: UInt)](./logger/debug%28_,metadata,file,function,line%29.md)
  Log a message at the ‘debug’ log level.
- [func debug(@autoclosure () -> Logger.Message, metadata: @autoclosure () -> Logger.Metadata?, source: @autoclosure () -> String?, file: String, function: String, line: UInt)](./logger/debug%28_,metadata,source,file,function,line%29.md)
  Log a message at the ‘debug’ log level with the source that you provide.
- [func debug(@autoclosure () -> Logger.Message, error: @autoclosure () -> (any Error)?, metadata: @autoclosure () -> Logger.Metadata?, source: @autoclosure () -> String?, file: String, function: String, line: UInt)](./logger/debug%28_,error,metadata,source,file,function,line%29.md)
  Log a message at the ‘debug’ log level with the source that you provide.
### Sending info log messages
- [func info(@autoclosure () -> Logger.Message, metadata: @autoclosure () -> Logger.Metadata?, file: String, function: String, line: UInt)](./logger/info%28_,metadata,file,function,line%29.md)
  Log a message at the ‘info’ log level.
- [func info(@autoclosure () -> Logger.Message, metadata: @autoclosure () -> Logger.Metadata?, source: @autoclosure () -> String?, file: String, function: String, line: UInt)](./logger/info%28_,metadata,source,file,function,line%29.md)
  Log a message at the ‘info’ log level with the source that you provide.
- [func info(@autoclosure () -> Logger.Message, error: @autoclosure () -> (any Error)?, metadata: @autoclosure () -> Logger.Metadata?, source: @autoclosure () -> String?, file: String, function: String, line: UInt)](./logger/info%28_,error,metadata,source,file,function,line%29.md)
  Log a message at the ‘info’ log level with the source that you provide.
### Sending notice log messages
- [func notice(@autoclosure () -> Logger.Message, metadata: @autoclosure () -> Logger.Metadata?, file: String, function: String, line: UInt)](./logger/notice%28_,metadata,file,function,line%29.md)
  Log a message at the ‘notice’ log level.
- [func notice(@autoclosure () -> Logger.Message, metadata: @autoclosure () -> Logger.Metadata?, source: @autoclosure () -> String?, file: String, function: String, line: UInt)](./logger/notice%28_,metadata,source,file,function,line%29.md)
  Log a message at the ‘notice’ log level with the source that you provide.
- [func notice(@autoclosure () -> Logger.Message, error: @autoclosure () -> (any Error)?, metadata: @autoclosure () -> Logger.Metadata?, source: @autoclosure () -> String?, file: String, function: String, line: UInt)](./logger/notice%28_,error,metadata,source,file,function,line%29.md)
  Log a message at the ‘notice’ log level with the source that you provide.
### Sending warning log messages
- [func warning(@autoclosure () -> Logger.Message, metadata: @autoclosure () -> Logger.Metadata?, file: String, function: String, line: UInt)](./logger/warning%28_,metadata,file,function,line%29.md)
  Log a message at the ‘warning’ log level.
- [func warning(@autoclosure () -> Logger.Message, metadata: @autoclosure () -> Logger.Metadata?, source: @autoclosure () -> String?, file: String, function: String, line: UInt)](./logger/warning%28_,metadata,source,file,function,line%29.md)
  Log a message at the ‘warning’ log level with the source that you provide.
- [func warning(@autoclosure () -> Logger.Message, error: @autoclosure () -> (any Error)?, metadata: @autoclosure () -> Logger.Metadata?, source: @autoclosure () -> String?, file: String, function: String, line: UInt)](./logger/warning%28_,error,metadata,source,file,function,line%29.md)
  Log a message at the ‘warning’ log level with the source that you provide.
### Sending error log messages
- [func error(@autoclosure () -> Logger.Message, metadata: @autoclosure () -> Logger.Metadata?, file: String, function: String, line: UInt)](./logger/error%28_,metadata,file,function,line%29.md)
  Log a message at the ‘error’ log level.
- [func error(@autoclosure () -> Logger.Message, metadata: @autoclosure () -> Logger.Metadata?, source: @autoclosure () -> String?, file: String, function: String, line: UInt)](./logger/error%28_,metadata,source,file,function,line%29.md)
  Log a message at the ‘error’ log level with the source that you provide.
- [func error(@autoclosure () -> Logger.Message, error: @autoclosure () -> (any Error)?, metadata: @autoclosure () -> Logger.Metadata?, source: @autoclosure () -> String?, file: String, function: String, line: UInt)](./logger/error%28_,error,metadata,source,file,function,line%29.md)
  Log a message at the ‘error’ log level with the source that you provide.
### Sending critical log messages
- [func critical(@autoclosure () -> Logger.Message, metadata: @autoclosure () -> Logger.Metadata?, file: String, function: String, line: UInt)](./logger/critical%28_,metadata,file,function,line%29.md)
  Log a message at the ‘critical’ log level.
- [func critical(@autoclosure () -> Logger.Message, metadata: @autoclosure () -> Logger.Metadata?, source: @autoclosure () -> String?, file: String, function: String, line: UInt)](./logger/critical%28_,metadata,source,file,function,line%29.md)
  Log a message at the ‘critical’ log level with the source that you provide.
- [func critical(@autoclosure () -> Logger.Message, error: @autoclosure () -> (any Error)?, metadata: @autoclosure () -> Logger.Metadata?, source: @autoclosure () -> String?, file: String, function: String, line: UInt)](./logger/critical%28_,error,metadata,source,file,function,line%29.md)
  Log a message at the ‘critical’ log level with the source that you provide.
### Sending general log messages
- [func log(level: Logger.Level, @autoclosure () -> Logger.Message, metadata: @autoclosure () -> Logger.Metadata?, file: String, function: String, line: UInt)](./logger/log%28level,_,metadata,file,function,line%29.md)
  Log a message using the log level you provide.
- [func log(level: Logger.Level, @autoclosure () -> Logger.Message, metadata: @autoclosure () -> Logger.Metadata?, source: @autoclosure () -> String?, file: String, function: String, line: UInt)](./logger/log%28level,_,metadata,source,file,function,line%29.md)
  Log a message using the log level and source that you provide.
- [func log(level: Logger.Level, @autoclosure () -> Logger.Message, error: @autoclosure () -> (any Error)?, metadata: @autoclosure () -> Logger.Metadata?, source: @autoclosure () -> String?, file: String, function: String, line: UInt)](./logger/log%28level,_,error,metadata,source,file,function,line%29.md)
  Log a message using the log level and source that you provide.
- [Logger.Level](./logger/level.md)
  The log level.
- [Logger.Message](./logger/message.md)
  The content of log message.
- [typealias Metadata](./logger/metadata.md)
  The type of the metadata storage.
### Adjusting logger metadata
- [subscript(metadataKey _: String) -> Logger.Metadata.Value?](./logger/subscript%28metadatakey%29.md)
  Log a message using the log level and attributed metadata that you provide.
- [Logger.MetadataValue](./logger/metadatavalue.md)
  A logging metadata value.
### Metadata attribute types
- [Logger.MetadataValueAttributes](./logger/metadatavalueattributes.md)
  Attributes that can be associated with metadata values.
### Inspecting a logger
- [var label: String](./logger/label.md)
- [var logLevel: Logger.Level](./logger/loglevel.md)
  Get or set the log level configured for this `Logger`.
- [var handler: any LogHandler](./logger/handler.md)
  The log handler.
- [var metadataProvider: Logger.MetadataProvider?](./logger/metadataprovider-swift.property.md)
  The metadata provider this logger was created with.

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Logging API
- [Understanding Loggers and Log Handlers](./understandingloggers.md)
  Learn how to create and configure loggers, set log levels, and use metadata to add context to your log messages.
- [enum LoggingSystem](./loggingsystem.md)
  The logging system is a global facility where you can configure the default logging backend implementation.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger)*
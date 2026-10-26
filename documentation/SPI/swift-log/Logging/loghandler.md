---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/loghandler"
framework: "swift-log/Logging"
---

# LogHandler

**Framework**: swift-log/Logging  
**Kind**: protocol  
**Role**: Protocol

A log handler provides an implementation of a logging backend.

## Declaration

```swift
protocol LogHandler : _SwiftLogSendableLogHandler
```

## Mentions

- [Disable log levels during compilation](./disableloglevelsduringcompilation.md)
- [Implementing a log handler](./implementingaloghandler.md)
- [SLG-NNNN: Feature name](./slg-nnnn.md)

#### Overview

This type is an implementation detail and should not normally be used, unless you implement your own logging backend. To use the SwiftLog API, please refer to the documentation of [`Logger`](./logger.md).

### Implementation requirements

To implement your own `LogHandler` you should respect a few requirements that are necessary so applications work as expected, regardless of the selected `LogHandler` implementation.

- The [`LogHandler`](./loghandler.md) must be a `struct`.
- The metadata and `logLevel` properties must be implemented so that setting them on a `Logger` does not affect other instances of `Logger`.

##### Treat log level & metadata as values

When developing your `LogHandler`, please make sure the following test works.

```swift
@Test
func logHandlerValueSemantics() {
    LoggingSystem.bootstrap(MyLogHandler.init)
    var logger1 = Logger(label: "first logger")
    logger1.logLevel = .debug
    logger1[metadataKey: "only-on"] = "first"

    var logger2 = logger1
    logger2.logLevel = .error                  // Must not affect logger1
    logger2[metadataKey: "only-on"] = "second" // Must not affect logger1

    // These expectations must pass
    #expect(logger1.logLevel == .debug)
    #expect(logger2.logLevel == .error)
    #expect(logger1[metadataKey: "only-on"] == "first")
    #expect(logger2[metadataKey: "only-on"] == "second")
}
```

##### Special cases

In certain special cases, the log level behaving like a value on `Logger` might not be what you want. For example, you might want to set the log level across *all* `Logger`s to `.debug` when a signal (for example `SIGUSR1`) is received to be able to debug special failures in production. This special case is acceptable but please create a solution specific to your `LogHandler` implementation to achieve that.

The following code illustrates an example implementation of this behavior. On reception of the signal you would call `LogHandlerWithGlobalLogLevelOverride.overrideGlobalLogLevel = .debug`, for example.

```swift
import class Foundation.NSLock

public struct LogHandlerWithGlobalLogLevelOverride: LogHandler {
    // The static properties hold the globally overridden
    // log level (if overridden).
    private static let overrideLock = NSLock()
    private static var overrideLogLevel: Logger.Level? = nil

    // this holds the log level if not overridden
    private var _logLevel: Logger.Level = .info

    // metadata storage
    public var metadata: Logger.Metadata = [:]

    public init(label: String) {
        // [...]
    }

    public var logLevel: Logger.Level {
        // When asked for the log level, check
        // if it was globally overridden or not.
        get {
            LogHandlerWithGlobalLogLevelOverride.overrideLock.lock()
            defer { LogHandlerWithGlobalLogLevelOverride.overrideLock.unlock() }
            return LogHandlerWithGlobalLogLevelOverride.overrideLogLevel ?? self._logLevel
        }
        // Set the log level whenever asked
        // (note: this might not have an effect if globally
        // overridden).
        set {
            self._logLevel = newValue
        }
    }

    public func log(event: LogEvent) {
        // [...]
    }

    public subscript(metadataKey metadataKey: String) -> Logger.Metadata.Value? {
        get {
            return self.metadata[metadataKey]
        }
        set(newValue) {
            self.metadata[metadataKey] = newValue
        }
    }

    // This is the function to globally override the log level,
    // it is not part of the `LogHandler` protocol.
    public static func overrideGlobalLogLevel(_ logLevel: Logger.Level) {
        LogHandlerWithGlobalLogLevelOverride.overrideLock.lock()
        defer { LogHandlerWithGlobalLogLevelOverride.overrideLock.unlock() }
        LogHandlerWithGlobalLogLevelOverride.overrideLogLevel = logLevel
    }
}
```

> **Note**: The above `LogHandler` still passes the ‘log level is a value’ test above it if the global log level has not been overridden. Most importantly, it passes the requirement listed above: A change to the log level on one `Logger` should not affect the log level of another `Logger` variable.

## Topics

### Sending log messages
- [func log(event: LogEvent)](./loghandler/log%28event%29.md)
  The library calls this method when a log handler must emit a log message.
- [func log(event: LogEvent)](./loghandler/log%28event%29-17f2r.md)
  Default implementation of [`log(event:)`](./loghandler/log%28event%29-17f2r.md) for backward compatibility with handlers that implement the deprecated flat-parameter method.
- [func log(level: Logger.Level, message: Logger.Message, metadata: Logger.Metadata?, source: String, file: String, function: String, line: UInt)](./loghandler/log%28level,message,metadata,source,file,function,line%29.md)
  Please do *not* implement this method when you create a `LogHandler` implementation. Implement [`log(event:)`](./loghandler/log%28event%29.md) instead.
- [func log(level: Logger.Level, message: Logger.Message, metadata: Logger.Metadata?, source: String, file: String, function: String, line: UInt)](./loghandler/log%28level,message,metadata,source,file,function,line%29-69pez.md)
  A default implementation for a log message handler that forwards to the SwiftLog 1.0 compatibility method.
- [func log(level: Logging.Logger.Level, message: Logging.Logger.Message, metadata: Logging.Logger.Metadata?, file: String, function: String, line: UInt)](./loghandler/log%28level,message,metadata,file,function,line%29.md)
  SwiftLog 1.0 log compatibility method.
- [func log(level: Logging.Logger.Level, message: Logging.Logger.Message, metadata: Logging.Logger.Metadata?, file: String, function: String, line: UInt)](./loghandler/log%28level,message,metadata,file,function,line%29-1xdau.md)
  A default implementation for the SwiftLog 1.0 log message handler.
### Updating metadata
- [subscript(metadataKey _: String) -> Logger.Metadata.Value?](./loghandler/subscript%28metadatakey%29.md)
  Add, remove, or change the logging metadata.
### Inspecting a log handler
- [var logLevel: Logger.Level](./loghandler/loglevel.md)
  Get or set the configured log level.
- [var metadata: Logger.Metadata](./loghandler/metadata.md)
  Get or set the entire metadata storage as a dictionary.
- [var metadataProvider: Logger.MetadataProvider?](./loghandler/metadataprovider.md)
  The metadata provider this log handler uses when a log statement is about to be emitted.

## Relationships

### Inherits From
- Swift.Sendable
- Swift.SendableMetatype
### Conforming Types
- [MultiplexLogHandler](./multiplexloghandler.md)
- [StreamLogHandler](./streamloghandler.md)
- [SwiftLogNoOpLogHandler](./swiftlognooploghandler.md)

## See Also

### Log Handlers
- [struct LogEvent](./logevent.md)
  A log event that contains all the information about a single log statement.
- [struct MultiplexLogHandler](./multiplexloghandler.md)
  A pseudo log handler that sends messages to multiple other log handlers.
- [struct StreamLogHandler](./streamloghandler.md)
  Stream log handler presents log messages to STDERR or STDOUT.
- [struct SwiftLogNoOpLogHandler](./swiftlognooploghandler.md)
  A no-operation log handler, used when no logging is required


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/loghandler)*
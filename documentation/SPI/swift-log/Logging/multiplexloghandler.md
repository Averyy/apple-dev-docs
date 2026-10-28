---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/multiplexloghandler"
framework: "swift-log/Logging"
---

# MultiplexLogHandler

**Framework**: swift-log/Logging  
**Kind**: struct  
**Role**: Structure

A pseudo log handler that sends messages to multiple other log handlers.

## Declaration

```swift
struct MultiplexLogHandler
```

### Effective Logger.Level

When first initialized, the multiplex log handlers’ log level is automatically set to the minimum of all the provided log handlers. This ensures that each of the handlers are able to log at their appropriate level any log events they might be interested in.

Example: If log handler `A` is logging at `.debug` level, and log handler `B` is logging at `.info` level, the log level of the constructed `MultiplexLogHandler([A, B])` is set to `.debug`. This means that this handler will operate on debug messages, while only logged by the underlying `A` log handler (since `B`’s log level is `.info` and thus it would not actually log that log message).

If the log level is *set* on a `Logger` backed by an `MultiplexLogHandler` the log level applies to *all* underlying log handlers, allowing a logger to still select at what level it wants to log regardless of if the underlying handler is a multiplex or a normal one. If for some reason one might want to not allow changing a log level of a specific handler passed into the multiplex log handler, this is possible by wrapping it in a handler which ignores any log level changes.

### Effective Logger.Metadata

Since a `MultiplexLogHandler` is a combination of multiple log handlers, the handling of metadata can be non-obvious. For example, the underlying log handlers may have metadata of their own set before they are used to initialize the multiplex log handler.

The multiplex log handler acts purely as proxy and does not make any changes to underlying handler metadata other than proxying writes that users made on a `Logger` instance backed by this handler.

Setting metadata is always proxied through to *all* underlying handlers, meaning that if a modification like `logger[metadataKey: "x"] = "y"` is made, all the underlying log handlers used to create the multiplex handler observe this change.

Reading metadata from the multiplex log handler MAY need to pick one of conflicting values if the underlying log handlers were previously initiated with metadata before passing them into the multiplex handler. The multiplex handler uses the order in which the handlers were passed in during its initialization as a priority indicator - the first handler’s values are more important than the next handlers values, etc.

Example: If the multiplex log handler was initiated with two handlers like this: `MultiplexLogHandler([handler1, handler2])`. The handlers each have some already set metadata: `handler1` has metadata values for keys `one` and `all`, and `handler2` has values for keys `two` and `all`.

A query through the multiplex log handler the key `one` naturally returns `handler1`’s value, and a query for `two` naturally returns `handler2`’s value. Querying for the key `all` will return `handler1`’s value, as that handler has a high priority, as indicated by its earlier position in the initialization, than the second handler. The same rule applies when querying for the `metadata` property of the multiplex log handler; it constructs `Metadata` uniquing values.

## Topics

### Creating a multiplex log handler
- [init([any LogHandler])](./multiplexloghandler/init%28_%29.md)
  Create a multiplex log handler.
- [init([any LogHandler], metadataProvider: Logger.MetadataProvider?)](./multiplexloghandler/init%28_,metadataprovider%29.md)
  Create a multiplex log handler with the metadata provider you provide.
### Sending log messages
- [func log(event: LogEvent)](./multiplexloghandler/log%28event%29.md)
  Log a message using the log level and source that you provide.
- [func log(level: Logger.Level, message: Logger.Message, metadata: Logger.Metadata?, source: String, file: String, function: String, line: UInt)](./multiplexloghandler/log%28level,message,metadata,source,file,function,line%29.md)
### Updating metadata
- [subscript(metadataKey _: Logger.Metadata.Key) -> Logger.Metadata.Value?](./multiplexloghandler/subscript%28metadatakey%29.md)
  Add, change, or remove a logging metadata item.
### Inspecting a log handler
- [var logLevel: Logger.Level](./multiplexloghandler/loglevel.md)
  Get or set the log level configured for this `Logger`.
- [var metadata: Logger.Metadata](./multiplexloghandler/metadata.md)
  Get or set the entire metadata storage as a dictionary.
- [var metadataProvider: Logger.MetadataProvider?](./multiplexloghandler/metadataprovider.md)
  The metadata provider.
### Default Implementations
- [LogHandler Implementations](./multiplexloghandler/loghandler-implementations.md)

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
- [struct StreamLogHandler](./streamloghandler.md)
  Stream log handler presents log messages to STDERR or STDOUT.
- [struct SwiftLogNoOpLogHandler](./swiftlognooploghandler.md)
  A no-operation log handler, used when no logging is required


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/multiplexloghandler)*
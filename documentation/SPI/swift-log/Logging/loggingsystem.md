---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/loggingsystem"
framework: "swift-log/Logging"
---

# LoggingSystem

**Framework**: swift-log/Logging  
**Kind**: enum  
**Role**: Enumeration

The logging system is a global facility where you can configure the default logging backend implementation.

## Declaration

```swift
enum LoggingSystem
```

#### Overview

`LoggingSystem` is set up just once in a given program to set up the desired logging backend implementation. The default behavior, if you don’t define otherwise, sets the [`LogHandler`](./loghandler.md) to use a [`StreamLogHandler`](./streamloghandler.md) that presents its output to `STDOUT`.

You can configure that handler to present the output to `STDERR` instead using the following code:

```swift
LoggingSystem.bootstrap(StreamLogHandler.standardError)
```

The default ([`StreamLogHandler`](./streamloghandler.md)) is intended to be a convenience. For production applications, implement the [`LogHandler`](./loghandler.md) protocol directly, or use a community-maintained backend.

## Topics

### Initializing the logging system
- [static func bootstrap(@Sendable (String) -> any LogHandler)](./loggingsystem/bootstrap%28_%29.md)
  A one-time configuration function that globally selects the implementation for your desired logging backend.
- [static func bootstrap(@Sendable (String, Logger.MetadataProvider?) -> any LogHandler, metadataProvider: Logger.MetadataProvider?)](./loggingsystem/bootstrap%28_,metadataprovider%29.md)
  A one-time configuration function that globally selects the implementation for your desired logging backend.
### Inspecting the logging system
- [static var metadataProvider: Logger.MetadataProvider?](./loggingsystem/metadataprovider.md)
  System wide [`Logger.MetadataProvider`](./logger/metadataprovider-swift.struct.md) that was configured during the logging system’s `bootstrap`.

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Logging API
- [Understanding Loggers and Log Handlers](./understandingloggers.md)
  Learn how to create and configure loggers, set log levels, and use metadata to add context to your log messages.
- [struct Logger](./logger.md)
  A Logger emits log messages using methods that correspond to a log level.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/loggingsystem)*
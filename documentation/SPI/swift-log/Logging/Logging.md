---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging"
framework: "swift-log/Logging"
---

# Logging

**Framework**: swift-log/Logging  
**Kind**: module  
**Role**: Framework

A unified, performant, and ergonomic logging API for Swift.

## Overview

SwiftLog provides a logging API package designed to establish a common API the ecosystem can use. It allows packages to emit log messages without tying them to any specific logging implementation, while applications can choose any compatible logging backend.

SwiftLog is an *API package* which cuts the logging problem in half:

1. A logging API (this package)
2. Logging backend implementations (community-provided)

This separation allows libraries to adopt the API while applications choose any compatible logging backend implementation without requiring changes from libraries.

### Getting Started

Use this package if you’re writing a cross-platform application (for example, Linux and macOS) or library, and want to target this logging API.

### Adding the Dependency

Add the dependency to your `Package.swift`:

```swift
.package(url: "https://github.com/apple/swift-log", from: "1.6.0")
```

And to your target:

```swift
.target(
    name: "YourTarget",
    dependencies: [
        .product(name: "Logging", package: "swift-log")
    ]
)
```

### Basic Usage

```swift
// Import the logging API
import Logging

// Create a logger with a label
let logger = Logger(label: "MyLogger")

// Use it to log messages
logger.info("Hello World!")
```

This outputs:

```
2025-10-24T17:26:47-0700 info MyLogger: [your_app] Hello World!
```

### Default Behavior

SwiftLog provides basic console logging via [`StreamLogHandler`](./streamloghandler.md). By default it uses `stdout`, however, you can configure it to use `stderr` instead:

```swift
LoggingSystem.bootstrap(StreamLogHandler.standardError)
```

[`StreamLogHandler`](./streamloghandler.md) is primarily for convenience. For production applications, implement the [`LogHandler`](./loghandler.md) protocol directly or use a community-maintained backend.

## Topics

### Logging API
- [Understanding Loggers and Log Handlers](./understandingloggers.md)
  Learn how to create and configure loggers, set log levels, and use metadata to add context to your log messages.
- [struct Logger](./logger.md)
  A Logger emits log messages using methods that correspond to a log level.
- [enum LoggingSystem](./loggingsystem.md)
  The logging system is a global facility where you can configure the default logging backend implementation.
### Log Handlers
- [protocol LogHandler](./loghandler.md)
  A log handler provides an implementation of a logging backend.
- [struct LogEvent](./logevent.md)
  A log event that contains all the information about a single log statement.
- [struct MultiplexLogHandler](./multiplexloghandler.md)
  A pseudo log handler that sends messages to multiple other log handlers.
- [struct StreamLogHandler](./streamloghandler.md)
  Stream log handler presents log messages to STDERR or STDOUT.
- [struct SwiftLogNoOpLogHandler](./swiftlognooploghandler.md)
  A no-operation log handler, used when no logging is required
### Best Practices
- [Logging best practices](./loggingbestpractices.md)
  Best practices for effective logging with SwiftLog.
- [Implementing a log handler](./implementingaloghandler.md)
  Create a custom logging backend that provides logging services for your apps and libraries.
- [Disable log levels during compilation](./disableloglevelsduringcompilation.md)
  SwiftLog provides compile-time traits to eliminate less severe log levels from your binary reducing the runtime overhead.
### Contributing
- [Proposals](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/proposals)
  Collaborate on API changes to SwiftLog by writing a proposal.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging)*
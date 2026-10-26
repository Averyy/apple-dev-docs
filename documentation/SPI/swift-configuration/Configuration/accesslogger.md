---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/accesslogger"
framework: "swift-configuration/Configuration"
---

# AccessLogger

**Framework**: swift-configuration/Configuration  
**Kind**: class  
**Role**: Class

An access reporter that logs configuration access events using the Swift Log API.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
final class AccessLogger
```

## Mentions

- [Handling secrets correctly](./handling-secrets-correctly.md)
- [Migrating to Swift Configuration](./migrating-to-swift-configuration.md)
- [Troubleshooting and access reporting](./troubleshooting.md)
- [Configuring libraries](./configuring-libraries.md)

#### Overview

This reporter integrates with the Swift Log library to provide structured logging of configuration accesses. Each configuration access generates a log entry with detailed metadata about the operation, making it easy to track configuration usage and debug issues.

#### Package traits

This type is guarded by the `Logging` package trait.

#### Usage

Create an access logger and pass it to your configuration reader:

```swift
import Logging

let logger = Logger(label: "config.access")
let accessLogger = AccessLogger(logger: logger, level: .info)
let config = ConfigReader(
    provider: EnvironmentVariablesProvider(),
    accessReporter: accessLogger
)
```

#### Log format

Each access event generates a structured log entry with metadata including:

- `kind`: The type of access operation (get, fetch, watch).
- `key`: The configuration key accessed.
- `location`: The source code location of the access.
- `value`: The resolved configuration value (redacted for secrets).
- `counter`: An incrementing counter for tracking access frequency.
- Provider-specific information for each provider in the hierarchy.

## Topics

### Creating an access logger
- [init(logger: Logger, level: Logger.Level, message: Logger.Message)](./accesslogger/init%28logger,level,message%29.md)
  Creates a new access logger that reports configuration access events.
### Default Implementations
- [AccessReporter Implementations](./accesslogger/accessreporter-implementations.md)

## Relationships

### Conforms To
- [AccessReporter](./accessreporter.md)
- Swift.Copyable
- Swift.Escapable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Troubleshooting and access reporting
- [Troubleshooting and access reporting](./troubleshooting.md)
  Check out some techniques to debug unexpected issues and to increase visibility into accessed config values.
- [protocol AccessReporter](./accessreporter.md)
  A type that receives and processes configuration access events.
- [class FileAccessLogger](./fileaccesslogger.md)
  An access reporter that writes configuration access events to a file.
- [struct AccessEvent](./accessevent.md)
  An event that captures information about accessing a configuration value.
- [struct BroadcastingAccessReporter](./broadcastingaccessreporter.md)
  An access reporter that forwards events to multiple other reporters.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/accesslogger)*
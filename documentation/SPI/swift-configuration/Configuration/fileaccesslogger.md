---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/fileaccesslogger"
framework: "swift-configuration/Configuration"
---

# FileAccessLogger

**Framework**: swift-configuration/Configuration  
**Kind**: class  
**Role**: Class

An access reporter that writes configuration access events to a file.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
final class FileAccessLogger
```

## Mentions

- [Handling secrets correctly](./handling-secrets-correctly.md)
- [Troubleshooting and access reporting](./troubleshooting.md)
- [Configuring libraries](./configuring-libraries.md)

## Overview

This reporter provides persistent logging of configuration access patterns by writing structured event summaries to a file. Each access generates a single-line entry with timestamp, key, value, and provider information, making it easy to analyze configuration usage patterns and debug issues in production.

## Usage

Create a file access logger and pass it to your configuration reader:

```swift
let logger = try FileAccessLogger(filePath: "/tmp/config-access.log")
let config = ConfigReader(
    provider: EnvironmentVariablesProvider(),
    accessReporter: logger
)
```

## Environment variable activation

The file access logger can be automatically enabled for the entire process using the `CONFIG_ACCESS_LOG_FILE` environment variable:

```bash
CONFIG_ACCESS_LOG_FILE=/tmp/access.log ./my-app
```

This allows operators to enable configuration access logging without recompiling the application, making it useful for debugging production issues.

## Log format

Each access event generates a single-line entry with the format:

```swift
✅ database.host -> "localhost" - provided by EnvironmentVariablesProvider / Get String from main.swift:42 at 2024-01-15T10:30:45.123Z
```

The log entries include:

- Status emoji (✅ success, 🟡 default/nil, ❌ error).
- Configuration key accessed.
- Resolved value (redacted for secrets).
- Provider that supplied the value or error information.
- Access metadata (operation type, value type, source location, timestamp).

## Topics

### Creating a file access logger
- [convenience init(filePath: FilePath, timeZone: TimeZone) throws](./fileaccesslogger/init%28filepath,timezone%29.md)
  Creates a new file access logger that writes to the specified file path.
### Default Implementations
- [AccessReporter Implementations](./fileaccesslogger/accessreporter-implementations.md)

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
- [class AccessLogger](./accesslogger.md)
  An access reporter that logs configuration access events using the Swift Log API.
- [struct AccessEvent](./accessevent.md)
  An event that captures information about accessing a configuration value.
- [struct BroadcastingAccessReporter](./broadcastingaccessreporter.md)
  An access reporter that forwards events to multiple other reporters.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/fileaccesslogger)*
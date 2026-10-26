---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/broadcastingaccessreporter"
framework: "swift-configuration/Configuration"
---

# BroadcastingAccessReporter

**Framework**: swift-configuration/Configuration  
**Kind**: struct  
**Role**: Structure

An access reporter that forwards events to multiple other reporters.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct BroadcastingAccessReporter
```

#### Overview

Use this reporter to send configuration access events to multiple destinations simultaneously. Each upstream reporter receives a copy of every event in the order you provide during initialization.

```swift
let fileLogger = try FileAccessLogger(filePath: "/tmp/config.log")
let accessLogger = AccessLogger(logger: logger)
let broadcaster = BroadcastingAccessReporter(upstreams: [fileLogger, accessLogger])

let config = ConfigReader(
    provider: EnvironmentVariablesProvider(),
    accessReporter: broadcaster
)
```

## Topics

### Creating a broadcasting access reporter
- [init(upstreams: [any AccessReporter])](./broadcastingaccessreporter/init%28upstreams%29.md)
  Creates a new broadcasting access reporter.
### Default Implementations
- [AccessReporter Implementations](./broadcastingaccessreporter/accessreporter-implementations.md)

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
- [class FileAccessLogger](./fileaccesslogger.md)
  An access reporter that writes configuration access events to a file.
- [struct AccessEvent](./accessevent.md)
  An event that captures information about accessing a configuration value.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/broadcastingaccessreporter)*
---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/accessreporter"
framework: "swift-configuration/Configuration"
---

# AccessReporter

**Framework**: swift-configuration/Configuration  
**Kind**: protocol  
**Role**: Protocol

A type that receives and processes configuration access events.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
protocol AccessReporter : Sendable
```

## Mentions

- [Troubleshooting and access reporting](./troubleshooting.md)
- [Choosing the access pattern](./choosing-access-patterns.md)
- [Configuring libraries](./configuring-libraries.md)

## Overview

Access reporters track when configuration values are read, fetched, or watched, to provide visibility into configuration usage patterns. This is useful for debugging, auditing, and understanding configuration dependencies.

## Topics

### Required methods
- [func report(AccessEvent)](./accessreporter/report%28_%29.md)
  Processes a configuration access event.

## Relationships

### Inherits From
- Swift.Sendable
- Swift.SendableMetatype
### Conforming Types
- [AccessLogger](./accesslogger.md)
- [BroadcastingAccessReporter](./broadcastingaccessreporter.md)
- [FileAccessLogger](./fileaccesslogger.md)

## See Also

### Troubleshooting and access reporting
- [Troubleshooting and access reporting](./troubleshooting.md)
  Check out some techniques to debug unexpected issues and to increase visibility into accessed config values.
- [class AccessLogger](./accesslogger.md)
  An access reporter that logs configuration access events using the Swift Log API.
- [class FileAccessLogger](./fileaccesslogger.md)
  An access reporter that writes configuration access events to a file.
- [struct AccessEvent](./accessevent.md)
  An event that captures information about accessing a configuration value.
- [struct BroadcastingAccessReporter](./broadcastingaccessreporter.md)
  An access reporter that forwards events to multiple other reporters.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/accessreporter)*
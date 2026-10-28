---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/accessevent"
framework: "swift-configuration/Configuration"
---

# AccessEvent

**Framework**: swift-configuration/Configuration  
**Kind**: struct  
**Role**: Structure

An event that captures information about accessing a configuration value.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct AccessEvent
```

## Overview

Access events are generated whenever configuration values are accessed through [`ConfigReader`](./configreader.md) and [`ConfigSnapshotReader`](./configsnapshotreader.md) methods. They contain metadata about the access, results from individual providers, and the final outcome of the operation.

## Topics

### Creating an access event
- [init(metadata: AccessEvent.Metadata, providerResults: [AccessEvent.ProviderResult], conversionError: (any Error)?, result: Result<ConfigValue?, any Error>)](./accessevent/init%28metadata,providerresults,conversionerror,result%29.md)
  Creates a configuration access event.
- [AccessEvent.Metadata](./accessevent/metadata-swift.struct.md)
  Metadata describing the configuration access operation.
- [AccessEvent.ProviderResult](./accessevent/providerresult.md)
  The result of a configuration lookup from a specific provider.
### Inspecting an access event
- [var result: Result<ConfigValue?, any Error>](./accessevent/result.md)
  The final outcome of the configuration access operation.
- [var conversionError: (any Error)?](./accessevent/conversionerror.md)
  An error that occurred when converting the raw config value into another type, for example `RawRepresentable`.
- [var metadata: AccessEvent.Metadata](./accessevent/metadata-swift.property.md)
  Metadata that describes the configuration access operation.
- [var providerResults: [AccessEvent.ProviderResult]](./accessevent/providerresults.md)
  The results from each configuration provider queried.
### Default Implementations
- [CustomStringConvertible Implementations](./accessevent/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- Swift.Copyable
- Swift.CustomStringConvertible
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
- [struct BroadcastingAccessReporter](./broadcastingaccessreporter.md)
  An access reporter that forwards events to multiple other reporters.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/accessevent)*
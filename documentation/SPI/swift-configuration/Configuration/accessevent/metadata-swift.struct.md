---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/accessevent/metadata-swift.struct"
framework: "swift-configuration/Configuration"
---

# AccessEvent.Metadata

**Framework**: swift-configuration/Configuration  
**Kind**: struct  
**Role**: Structure

Metadata describing the configuration access operation.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct Metadata
```

## Overview

Contains information about the type of access, the key accessed, value type, source location, and timestamp.

## Topics

### Creating access event metadata
- [init(accessKind: AccessEvent.Metadata.AccessKind, key: AbsoluteConfigKey, valueType: ConfigType, sourceLocation: AccessEvent.Metadata.SourceLocation, accessTimestamp: Date)](./metadata-swift.struct/init%28accesskind,key,valuetype,sourcelocation,accesstimestamp%29.md)
  Creates access event metadata.
- [AccessEvent.Metadata.AccessKind](./metadata-swift.struct/accesskind-swift.enum.md)
  The type of configuration access operation.
### Inspecting access event metadata
- [var accessKind: AccessEvent.Metadata.AccessKind](./metadata-swift.struct/accesskind-swift.property.md)
  The type of configuration access operation for this event.
- [var accessTimestamp: Date](./metadata-swift.struct/accesstimestamp.md)
  The timestamp when the configuration access occurs.
- [var key: AbsoluteConfigKey](./metadata-swift.struct/key.md)
  The configuration key accessed.
- [var sourceLocation: AccessEvent.Metadata.SourceLocation](./metadata-swift.struct/sourcelocation-swift.property.md)
  The source code location where the access occurs.
- [var valueType: ConfigType](./metadata-swift.struct/valuetype.md)
  The expected type of the configuration value.
### Structures
- [AccessEvent.Metadata.SourceLocation](./metadata-swift.struct/sourcelocation-swift.struct.md)
  The source code location where a configuration access occurs.

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Creating an access event
- [init(metadata: AccessEvent.Metadata, providerResults: [AccessEvent.ProviderResult], conversionError: (any Error)?, result: Result<ConfigValue?, any Error>)](./init%28metadata,providerresults,conversionerror,result%29.md)
  Creates a configuration access event.
- [AccessEvent.ProviderResult](./providerresult.md)
  The result of a configuration lookup from a specific provider.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/accessevent/metadata-swift.struct)*
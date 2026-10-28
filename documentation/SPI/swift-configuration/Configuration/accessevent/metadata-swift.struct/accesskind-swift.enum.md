---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/accessevent/metadata-swift.struct/accesskind-swift.enum"
framework: "swift-configuration/Configuration"
---

# AccessEvent.Metadata.AccessKind

**Framework**: swift-configuration/Configuration  
**Kind**: enum  
**Role**: Enumeration

The type of configuration access operation.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
@frozen
enum AccessKind
```

## Overview

Indicates whether the access is a synchronous get, asynchronous fetch, or an async watch operation.

## Topics

### Kinds of configuration access
- [AccessEvent.Metadata.AccessKind.get](./accesskind-swift.enum/get.md)
  A synchronous get operation that returns the current value.
- [AccessEvent.Metadata.AccessKind.fetch](./accesskind-swift.enum/fetch.md)
  An asynchronous fetch operation that retrieves the latest value.
- [AccessEvent.Metadata.AccessKind.watch](./accesskind-swift.enum/watch.md)
  An asynchronous watch operation that monitors value changes.
### Initializers
- [init?(rawValue: String)](./accesskind-swift.enum/init%28rawvalue%29.md)
### Default Implementations
- [Equatable Implementations](./accesskind-swift.enum/equatable-implementations.md)
- [RawRepresentable Implementations](./accesskind-swift.enum/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- Swift.BitwiseCopyable
- Swift.Equatable
- Swift.Hashable
- Swift.RawRepresentable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Creating access event metadata
- [init(accessKind: AccessEvent.Metadata.AccessKind, key: AbsoluteConfigKey, valueType: ConfigType, sourceLocation: AccessEvent.Metadata.SourceLocation, accessTimestamp: Date)](./init%28accesskind,key,valuetype,sourcelocation,accesstimestamp%29.md)
  Creates access event metadata.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/accessevent/metadata-swift.struct/accesskind-swift.enum)*
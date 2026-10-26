---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/accessevent/metadata-swift.struct/init(accesskind:key:valuetype:sourcelocation:accesstimestamp:)"
framework: "swift-configuration/Configuration"
---

# init(accessKind:key:valueType:sourceLocation:accessTimestamp:)

**Framework**: swift-configuration/Configuration  
**Kind**: init  
**Role**: Initializer

Creates access event metadata.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(accessKind: AccessEvent.Metadata.AccessKind, key: AbsoluteConfigKey, valueType: ConfigType, sourceLocation: AccessEvent.Metadata.SourceLocation, accessTimestamp: Date)
```

## Parameters

- `accessKind`: The type of configuration access operation.
- `key`: The configuration key accessed.
- `valueType`: The expected type of the configuration value.
- `sourceLocation`: The source code location where the access occurs.
- `accessTimestamp`: The timestamp when the access occurs.

## See Also

### Creating access event metadata
- [AccessEvent.Metadata.AccessKind](./accesskind-swift.enum.md)
  The type of configuration access operation.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/accessevent/metadata-swift.struct/init(accesskind:key:valuetype:sourcelocation:accesstimestamp:))*
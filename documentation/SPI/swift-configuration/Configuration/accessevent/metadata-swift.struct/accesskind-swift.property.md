---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/accessevent/metadata-swift.struct/accesskind-swift.property"
framework: "swift-configuration/Configuration"
---

# accessKind

**Framework**: swift-configuration/Configuration  
**Kind**: property  
**Role**: Instance Property

The type of configuration access operation for this event.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var accessKind: AccessEvent.Metadata.AccessKind
```

## See Also

### Inspecting access event metadata
- [var accessTimestamp: Date](./accesstimestamp.md)
  The timestamp when the configuration access occurs.
- [var key: AbsoluteConfigKey](./key.md)
  The configuration key accessed.
- [var sourceLocation: AccessEvent.Metadata.SourceLocation](./sourcelocation-swift.property.md)
  The source code location where the access occurs.
- [var valueType: ConfigType](./valuetype.md)
  The expected type of the configuration value.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/accessevent/metadata-swift.struct/accesskind-swift.property)*
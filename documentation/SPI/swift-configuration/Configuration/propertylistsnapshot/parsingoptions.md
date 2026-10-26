---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/propertylistsnapshot/parsingoptions"
framework: "swift-configuration/Configuration"
---

# PropertyListSnapshot.ParsingOptions

**Framework**: swift-configuration/Configuration  
**Kind**: struct  
**Role**: Structure

Parsing options for property list snapshot creation.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct ParsingOptions
```

#### Overview

This struct provides configuration options for parsing plist data into configuration snapshots.

## Topics

### Initializers
- [init(secretsSpecifier: SecretsSpecifier<String, any Sendable>)](./parsingoptions/init%28secretsspecifier%29.md)
  Creates parsing options for plist snapshots.
### Instance Properties
- [var secretsSpecifier: SecretsSpecifier<String, any Sendable>](./parsingoptions/secretsspecifier.md)
  A specifier for determining which configuration values should be treated as secrets.
### Type Properties
- [static var `default`: PropertyListSnapshot.ParsingOptions](./parsingoptions/default.md)
  The default parsing options.

## Relationships

### Conforms To
- [FileParsingOptions](../fileparsingoptions.md)
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Creating a property list snapshot
- [init(data: RawSpan, providerName: String, parsingOptions: PropertyListSnapshot.ParsingOptions) throws](./init%28data,providername,parsingoptions%29.md)
  Creates a new snapshot from file data.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/propertylistsnapshot/parsingoptions)*
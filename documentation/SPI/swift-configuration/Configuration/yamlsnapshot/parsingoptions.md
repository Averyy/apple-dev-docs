---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/yamlsnapshot/parsingoptions"
framework: "swift-configuration/Configuration"
---

# YAMLSnapshot.ParsingOptions

**Framework**: swift-configuration/Configuration  
**Kind**: struct  
**Role**: Structure

Custom input configuration for YAML snapshot creation.

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

This struct provides configuration options for parsing YAML data into configuration snapshots, including byte decoding and secrets specification.

## Topics

### Initializers
- [init(bytesDecoder: some ConfigBytesFromStringDecoder, secretsSpecifier: SecretsSpecifier<String, Void>)](./parsingoptions/init%28bytesdecoder,secretsspecifier%29.md)
  Creates custom input configuration for YAML snapshots.
### Instance Properties
- [var bytesDecoder: any ConfigBytesFromStringDecoder](./parsingoptions/bytesdecoder.md)
  A decoder of bytes from a string.
- [var secretsSpecifier: SecretsSpecifier<String, Void>](./parsingoptions/secretsspecifier.md)
  A specifier for determining which configuration values should be treated as secrets.
### Type Properties
- [static var `default`: YAMLSnapshot.ParsingOptions](./parsingoptions/default.md)
  The default custom input configuration.

## Relationships

### Conforms To
- [FileParsingOptions](../fileparsingoptions.md)
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Creating a YAML snapshot
- [convenience init(data: RawSpan, providerName: String, parsingOptions: YAMLSnapshot.ParsingOptions) throws](./init%28data,providername,parsingoptions%29.md)
  Creates a new snapshot from file data.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/yamlsnapshot/parsingoptions)*
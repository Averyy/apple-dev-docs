---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/fileparsingoptions"
framework: "swift-configuration/Configuration"
---

# FileParsingOptions

**Framework**: swift-configuration/Configuration  
**Kind**: protocol  
**Role**: Protocol

A type that provides parsing options for file configuration snapshots.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
protocol FileParsingOptions : Sendable
```

## Overview

This protocol defines the requirements for parsing options types used with [`FileConfigSnapshot`](./fileconfigsnapshot.md) implementations. Types conforming to this protocol provide configuration parameters that control how file data is interpreted and parsed during snapshot creation.

The parsing options are passed to the [`init(data:providerName:parsingOptions:)`](./fileconfigsnapshot/init%28data,providername,parsingoptions%29.md) initializer, allowing custom file format implementations to access format-specific parsing settings such as character encoding, date formats, or validation rules.

## Usage

Implement this protocol to provide parsing options for your custom [`FileConfigSnapshot`](./fileconfigsnapshot.md):

```swift
struct MyParsingOptions: FileParsingOptions {
    let encoding: String.Encoding
    let dateFormat: String?
    let strictValidation: Bool

    static let `default` = MyParsingOptions(
        encoding: .utf8,
        dateFormat: nil,
        strictValidation: false
    )
}

struct MyFormatSnapshot: FileConfigSnapshot {
    typealias ParsingOptions = MyParsingOptions

    init(data: RawSpan, providerName: String, parsingOptions: ParsingOptions) throws {
        // Implementation that inspects `parsingOptions` properties like `encoding`,
        // `dateFormat`, and `strictValidation`.
    }
}
```

## Topics

### Required properties
- [static var `default`: Self](./fileparsingoptions/default.md)
  The default instance of this options type.
### Parsing options
- [protocol FileConfigSnapshot](./fileconfigsnapshot.md)
  A protocol for configuration snapshots created from file data.

## Relationships

### Inherits From
- Swift.Sendable
- Swift.SendableMetatype
### Conforming Types
- [JSONSnapshot.ParsingOptions](./jsonsnapshot/parsingoptions.md)
- [PropertyListSnapshot.ParsingOptions](./propertylistsnapshot/parsingoptions.md)
- [YAMLSnapshot.ParsingOptions](./yamlsnapshot/parsingoptions.md)

## See Also

### Creating a custom provider
- [Implementing a custom provider](./implementing-a-provider.md)
  Create a custom configuration provider to integrate a new data source.
- [protocol ConfigSnapshot](./configsnapshot.md)
  An immutable snapshot of a configuration provider’s state.
- [protocol FileConfigSnapshot](./fileconfigsnapshot.md)
  A protocol for configuration snapshots created from file data.
- [protocol ConfigProvider](./configprovider.md)
  A type that provides configuration values from a data source.
- [enum ConfigContent](./configcontent.md)
  The raw content of a configuration value.
- [struct ConfigValue](./configvalue.md)
  A configuration value that wraps content with metadata.
- [enum ConfigType](./configtype.md)
  The supported configuration value types.
- [struct LookupResult](./lookupresult.md)
  The result of looking up a configuration value in a provider.
- [enum SecretsSpecifier](./secretsspecifier.md)
  A specification for identifying which configuration values contain sensitive information.
- [struct ConfigUpdatesAsyncSequence](./configupdatesasyncsequence.md)
  A concrete async sequence for delivering updated configuration values.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/fileparsingoptions)*
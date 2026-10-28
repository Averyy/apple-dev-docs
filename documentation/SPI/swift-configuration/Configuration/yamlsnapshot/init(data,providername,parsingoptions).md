---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/yamlsnapshot/init(data:providername:parsingoptions:)"
framework: "swift-configuration/Configuration"
---

# init(data:providerName:parsingOptions:)

**Framework**: swift-configuration/Configuration  
**Kind**: init  
**Role**: Initializer

Creates a new snapshot from file data.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
convenience init(data: RawSpan, providerName: String, parsingOptions: YAMLSnapshot.ParsingOptions) throws
```

## Discussion

This initializer parses the provided file data and creates a snapshot containing the configuration values found in the file.

> **Throws**: If the file data cannot be parsed or contains invalid configuration.

## Parameters

- `data`: The raw file data to parse.
- `providerName`: The name of the provider creating this snapshot.
- `parsingOptions`: Parsing options that affect parsing behavior.

## See Also

### Creating a YAML snapshot
- [YAMLSnapshot.ParsingOptions](./parsingoptions.md)
  Custom input configuration for YAML snapshot creation.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/yamlsnapshot/init(data:providername:parsingoptions:))*
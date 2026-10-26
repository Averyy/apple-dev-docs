---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/fileprovider/init(snapshottype:parsingoptions:config:)"
framework: "swift-configuration/Configuration"
---

# init(snapshotType:parsingOptions:config:)

**Framework**: swift-configuration/Configuration  
**Kind**: init  
**Role**: Initializer

Creates a file provider using a file path from a configuration reader.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(snapshotType: Snapshot.Type = Snapshot.self, parsingOptions: Snapshot.ParsingOptions = .default, config: ConfigReader) async throws
```

#### Discussion

This initializer reads the file path from the provided configuration reader and creates a snapshot from that file.

#### Configuration keys

- `filePath` (string, required): The path to the configuration file to read.
- `allowMissing` (bool, optional, default: false): A flag controlling how the provider handles a missing file. When `false` (the default), if the file is missing or malformed, throws an error. When `true`, if the file is missing, treats it as empty. Malformed files still throw an error.

> **Throws**: If snapshot creation fails or if the file is malformed. Whether an error is thrown when the file is missing is controlled by the `allowMissing` configuration value.

## Parameters

- `snapshotType`: The type of snapshot to create from the file contents.
- `parsingOptions`: Options used by the snapshot to parse the file data.
- `config`: A configuration reader that contains the required configuration keys.

## See Also

### Creating a file provider
- [init(snapshotType: Snapshot.Type, parsingOptions: Snapshot.ParsingOptions, filePath: FilePath, allowMissing: Bool) async throws](./init%28snapshottype,parsingoptions,filepath,allowmissing%29.md)
  Creates a file provider that reads from the specified file path.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/fileprovider/init(snapshottype:parsingoptions:config:))*
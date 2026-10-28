---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/fileprovider/init(snapshottype:parsingoptions:filepath:allowmissing:)"
framework: "swift-configuration/Configuration"
---

# init(snapshotType:parsingOptions:filePath:allowMissing:)

**Framework**: swift-configuration/Configuration  
**Kind**: init  
**Role**: Initializer

Creates a file provider that reads from the specified file path.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(snapshotType: Snapshot.Type = Snapshot.self, parsingOptions: Snapshot.ParsingOptions = .default, filePath: FilePath, allowMissing: Bool = false) async throws
```

## Discussion

This initializer reads the file at the given path and creates a snapshot using the specified snapshot type. The file is read once during initialization.

> **Throws**: If snapshot creation fails or if the file is malformed. Whether an error is thrown when the file is missing is controlled by the `allowMissing` parameter.

## Parameters

- `snapshotType`: The type of snapshot to create from the file contents.
- `parsingOptions`: Options used by the snapshot to parse the file data.
- `filePath`: The path to the configuration file to read.
- `allowMissing`: A flag controlling how the provider handles a missing file.

  - When `false` (the default), if the file is missing or malformed, throws an error.
  - When `true`, if the file is missing, treats it as empty. Malformed files still throw an error.

## See Also

### Creating a file provider
- [init(snapshotType: Snapshot.Type, parsingOptions: Snapshot.ParsingOptions, config: ConfigReader) async throws](./init%28snapshottype,parsingoptions,config%29.md)
  Creates a file provider using a file path from a configuration reader.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/fileprovider/init(snapshottype:parsingoptions:filepath:allowmissing:))*
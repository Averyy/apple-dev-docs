---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/directoryfilesprovider/init(directorypath:allowmissing:secretsspecifier:arrayseparator:)"
framework: "swift-configuration/Configuration"
---

# init(directoryPath:allowMissing:secretsSpecifier:arraySeparator:)

**Framework**: swift-configuration/Configuration  
**Kind**: init  
**Role**: Initializer

Creates a new provider that reads files from a directory.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(directoryPath: FilePath, allowMissing: Bool = false, secretsSpecifier: SecretsSpecifier<String, Data> = .all, arraySeparator: Character = ",") async throws
```

#### Discussion

This initializer scans the specified directory and loads all regular files as configuration values. Subdirectories are not traversed. Hidden files (starting with a dot) are skipped.

```swift
// Load configuration from a directory
let provider = try await DirectoryFilesProvider(
    directoryPath: "/run/secrets"
)
```

> **Throws**: If the directory doesn’t exist or is unreadable.

## Parameters

- `directoryPath`: The file system path to the directory containing configuration files.
- `allowMissing`: A flag controlling how the provider handles a missing directory.

  - When `false`, if the directory is missing, throws an error.
  - When `true`, if the directory is missing, treats it as empty.
- `secretsSpecifier`: Specifies which values should be treated as secrets.
- `arraySeparator`: The character used to separate elements in array values.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/directoryfilesprovider/init(directorypath:allowmissing:secretsspecifier:arrayseparator:))*
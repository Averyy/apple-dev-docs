---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/reloadingfileprovider/init(snapshottype:parsingoptions:filepath:allowmissing:pollinterval:logger:metrics:)"
framework: "swift-configuration/Configuration"
---

# init(snapshotType:parsingOptions:filePath:allowMissing:pollInterval:logger:metrics:)

**Framework**: swift-configuration/Configuration  
**Kind**: init  
**Role**: Initializer

Creates a reloading file provider that monitors the specified file path.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
convenience init(snapshotType: Snapshot.Type = Snapshot.self, parsingOptions: Snapshot.ParsingOptions = .default, filePath: FilePath, allowMissing: Bool = false, pollInterval: Duration = .seconds(15), logger: Logger = Logger(label: "ReloadingFileProvider"), metrics: any MetricsFactory = MetricsSystem.factory) async throws
```

## Discussion

> **Throws**: If the file cannot be read or if snapshot creation fails.

## Parameters

- `snapshotType`: The type of snapshot to create from the file contents.
- `parsingOptions`: Options used by the snapshot to parse the file data.
- `filePath`: The path to the configuration file to monitor.
- `allowMissing`: A flag controlling how the provider handles a missing file.

  - When `false` (the default), if the file is missing or malformed, throws an error.
  - When `true`, if the file is missing, treats it as empty. Malformed files still throw an error.
- `pollInterval`: How often to check for file changes.
- `logger`: The logger instance to use for this provider.
- `metrics`: The metrics factory to use for monitoring provider performance.

## See Also

### Creating a reloading file provider
- [convenience init(snapshotType: Snapshot.Type, parsingOptions: Snapshot.ParsingOptions, config: ConfigReader, logger: Logger, metrics: any MetricsFactory) async throws](./init%28snapshottype,parsingoptions,config,logger,metrics%29.md)
  Creates a reloading file provider using configuration from a reader.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/reloadingfileprovider/init(snapshottype:parsingoptions:filepath:allowmissing:pollinterval:logger:metrics:))*
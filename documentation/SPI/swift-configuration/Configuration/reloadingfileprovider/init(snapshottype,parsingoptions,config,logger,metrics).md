---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/reloadingfileprovider/init(snapshottype:parsingoptions:config:logger:metrics:)"
framework: "swift-configuration/Configuration"
---

# init(snapshotType:parsingOptions:config:logger:metrics:)

**Framework**: swift-configuration/Configuration  
**Kind**: init  
**Role**: Initializer

Creates a reloading file provider using configuration from a reader.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
convenience init(snapshotType: Snapshot.Type = Snapshot.self, parsingOptions: Snapshot.ParsingOptions = .default, config: ConfigReader, logger: Logger = Logger(label: "ReloadingFileProvider"), metrics: any MetricsFactory = MetricsSystem.factory) async throws
```

#### Configuration keys

- `filePath` (string, required): The path to the configuration file to monitor.
- `allowMissing` (bool, optional, default: false): A flag controlling how the provider handles a missing file. When `false` (the default), if the file is missing or malformed, throws an error. When `true`, if the file is missing, treats it as empty. Malformed files still throw an error.
- `pollIntervalSeconds` (int, optional, default: 15): How often, in seconds, to check for file changes.

> **Throws**: If required configuration keys are missing, if the file cannot be read, or if snapshot creation fails.

## Parameters

- `snapshotType`: The type of snapshot to create from the file contents.
- `parsingOptions`: Options used by the snapshot to parse the file data.
- `config`: A configuration reader that contains the required configuration keys.
- `logger`: The logger instance to use for this provider.
- `metrics`: The metrics factory to use for monitoring provider performance.

## See Also

### Creating a reloading file provider
- [convenience init(snapshotType: Snapshot.Type, parsingOptions: Snapshot.ParsingOptions, filePath: FilePath, allowMissing: Bool, pollInterval: Duration, logger: Logger, metrics: any MetricsFactory) async throws](./init%28snapshottype,parsingoptions,filepath,allowmissing,pollinterval,logger,metrics%29.md)
  Creates a reloading file provider that monitors the specified file path.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/reloadingfileprovider/init(snapshottype:parsingoptions:config:logger:metrics:))*
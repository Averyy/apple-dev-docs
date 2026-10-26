---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/reloadingfileprovider"
framework: "swift-configuration/Configuration"
---

# ReloadingFileProvider

**Framework**: swift-configuration/Configuration  
**Kind**: class  
**Role**: Class

A configuration provider that reads configuration from a file on disk with automatic reloading capability.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
final class ReloadingFileProvider<Snapshot> where Snapshot : FileConfigSnapshot
```

## Mentions

- [Using reloading providers](./using-reloading-providers.md)
- [Choosing the access pattern](./choosing-access-patterns.md)
- [Implementing a custom provider](./implementing-a-provider.md)
- [Troubleshooting and access reporting](./troubleshooting.md)

#### Overview

`ReloadingFileProvider` is a generic file-based configuration provider that monitors a configuration file for changes and automatically reloads the data when the file is modified. This provider works with different file formats by using different snapshot types that conform to [`FileConfigSnapshot`](./fileconfigsnapshot.md).

#### Usage

Create a reloading provider by specifying the snapshot type and file path:

```swift
// Using with a JSON snapshot and a custom poll interval
let jsonProvider = try await ReloadingFileProvider<JSONSnapshot>(
    filePath: "/etc/config.json",
    pollInterval: .seconds(30)
)

// Using with a YAML snapshot
let yamlProvider = try await ReloadingFileProvider<YAMLSnapshot>(
    filePath: "/etc/config.yaml"
)
```

#### Service integration

This provider implements the `Service` protocol and must be run within a `ServiceGroup` to enable automatic reloading:

```swift
let provider = try await ReloadingFileProvider<JSONSnapshot>(filePath: "/etc/config.json")
let serviceGroup = ServiceGroup(services: [provider], logger: logger)
try await serviceGroup.run()
```

The provider monitors the file by polling at the specified interval (default: 15 seconds) and notifies any active watchers when it detects changes.

On platforms with Unix signals, a running provider also checks the file whenever the process receives `SIGHUP`, so you don’t have to wait for the next poll. Either way, the file is only reloaded if its modification timestamp or resolved path changed.

#### Configuration from a reader

You can also initialize the provider using a configuration reader:

```swift
let envConfig = ConfigReader(provider: EnvironmentVariablesProvider())
let provider = try await ReloadingFileProvider<JSONSnapshot>(config: envConfig)
```

This expects configuration keys that specify the file path and optionally other format-specific values. For a full list of configuration keys, see [`init(snapshotType:parsingOptions:config:logger:metrics:)`](./reloadingfileprovider/init%28snapshottype,parsingoptions,config,logger,metrics%29.md).

#### File monitoring

The provider detects changes by monitoring both file timestamps and symlink target changes. When it detects a change, it reloads the file and notifies all active watchers of the updated configuration values.

## Topics

### Creating a reloading file provider
- [convenience init(snapshotType: Snapshot.Type, parsingOptions: Snapshot.ParsingOptions, filePath: FilePath, allowMissing: Bool, pollInterval: Duration, logger: Logger, metrics: any MetricsFactory) async throws](./reloadingfileprovider/init%28snapshottype,parsingoptions,filepath,allowmissing,pollinterval,logger,metrics%29.md)
  Creates a reloading file provider that monitors the specified file path.
- [convenience init(snapshotType: Snapshot.Type, parsingOptions: Snapshot.ParsingOptions, config: ConfigReader, logger: Logger, metrics: any MetricsFactory) async throws](./reloadingfileprovider/init%28snapshottype,parsingoptions,config,logger,metrics%29.md)
  Creates a reloading file provider using configuration from a reader.
### Service lifecycle
- [func run() async throws](./reloadingfileprovider/run%28%29.md)
### Monitoring file changes
- [protocol FileConfigSnapshot](./fileconfigsnapshot.md)
  A protocol for configuration snapshots created from file data.
- [struct JSONSnapshot](./jsonsnapshot.md)
  A snapshot of configuration values parsed from JSON data.
- [class YAMLSnapshot](./yamlsnapshot.md)
  A snapshot of configuration values parsed from YAML data.
- [struct PropertyListSnapshot](./propertylistsnapshot.md)
  A snapshot of configuration values parsed from property list (plist) data.
### Instance Properties
- [let providerName: String](./reloadingfileprovider/providername.md)
  The human-readable name of the provider.
### Default Implementations
- [ConfigProvider Implementations](./reloadingfileprovider/configprovider-implementations.md)
- [CustomDebugStringConvertible Implementations](./reloadingfileprovider/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](./reloadingfileprovider/customstringconvertible-implementations.md)
- [Service Implementations](./reloadingfileprovider/service-implementations.md)

## Relationships

### Conforms To
- [ConfigProvider](./configprovider.md)
- ServiceLifecycle.Service
- Swift.Copyable
- Swift.CustomDebugStringConvertible
- Swift.CustomStringConvertible
- Swift.Escapable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Built-in providers
- [struct EnvironmentVariablesProvider](./environmentvariablesprovider.md)
  A configuration provider that reads values from environment variables.
- [struct CommandLineArgumentsProvider](./commandlineargumentsprovider.md)
  A configuration provider that sources values from command-line arguments.
- [Integrating with Swift Argument Parser](./integrating-with-swift-argument-parser.md)
  Combine the commands and options of Swift Argument Parser with the provider hierarchy of Swift Configuration.
- [struct FileProvider](./fileprovider.md)
  A configuration provider that reads from a file on disk using a configurable snapshot type.
- [struct JSONSnapshot](./jsonsnapshot.md)
  A snapshot of configuration values parsed from JSON data.
- [class YAMLSnapshot](./yamlsnapshot.md)
  A snapshot of configuration values parsed from YAML data.
- [struct PropertyListSnapshot](./propertylistsnapshot.md)
  A snapshot of configuration values parsed from property list (plist) data.
- [Using reloading providers](./using-reloading-providers.md)
  Automatically reload configuration from files when they change.
- [struct DirectoryFilesProvider](./directoryfilesprovider.md)
  A configuration provider that reads values from individual files in a directory.
- [Using in-memory providers](./using-in-memory-providers.md)
  Learn about the [`InMemoryProvider`](./inmemoryprovider.md) and [`MutableInMemoryProvider`](./mutableinmemoryprovider.md) built-in types.
- [struct InMemoryProvider](./inmemoryprovider.md)
  A configuration provider that stores values in memory.
- [class MutableInMemoryProvider](./mutableinmemoryprovider.md)
  A configuration provider that stores mutable values in memory.
- [struct KeyMappingProvider](./keymappingprovider.md)
  A configuration provider that maps all keys before delegating to an upstream provider.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/reloadingfileprovider)*
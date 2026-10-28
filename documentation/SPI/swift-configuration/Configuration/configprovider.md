---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configprovider"
framework: "swift-configuration/Configuration"
---

# ConfigProvider

**Framework**: swift-configuration/Configuration  
**Kind**: protocol  
**Role**: Protocol

A type that provides configuration values from a data source.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
protocol ConfigProvider : Sendable
```

## Mentions

- [Implementing a custom provider](./implementing-a-provider.md)
- [Choosing the access pattern](./choosing-access-patterns.md)
- [Developing Swift Configuration](./development.md)
- [Example use cases](./example-use-cases.md)
- [Handling secrets correctly](./handling-secrets-correctly.md)

## Overview

Configuration providers offer three access patterns for retrieving values:

1. **Get methods**: Synchronous access to cached, in-memory values.
2. **Fetch methods**: Asynchronous access that retrieves fresh values from the remote source.
3. **Watch methods**: Reactive access that provides an async sequence of updates.

For more details on the patterns, check out [Choosing the access pattern](./choosing-access-patterns.md).

## Individual value access

Access specific configuration values using these methods:

- [`value(forKey:type:)`](./configprovider/value%28forkey,type%29.md) - Get the current value synchronously.
- [`fetchValue(forKey:type:)`](./configprovider/fetchvalue%28forkey,type%29.md) - Fetch the latest value asynchronously.
- [`watchValue(forKey:type:updatesHandler:)`](./configprovider/watchvalue%28forkey,type,updateshandler%29.md) - Watch for value changes, receiving the current value first.

## Snapshot access

Access immutable snapshots of the provider’s state:

- [`snapshot()`](./configprovider/snapshot%28%29.md) - Get the current snapshot.
- [`watchSnapshot(updatesHandler:)`](./configprovider/watchsnapshot%28updateshandler%29.md) - Watch for snapshot changes, receiving the current snapshot first.

## Implementation guidance

**Immutable providers**: Implement only the synchronous methods and use these convenience methods for the other access patterns:

- [`watchValueFromValue(forKey:type:updatesHandler:)`](./configprovider/watchvaluefromvalue%28forkey,type,updateshandler%29.md)
- [`watchSnapshotFromSnapshot(updatesHandler:)`](./configprovider/watchsnapshotfromsnapshot%28updateshandler%29.md)

**Remote providers**: Implement `fetch` methods to retrieve up-to-date values from network sources or external systems.

**Dynamic providers**: Implement `watch` methods to emit real-time updates from polling, file system monitoring, or other change detection mechanisms.

For a comprehensive guide on implementing your own custom provider, see [Implementing a custom provider](./implementing-a-provider.md).

## Topics

### Required methods
- [var providerName: String](./configprovider/providername.md)
  The human-readable name of the configuration provider.
- [func value(forKey: AbsoluteConfigKey, type: ConfigType) throws -> LookupResult](./configprovider/value%28forkey,type%29.md)
  Returns the current value for the specified configuration key.
- [func fetchValue(forKey: AbsoluteConfigKey, type: ConfigType) async throws -> LookupResult](./configprovider/fetchvalue%28forkey,type%29.md)
  Fetches the current value for the specified configuration key.
- [func watchValue<Return>(forKey: AbsoluteConfigKey, type: ConfigType, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Result<LookupResult, any Error>, Never>) async throws -> Return) async throws -> Return](./configprovider/watchvalue%28forkey,type,updateshandler%29.md)
  Monitors a configuration key for value changes over time.
- [func snapshot() -> any ConfigSnapshot](./configprovider/snapshot%28%29.md)
  Returns an immutable snapshot of the provider’s current state.
- [func watchSnapshot<Return>(updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<any ConfigSnapshot, Never>) async throws -> Return) async throws -> Return](./configprovider/watchsnapshot%28updateshandler%29.md)
  Monitors the provider’s state for changes by emitting snapshots.
### Conveniences
- [func watchValueFromValue<Return>(forKey: AbsoluteConfigKey, type: ConfigType, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Result<LookupResult, any Error>, Never>) async throws -> Return) async throws -> Return](./configprovider/watchvaluefromvalue%28forkey,type,updateshandler%29.md)
  Implements `watchValue` by getting the current value and emitting it immediately.
- [func watchSnapshotFromSnapshot<Return>(updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<any ConfigSnapshot, Never>) async throws -> Return) async throws -> Return](./configprovider/watchsnapshotfromsnapshot%28updateshandler%29.md)
  Implements `watchSnapshot` by getting the current snapshot and emitting it immediately.
- [func mapKeys((AbsoluteConfigKey) -> AbsoluteConfigKey) -> KeyMappingProvider<Self>](./configprovider/mapkeys%28_%29.md)
  Creates a new configuration provider where each key is rewritten by the given closure.
- [func prefixKeys(with: ConfigKey) -> KeyMappingProvider<Self>](./configprovider/prefixkeys%28with%29.md)
  Creates a new prefixed configuration provider.
### Related guides
- [Implementing a custom provider](./implementing-a-provider.md)
  Create a custom configuration provider to integrate a new data source.

## Relationships

### Inherits From
- Swift.Sendable
- Swift.SendableMetatype
### Conforming Types
- [CommandLineArgumentsProvider](./commandlineargumentsprovider.md)
- [DirectoryFilesProvider](./directoryfilesprovider.md)
- [EnvironmentVariablesProvider](./environmentvariablesprovider.md)
- [FileProvider](./fileprovider.md)
- [InMemoryProvider](./inmemoryprovider.md)
- [KeyMappingProvider](./keymappingprovider.md)
- [MutableInMemoryProvider](./mutableinmemoryprovider.md)
- [ReloadingFileProvider](./reloadingfileprovider.md)

## See Also

### Readers and providers
- [struct ConfigReader](./configreader.md)
  A type that provides read-only access to configuration values from underlying providers.
- [struct ConfigSnapshotReader](./configsnapshotreader.md)
  A container type for reading config values from snapshots.
- [Choosing the access pattern](./choosing-access-patterns.md)
  Learn how to select the right method for reading configuration values based on your needs.
- [Choosing reader methods](./choosing-reader-methods.md)
  Choose between optional, default, and required variants of configuration methods.
- [Handling secrets correctly](./handling-secrets-correctly.md)
  Protect sensitive configuration values from accidental disclosure in logs and debug output.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configprovider)*
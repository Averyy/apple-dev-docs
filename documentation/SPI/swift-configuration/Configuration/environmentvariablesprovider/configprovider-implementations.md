---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/environmentvariablesprovider/configprovider-implementations"
framework: "swift-configuration/Configuration"
---

# ConfigProvider Implementations

**Framework**: swift-configuration/Configuration  
**Role**: API Collection

## Topics

### Instance Properties
- [var providerName: String](./providername.md)
  The human-readable name of the configuration provider.
### Instance Methods
- [func fetchValue(forKey: AbsoluteConfigKey, type: ConfigType) async throws -> LookupResult](./fetchvalue%28forkey,type%29.md)
  Fetches the current value for the specified configuration key.
- [func mapKeys((AbsoluteConfigKey) -> AbsoluteConfigKey) -> KeyMappingProvider<Self>](./mapkeys%28_%29.md)
  Creates a new configuration provider where each key is rewritten by the given closure.
- [func prefixKeys(with: ConfigKey) -> KeyMappingProvider<Self>](./prefixkeys%28with%29.md)
  Creates a new prefixed configuration provider.
- [func snapshot() -> any ConfigSnapshot](./snapshot%28%29.md)
  Returns an immutable snapshot of the provider’s current state.
- [func value(forKey: AbsoluteConfigKey, type: ConfigType) throws -> LookupResult](./value%28forkey,type%29.md)
  Returns the current value for the specified configuration key.
- [func watchSnapshot<Return>(updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<any ConfigSnapshot, Never>) async throws -> Return) async throws -> Return](./watchsnapshot%28updateshandler%29.md)
  Monitors the provider’s state for changes by emitting snapshots.
- [func watchSnapshotFromSnapshot<Return>(updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<any ConfigSnapshot, Never>) async throws -> Return) async throws -> Return](./watchsnapshotfromsnapshot%28updateshandler%29.md)
  Implements `watchSnapshot` by getting the current snapshot and emitting it immediately.
- [func watchValue<Return>(forKey: AbsoluteConfigKey, type: ConfigType, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Result<LookupResult, any Error>, Never>) async throws -> Return) async throws -> Return](./watchvalue%28forkey,type,updateshandler%29.md)
  Monitors a configuration key for value changes over time.
- [func watchValueFromValue<Return>(forKey: AbsoluteConfigKey, type: ConfigType, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Result<LookupResult, any Error>, Never>) async throws -> Return) async throws -> Return](./watchvaluefromvalue%28forkey,type,updateshandler%29.md)
  Implements `watchValue` by getting the current value and emitting it immediately.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/environmentvariablesprovider/configprovider-implementations)*
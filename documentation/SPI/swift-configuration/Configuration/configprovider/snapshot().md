---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configprovider/snapshot()"
framework: "swift-configuration/Configuration"
---

# snapshot()

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns an immutable snapshot of the provider’s current state.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func snapshot() -> any ConfigSnapshot
```

#### Return Value

An immutable snapshot that represents the current provider state.

#### Discussion

Snapshots provide consistent access to multiple configuration values by capturing the provider’s state at a specific point in time. This prevents values from changing between reads, which is useful for reading related configuration keys together.

Snapshots are designed to be lightweight and can be created frequently without significant performance impact.

## See Also

### Required methods
- [var providerName: String](./providername.md)
  The human-readable name of the configuration provider.
- [func value(forKey: AbsoluteConfigKey, type: ConfigType) throws -> LookupResult](./value%28forkey,type%29.md)
  Returns the current value for the specified configuration key.
- [func fetchValue(forKey: AbsoluteConfigKey, type: ConfigType) async throws -> LookupResult](./fetchvalue%28forkey,type%29.md)
  Fetches the current value for the specified configuration key.
- [func watchValue<Return>(forKey: AbsoluteConfigKey, type: ConfigType, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Result<LookupResult, any Error>, Never>) async throws -> Return) async throws -> Return](./watchvalue%28forkey,type,updateshandler%29.md)
  Monitors a configuration key for value changes over time.
- [func watchSnapshot<Return>(updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<any ConfigSnapshot, Never>) async throws -> Return) async throws -> Return](./watchsnapshot%28updateshandler%29.md)
  Monitors the provider’s state for changes by emitting snapshots.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configprovider/snapshot())*
---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configprovider/value(forkey:type:)"
framework: "swift-configuration/Configuration"
---

# value(forKey:type:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the current value for the specified configuration key.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func value(forKey key: AbsoluteConfigKey, type: ConfigType) throws -> LookupResult
```

#### Return Value

The lookup result containing the value and encoded key, or nil if not found.

#### Discussion

This method provides synchronous access to configuration values and should be efficient to call repeatedly. The returned value may change between calls if the underlying data source is mutable.

> **Throws**: Provider-specific errors or type conversion errors.

## Parameters

- `key`: The configuration key to look up.
- `type`: The expected configuration value type.

## See Also

### Required methods
- [var providerName: String](./providername.md)
  The human-readable name of the configuration provider.
- [func fetchValue(forKey: AbsoluteConfigKey, type: ConfigType) async throws -> LookupResult](./fetchvalue%28forkey,type%29.md)
  Fetches the current value for the specified configuration key.
- [func watchValue<Return>(forKey: AbsoluteConfigKey, type: ConfigType, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Result<LookupResult, any Error>, Never>) async throws -> Return) async throws -> Return](./watchvalue%28forkey,type,updateshandler%29.md)
  Monitors a configuration key for value changes over time.
- [func snapshot() -> any ConfigSnapshot](./snapshot%28%29.md)
  Returns an immutable snapshot of the provider’s current state.
- [func watchSnapshot<Return>(updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<any ConfigSnapshot, Never>) async throws -> Return) async throws -> Return](./watchsnapshot%28updateshandler%29.md)
  Monitors the provider’s state for changes by emitting snapshots.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configprovider/value(forkey:type:))*
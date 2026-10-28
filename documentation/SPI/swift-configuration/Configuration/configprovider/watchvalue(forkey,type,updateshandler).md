---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configprovider/watchvalue(forkey:type:updateshandler:)"
framework: "swift-configuration/Configuration"
---

# watchValue(forKey:type:updatesHandler:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Monitors a configuration key for value changes over time.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func watchValue<Return>(forKey key: AbsoluteConfigKey, type: ConfigType, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Result<LookupResult, any Error>, Never>) async throws -> Return) async throws -> Return where Return : ~Copyable
```

## Return Value

The value returned by the closure.

## Discussion

The async sequence provided to the handler should immediately emit the current value (equivalent to calling [`value(forKey:type:)`](./value%28forkey,type%29.md)), followed by subsequent updates as they occur.

The sequence completes gracefully when the current task is canceled, to allow proper cleanup of resources.

> **Throws**: Provider-specific errors or errors thrown by the handler closure.

## Parameters

- `key`: The configuration key to monitor.
- `type`: The expected configuration value type.
- `updatesHandler`: The closure that processes the async sequence of value updates.

## See Also

### Required methods
- [var providerName: String](./providername.md)
  The human-readable name of the configuration provider.
- [func value(forKey: AbsoluteConfigKey, type: ConfigType) throws -> LookupResult](./value%28forkey,type%29.md)
  Returns the current value for the specified configuration key.
- [func fetchValue(forKey: AbsoluteConfigKey, type: ConfigType) async throws -> LookupResult](./fetchvalue%28forkey,type%29.md)
  Fetches the current value for the specified configuration key.
- [func snapshot() -> any ConfigSnapshot](./snapshot%28%29.md)
  Returns an immutable snapshot of the provider’s current state.
- [func watchSnapshot<Return>(updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<any ConfigSnapshot, Never>) async throws -> Return) async throws -> Return](./watchsnapshot%28updateshandler%29.md)
  Monitors the provider’s state for changes by emitting snapshots.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configprovider/watchvalue(forkey:type:updateshandler:))*
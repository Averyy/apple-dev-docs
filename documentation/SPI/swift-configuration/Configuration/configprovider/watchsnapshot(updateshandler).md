---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configprovider/watchsnapshot(updateshandler:)"
framework: "swift-configuration/Configuration"
---

# watchSnapshot(updatesHandler:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Monitors the provider’s state for changes by emitting snapshots.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func watchSnapshot<Return>(updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<any ConfigSnapshot, Never>) async throws -> Return) async throws -> Return where Return : ~Copyable
```

## Return Value

The value returned by the closure.

## Discussion

The async sequence provided to the handler should immediately emit the current snapshot (equivalent to calling [`snapshot()`](./snapshot%28%29.md)), followed by new snapshots as the provider’s state changes.

The sequence completes gracefully when the current task is canceled.

> **Throws**: Provider-specific errors or errors thrown by the handler closure.

## Parameters

- `updatesHandler`: The closure that processes the asynchronous sequence of snapshot updates.

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
- [func snapshot() -> any ConfigSnapshot](./snapshot%28%29.md)
  Returns an immutable snapshot of the provider’s current state.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configprovider/watchsnapshot(updateshandler:))*
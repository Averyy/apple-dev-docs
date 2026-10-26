---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configprovider/providername"
framework: "swift-configuration/Configuration"
---

# providerName

**Framework**: swift-configuration/Configuration  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The human-readable name of the configuration provider.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var providerName: String { get }
```

#### Discussion

Used by [`AccessReporter`](../accessreporter.md) and other diagnostic logging.

## See Also

### Required methods
- [func value(forKey: AbsoluteConfigKey, type: ConfigType) throws -> LookupResult](./value%28forkey,type%29.md)
  Returns the current value for the specified configuration key.
- [func fetchValue(forKey: AbsoluteConfigKey, type: ConfigType) async throws -> LookupResult](./fetchvalue%28forkey,type%29.md)
  Fetches the current value for the specified configuration key.
- [func watchValue<Return>(forKey: AbsoluteConfigKey, type: ConfigType, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Result<LookupResult, any Error>, Never>) async throws -> Return) async throws -> Return](./watchvalue%28forkey,type,updateshandler%29.md)
  Monitors a configuration key for value changes over time.
- [func snapshot() -> any ConfigSnapshot](./snapshot%28%29.md)
  Returns an immutable snapshot of the provider’s current state.
- [func watchSnapshot<Return>(updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<any ConfigSnapshot, Never>) async throws -> Return) async throws -> Return](./watchsnapshot%28updateshandler%29.md)
  Monitors the provider’s state for changes by emitting snapshots.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configprovider/providername)*
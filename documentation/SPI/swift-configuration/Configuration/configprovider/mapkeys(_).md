---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configprovider/mapkeys(_:)"
framework: "swift-configuration/Configuration"
---

# mapKeys(_:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Creates a new configuration provider where each key is rewritten by the given closure.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func mapKeys(_ transform: @escaping @Sendable (AbsoluteConfigKey) -> AbsoluteConfigKey) -> KeyMappingProvider<Self>
```

#### Return Value

A provider which maps keys using the provided transformation function.

## Parameters

- `transform`: The closure applied to each key before a lookup.

## See Also

### Conveniences
- [func watchValueFromValue<Return>(forKey: AbsoluteConfigKey, type: ConfigType, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Result<LookupResult, any Error>, Never>) async throws -> Return) async throws -> Return](./watchvaluefromvalue%28forkey,type,updateshandler%29.md)
  Implements `watchValue` by getting the current value and emitting it immediately.
- [func watchSnapshotFromSnapshot<Return>(updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<any ConfigSnapshot, Never>) async throws -> Return) async throws -> Return](./watchsnapshotfromsnapshot%28updateshandler%29.md)
  Implements `watchSnapshot` by getting the current snapshot and emitting it immediately.
- [func prefixKeys(with: ConfigKey) -> KeyMappingProvider<Self>](./prefixkeys%28with%29.md)
  Creates a new prefixed configuration provider.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configprovider/mapkeys(_:))*
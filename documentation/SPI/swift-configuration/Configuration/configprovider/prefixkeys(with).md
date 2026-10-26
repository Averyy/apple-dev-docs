---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configprovider/prefixkeys(with:)"
framework: "swift-configuration/Configuration"
---

# prefixKeys(with:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Creates a new prefixed configuration provider.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func prefixKeys(with prefix: ConfigKey) -> KeyMappingProvider<Self>
```

#### Return Value

A provider which prefixes keys with the given prefix.

#### Discussion

- Parameter: prefix: The configuration key to prepend to all configuration keys.

## See Also

### Conveniences
- [func watchValueFromValue<Return>(forKey: AbsoluteConfigKey, type: ConfigType, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Result<LookupResult, any Error>, Never>) async throws -> Return) async throws -> Return](./watchvaluefromvalue%28forkey,type,updateshandler%29.md)
  Implements `watchValue` by getting the current value and emitting it immediately.
- [func watchSnapshotFromSnapshot<Return>(updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<any ConfigSnapshot, Never>) async throws -> Return) async throws -> Return](./watchsnapshotfromsnapshot%28updateshandler%29.md)
  Implements `watchSnapshot` by getting the current snapshot and emitting it immediately.
- [func mapKeys((AbsoluteConfigKey) -> AbsoluteConfigKey) -> KeyMappingProvider<Self>](./mapkeys%28_%29.md)
  Creates a new configuration provider where each key is rewritten by the given closure.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configprovider/prefixkeys(with:))*
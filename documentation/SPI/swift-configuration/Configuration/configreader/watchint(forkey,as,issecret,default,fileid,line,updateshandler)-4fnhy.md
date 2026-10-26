---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/watchint(forkey:as:issecret:default:fileid:line:updateshandler:)-4fnhy"
framework: "swift-configuration/Configuration"
---

# watchInt(forKey:as:isSecret:default:fileID:line:updatesHandler:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Watches for updates to a config value for the given config key with default fallback, converting from an integer.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func watchInt<Value, Return>(forKey key: ConfigKey, as type: Value.Type = Value.self, isSecret: Bool = false, default defaultValue: Value, fileID: String = #fileID, line: UInt = #line, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Value, Never>) async throws -> Return) async throws -> Return where Value : RawRepresentable, Value : Sendable, Value.RawValue == Int, Return : ~Copyable
```

#### Return Value

The result produced by the handler.

#### Discussion

Use this method to observe changes to integer-convertible configuration values over time with a guaranteed fallback. The handler receives an async sequence that produces the current value whenever it changes, or the default value if the configuration value is missing or can’t be converted.

```swift
try await config.watchInt(forKey: ["api", "version"], as: APIVersion.self, default: .version(1)) { updates in
    for await version in updates {
        print("Api version is: \(version.description)")
    }
}
```

> **Throws**: Rethrows any error thrown by the handler or the underlying watch operation.

## Parameters

- `key`: The config key to watch.
- `type`: The type to convert the integer value to.
- `isSecret`: Whether the value should be treated as secret for logging and debugging purposes.
- `defaultValue`: The fallback value used when the config value is missing or invalid.
- `fileID`: The file ID where this call originates. Used for access reporting.
- `line`: The line number where this call originates. Used for access reporting.
- `updatesHandler`: A closure that handles an async sequence of updates to the value. The sequence produces the default value if the provider returned a `nil` value or conversion failed.

## See Also

### Watching integer values
- [func watchInt<Return>(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Int?, Never>) async throws -> Return) async throws -> Return](./watchint%28forkey,issecret,fileid,line,updateshandler%29.md)
  Watches for updates to a config value for the given config key.
- [func watchInt<Return>(forKey: ConfigKey, isSecret: Bool, default: Int, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Int, Never>) async throws -> Return) async throws -> Return](./watchint%28forkey,issecret,default,fileid,line,updateshandler%29.md)
  Watches for updates to a config value for the given config key with default fallback.
- [func watchInt<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Value?, Never>) async throws -> Return) async throws -> Return](./watchint%28forkey,as,issecret,fileid,line,updateshandler%29-1jgbh.md)
  Watches for updates to a config value for the given config key, converting from an integer.
- [func watchInt<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Value?, Never>) async throws -> Return) async throws -> Return](./watchint%28forkey,as,issecret,fileid,line,updateshandler%29-8ybja.md)
  Watches for updates to a config value for the given config key, converting from an integer.
- [func watchInt<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: Value, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Value, Never>) async throws -> Return) async throws -> Return](./watchint%28forkey,as,issecret,default,fileid,line,updateshandler%29-933s1.md)
  Watches for updates to a config value for the given config key with default fallback, converting from an integer.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/watchint(forkey:as:issecret:default:fileid:line:updateshandler:)-4fnhy)*
---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/watchstringarray(forkey:as:issecret:default:fileid:line:updateshandler:)-256k2"
framework: "swift-configuration/Configuration"
---

# watchStringArray(forKey:as:isSecret:default:fileID:line:updatesHandler:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Watches for updates to an array of config values for the given config key with default fallback, converting from strings.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func watchStringArray<Value, Return>(forKey key: ConfigKey, as type: Value.Type = Value.self, isSecret: Bool = false, default defaultValue: [Value], fileID: String = #fileID, line: UInt = #line, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[Value], Never>) async throws -> Return) async throws -> Return where Value : RawRepresentable, Value : Sendable, Value.RawValue == String, Return : ~Copyable
```

## Return Value

The result produced by the handler.

## Discussion

Use this method to observe changes to string-convertible array configuration values over time with a guaranteed fallback. The handler receives an async sequence that produces the current array whenever it changes, or the default value if the configuration value is missing or can’t be converted.

```swift
try await config.watchStringArray(forKey: ["server", "allowedModes"], as: ServerMode.self, default: [.production]) { updates in
    for await modes in updates {
        print("Allowed server modes: \(modes.map(\.description).joined(separator: ", "))")
    }
}
```

> **Throws**: Rethrows any error thrown by the handler or the underlying watch operation.

## Parameters

- `key`: The config key to watch.
- `type`: The element type to convert each string value to.
- `isSecret`: Whether the value should be treated as secret for logging and debugging purposes.
- `defaultValue`: The fallback array used when the config value is missing or invalid.
- `fileID`: The file ID where this call originates. Used for access reporting.
- `line`: The line number where this call originates. Used for access reporting.
- `updatesHandler`: A closure that handles an async sequence of updates to the value. The sequence produces the default value if the provider returned a `nil` value or conversion failed.

## See Also

### Watching lists of string values
- [func watchStringArray<Return>(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[String]?, Never>) async throws -> Return) async throws -> Return](./watchstringarray%28forkey,issecret,fileid,line,updateshandler%29.md)
  Watches for updates to a config value for the given config key.
- [func watchStringArray<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[Value]?, Never>) async throws -> Return) async throws -> Return](./watchstringarray%28forkey,as,issecret,fileid,line,updateshandler%29-15oye.md)
  Watches for updates to an array of config values for the given config key, converting from strings.
- [func watchStringArray<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[Value]?, Never>) async throws -> Return) async throws -> Return](./watchstringarray%28forkey,as,issecret,fileid,line,updateshandler%29-7snta.md)
  Watches for updates to an array of config values for the given config key, converting from strings.
- [func watchStringArray<Return>(forKey: ConfigKey, isSecret: Bool, default: [String], fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[String], Never>) async throws -> Return) async throws -> Return](./watchstringarray%28forkey,issecret,default,fileid,line,updateshandler%29.md)
  Watches for updates to a config value for the given config key with default fallback.
- [func watchStringArray<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: [Value], fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[Value], Never>) async throws -> Return) async throws -> Return](./watchstringarray%28forkey,as,issecret,default,fileid,line,updateshandler%29-9t8bb.md)
  Watches for updates to an array of config values for the given config key with default fallback, converting from strings.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/watchstringarray(forkey:as:issecret:default:fileid:line:updateshandler:)-256k2)*
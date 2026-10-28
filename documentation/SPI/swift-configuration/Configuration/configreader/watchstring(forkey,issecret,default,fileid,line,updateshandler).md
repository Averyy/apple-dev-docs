---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/watchstring(forkey:issecret:default:fileid:line:updateshandler:)"
framework: "swift-configuration/Configuration"
---

# watchString(forKey:isSecret:default:fileID:line:updatesHandler:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Watches for updates to a config value for the given config key with default fallback.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func watchString<Return>(forKey key: ConfigKey, isSecret: Bool = false, default defaultValue: String, fileID: String = #fileID, line: UInt = #line, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<String, Never>) async throws -> Return) async throws -> Return where Return : ~Copyable
```

## Return Value

The result produced by the handler.

## Discussion

Use this method to observe changes to configuration values over time with a guaranteed fallback. The handler receives an async sequence that produces the current value whenever it changes, or the default value if the configuration value is missing or can’t be converted.

```swift
try await config.watchString(forKey: ["server", "port"], default: "hello") { updates in
    for await port in updates {
        print("Server port is: \(port)")
    }
}
```

> **Throws**: Rethrows any error thrown by the handler or the underlying watch operation.

## Parameters

- `key`: The config key to watch.
- `isSecret`: Whether the value should be treated as secret for logging and debugging purposes.
- `defaultValue`: The fallback value used when the config value is missing or invalid.
- `fileID`: The file ID where this call originates. Used for access reporting.
- `line`: The line number where this call originates. Used for access reporting.
- `updatesHandler`: A closure that handles an async sequence of updates to the value. The sequence produces the default value if the provider returned a `nil` value or conversion failed.

## See Also

### Watching string values
- [func watchString<Return>(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<String?, Never>) async throws -> Return) async throws -> Return](./watchstring%28forkey,issecret,fileid,line,updateshandler%29.md)
  Watches for updates to a config value for the given config key.
- [func watchString<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Value?, Never>) async throws -> Return) async throws -> Return](./watchstring%28forkey,as,issecret,fileid,line,updateshandler%29-4zs5y.md)
  Watches for updates to a config value for the given config key, converting from string.
- [func watchString<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Value?, Never>) async throws -> Return) async throws -> Return](./watchstring%28forkey,as,issecret,fileid,line,updateshandler%29-8hegv.md)
  Watches for updates to a config value for the given config key, converting from string.
- [func watchString<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: Value, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Value, Never>) async throws -> Return) async throws -> Return](./watchstring%28forkey,as,issecret,default,fileid,line,updateshandler%29-hi1l.md)
  Watches for updates to a config value for the given config key with default fallback, converting from string.
- [func watchString<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: Value, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Value, Never>) async throws -> Return) async throws -> Return](./watchstring%28forkey,as,issecret,default,fileid,line,updateshandler%29-9qsww.md)
  Watches for updates to a config value for the given config key with default fallback, converting from string.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/watchstring(forkey:issecret:default:fileid:line:updateshandler:))*
---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/watchstring(forkey:as:issecret:fileid:line:updateshandler:)-4zs5y"
framework: "swift-configuration/Configuration"
---

# watchString(forKey:as:isSecret:fileID:line:updatesHandler:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Watches for updates to a config value for the given config key, converting from string.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func watchString<Value, Return>(forKey key: ConfigKey, as type: Value.Type = Value.self, isSecret: Bool = false, fileID: String = #fileID, line: UInt = #line, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Value?, Never>) async throws -> Return) async throws -> Return where Value : ExpressibleByConfigString, Value : Sendable, Return : ~Copyable
```

#### Return Value

The result produced by the handler.

#### Discussion

Use this method to observe changes to optional string-convertible configuration values over time. The handler receives an async sequence that produces the current value whenever it changes, or `nil` if the value is missing or can’t be converted.

```swift
try await config.watchString(forKey: ["server", "mode"], as: ServerMode.self) { updates in
    for await mode in updates {
        if let mode = mode {
            print("Server mode is: \(mode.description)")
        } else {
            print("No server mode configured")
        }
    }
}
```

> **Throws**: Rethrows any error thrown by the handler or the underlying watch operation.

## Parameters

- `key`: The config key to watch.
- `type`: The type to convert the string value to.
- `isSecret`: Whether the value should be treated as secret for logging and debugging purposes.
- `fileID`: The file ID where this call originates. Used for access reporting.
- `line`: The line number where this call originates. Used for access reporting.
- `updatesHandler`: A closure that handles an async sequence of updates to the value. The sequence produces `nil` if the value is missing or can’t be converted.

## See Also

### Watching string values
- [func watchString<Return>(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<String?, Never>) async throws -> Return) async throws -> Return](./watchstring%28forkey,issecret,fileid,line,updateshandler%29.md)
  Watches for updates to a config value for the given config key.
- [func watchString<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Value?, Never>) async throws -> Return) async throws -> Return](./watchstring%28forkey,as,issecret,fileid,line,updateshandler%29-8hegv.md)
  Watches for updates to a config value for the given config key, converting from string.
- [func watchString<Return>(forKey: ConfigKey, isSecret: Bool, default: String, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<String, Never>) async throws -> Return) async throws -> Return](./watchstring%28forkey,issecret,default,fileid,line,updateshandler%29.md)
  Watches for updates to a config value for the given config key with default fallback.
- [func watchString<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: Value, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Value, Never>) async throws -> Return) async throws -> Return](./watchstring%28forkey,as,issecret,default,fileid,line,updateshandler%29-hi1l.md)
  Watches for updates to a config value for the given config key with default fallback, converting from string.
- [func watchString<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: Value, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Value, Never>) async throws -> Return) async throws -> Return](./watchstring%28forkey,as,issecret,default,fileid,line,updateshandler%29-9qsww.md)
  Watches for updates to a config value for the given config key with default fallback, converting from string.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/watchstring(forkey:as:issecret:fileid:line:updateshandler:)-4zs5y)*
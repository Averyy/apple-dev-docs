---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/watchint(forkey:issecret:fileid:line:updateshandler:)"
framework: "swift-configuration/Configuration"
---

# watchInt(forKey:isSecret:fileID:line:updatesHandler:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Watches for updates to a config value for the given config key.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func watchInt<Return>(forKey key: ConfigKey, isSecret: Bool = false, fileID: String = #fileID, line: UInt = #line, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Int?, Never>) async throws -> Return) async throws -> Return where Return : ~Copyable
```

## Mentions

- [Example use cases](../example-use-cases.md)

#### Return Value

The result produced by the handler.

#### Discussion

Use this method to observe changes to optional configuration values over time. The handler receives an async sequence that produces the current value whenever it changes, or `nil` if the value is missing or can’t be converted.

```swift
try await config.watchInt(forKey: ["server", "port"]) { updates in
    for await port in updates {
        if let port = port {
            print("Server port is: \(port)")
        } else {
            print("No server port configured")
        }
    }
}
```

> **Throws**: Rethrows any error thrown by the handler or the underlying watch operation.

## Parameters

- `key`: The config key to watch.
- `isSecret`: Whether the value should be treated as secret for logging and debugging purposes.
- `fileID`: The file ID where this call originates. Used for access reporting.
- `line`: The line number where this call originates. Used for access reporting.
- `updatesHandler`: A closure that handles an async sequence of updates to the value. The sequence produces `nil` if the value is missing or can’t be converted.

## See Also

### Watching integer values
- [func watchInt<Return>(forKey: ConfigKey, isSecret: Bool, default: Int, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Int, Never>) async throws -> Return) async throws -> Return](./watchint%28forkey,issecret,default,fileid,line,updateshandler%29.md)
  Watches for updates to a config value for the given config key with default fallback.
- [func watchInt<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Value?, Never>) async throws -> Return) async throws -> Return](./watchint%28forkey,as,issecret,fileid,line,updateshandler%29-1jgbh.md)
  Watches for updates to a config value for the given config key, converting from an integer.
- [func watchInt<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Value?, Never>) async throws -> Return) async throws -> Return](./watchint%28forkey,as,issecret,fileid,line,updateshandler%29-8ybja.md)
  Watches for updates to a config value for the given config key, converting from an integer.
- [func watchInt<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: Value, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Value, Never>) async throws -> Return) async throws -> Return](./watchint%28forkey,as,issecret,default,fileid,line,updateshandler%29-933s1.md)
  Watches for updates to a config value for the given config key with default fallback, converting from an integer.
- [func watchInt<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: Value, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Value, Never>) async throws -> Return) async throws -> Return](./watchint%28forkey,as,issecret,default,fileid,line,updateshandler%29-4fnhy.md)
  Watches for updates to a config value for the given config key with default fallback, converting from an integer.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/watchint(forkey:issecret:fileid:line:updateshandler:))*
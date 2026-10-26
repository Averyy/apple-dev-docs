---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/watchintarray(forkey:issecret:fileid:line:updateshandler:)"
framework: "swift-configuration/Configuration"
---

# watchIntArray(forKey:isSecret:fileID:line:updatesHandler:)

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
func watchIntArray<Return>(forKey key: ConfigKey, isSecret: Bool = false, fileID: String = #fileID, line: UInt = #line, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[Int]?, Never>) async throws -> Return) async throws -> Return where Return : ~Copyable
```

#### Return Value

The result produced by the handler.

#### Discussion

Use this method to observe changes to optional configuration values over time. The handler receives an async sequence that produces the current value whenever it changes, or `nil` if the value is missing or can’t be converted.

```swift
try await config.watchIntArray(forKey: ["server", "port"]) { updates in
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

### Watching lists of integer values
- [func watchIntArray<Return>(forKey: ConfigKey, isSecret: Bool, default: [Int], fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[Int], Never>) async throws -> Return) async throws -> Return](./watchintarray%28forkey,issecret,default,fileid,line,updateshandler%29.md)
  Watches for updates to a config value for the given config key with default fallback.
- [func watchIntArray<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[Value]?, Never>) async throws -> Return) async throws -> Return](./watchintarray%28forkey,as,issecret,fileid,line,updateshandler%29-getl.md)
  Watches for updates to an array of config values for the given config key, converting from integers.
- [func watchIntArray<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[Value]?, Never>) async throws -> Return) async throws -> Return](./watchintarray%28forkey,as,issecret,fileid,line,updateshandler%29-3wh9t.md)
  Watches for updates to an array of config values for the given config key, converting from integers.
- [func watchIntArray<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: [Value], fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[Value], Never>) async throws -> Return) async throws -> Return](./watchintarray%28forkey,as,issecret,default,fileid,line,updateshandler%29-1qrsh.md)
  Watches for updates to an array of config values for the given config key with default fallback, converting from integers.
- [func watchIntArray<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: [Value], fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[Value], Never>) async throws -> Return) async throws -> Return](./watchintarray%28forkey,as,issecret,default,fileid,line,updateshandler%29-3987h.md)
  Watches for updates to an array of config values for the given config key with default fallback, converting from integers.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/watchintarray(forkey:issecret:fileid:line:updateshandler:))*
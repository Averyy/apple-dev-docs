---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/watchrequiredstring(forkey:issecret:fileid:line:updateshandler:)"
framework: "swift-configuration/Configuration"
---

# watchRequiredString(forKey:isSecret:fileID:line:updatesHandler:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Watches for updates to a required config value for the given config key.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func watchRequiredString<Return>(forKey key: ConfigKey, isSecret: Bool = false, fileID: String = #fileID, line: UInt = #line, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<String, any Error>) async throws -> Return) async throws -> Return where Return : ~Copyable
```

## Return Value

The result produced by the handler.

## Discussion

Use this method to observe changes to configuration values that must be present. The handler receives an async sequence that produces the current value whenever it changes, or an error if the configuration value is missing or can’t be converted.

```swift
try await config.watchRequiredString(forKey: ["server", "port"]) { updates in
    for try await port in updates {
        print("Server port is: \(port)")
    }
}
```

> **Throws**: Rethrows any error thrown by the handler or the underlying watch operation.

## Parameters

- `key`: The config key to watch.
- `isSecret`: Whether the value should be treated as secret for logging and debugging purposes.
- `fileID`: The file ID where this call originates. Used for access reporting.
- `line`: The line number where this call originates. Used for access reporting.
- `updatesHandler`: A closure that handles an async sequence of updates to the value. The sequence produces an error if the provider returned a `nil` value or if the value was of an incorrect type.

## See Also

### Watching required string values
- [func watchRequiredString<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Value, any Error>) async throws -> Return) async throws -> Return](./watchrequiredstring%28forkey,as,issecret,fileid,line,updateshandler%29-581rg.md)
  Watches for updates to a required config value for the given config key, converting from string.
- [func watchRequiredString<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Value, any Error>) async throws -> Return) async throws -> Return](./watchrequiredstring%28forkey,as,issecret,fileid,line,updateshandler%29-13z9o.md)
  Watches for updates to a required config value for the given config key, converting from string.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/watchrequiredstring(forkey:issecret:fileid:line:updateshandler:))*
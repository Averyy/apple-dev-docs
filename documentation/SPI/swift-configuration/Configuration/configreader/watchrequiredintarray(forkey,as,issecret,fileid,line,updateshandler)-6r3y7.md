---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/watchrequiredintarray(forkey:as:issecret:fileid:line:updateshandler:)-6r3y7"
framework: "swift-configuration/Configuration"
---

# watchRequiredIntArray(forKey:as:isSecret:fileID:line:updatesHandler:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Watches for updates to a required array of config values for the given config key, converting from integers.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func watchRequiredIntArray<Value, Return>(forKey key: ConfigKey, as type: Value.Type = Value.self, isSecret: Bool = false, fileID: String = #fileID, line: UInt = #line, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[Value], any Error>) async throws -> Return) async throws -> Return where Value : RawRepresentable, Value : Sendable, Value.RawValue == Int, Return : ~Copyable
```

## Return Value

The result produced by the handler.

## Discussion

Use this method to observe changes to mandatory integer-convertible array configuration values over time. The handler receives an async sequence that produces the current array whenever it changes, or throws an error if the value is missing or can’t be converted.

```swift
try await config.watchRequiredIntArray(forKey: ["api", "versions"], as: APIVersion.self) { updates in
    for try await versions in updates {
        print("Api versions: \(versions.map(\.description).joined(separator: ", "))")
    }
}
```

> **Throws**: Rethrows any error thrown by the handler or the underlying watch operation.

## Parameters

- `key`: The config key to watch.
- `type`: The element type to convert each integer value to.
- `isSecret`: Whether the value should be treated as secret for logging and debugging purposes.
- `fileID`: The file ID where this call originates. Used for access reporting.
- `line`: The line number where this call originates. Used for access reporting.
- `updatesHandler`: A closure that handles an async sequence of updates to the value. The sequence produces an error if the provider returned a `nil` value or if the value was of an incorrect type.

## See Also

### Watching required lists of integer values
- [func watchRequiredIntArray<Return>(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[Int], any Error>) async throws -> Return) async throws -> Return](./watchrequiredintarray%28forkey,issecret,fileid,line,updateshandler%29.md)
  Watches for updates to a required config value for the given config key.
- [func watchRequiredIntArray<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[Value], any Error>) async throws -> Return) async throws -> Return](./watchrequiredintarray%28forkey,as,issecret,fileid,line,updateshandler%29-84hp3.md)
  Watches for updates to a required array of config values for the given config key, converting from integers.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/watchrequiredintarray(forkey:as:issecret:fileid:line:updateshandler:)-6r3y7)*
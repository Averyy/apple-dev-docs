---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/fetchstring(forkey:as:issecret:default:fileid:line:)-9vhmw"
framework: "swift-configuration/Configuration"
---

# fetchString(forKey:as:isSecret:default:fileID:line:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Asynchronously fetches a config value for the given config key with default fallback, converting from string.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func fetchString<Value>(forKey key: ConfigKey, as type: Value.Type = Value.self, isSecret: Bool = false, default defaultValue: Value, fileID: String = #fileID, line: UInt = #line) async throws -> Value where Value : ExpressibleByConfigString
```

## Return Value

The config value if found and convertible, otherwise the default value.

## Discussion

Use this method when you need a guaranteed non-nil result from an async provider for string-convertible types. If the configuration value is missing, the method returns the default value instead.

```swift
let serverMode = try await config.fetchString(forKey: ["server", "mode"], as: ServerMode.self, default: .production)
```

> **Throws**: An error if the underlying provider throws or if the value can’t be converted to the expected type.

## Parameters

- `key`: The config key to look up.
- `type`: The type to convert the string value to.
- `isSecret`: Whether the value should be treated as secret for logging and debugging purposes.
- `defaultValue`: The fallback value returned when the config value is missing or invalid.
- `fileID`: The file ID where this call originates. Used for access reporting.
- `line`: The line number where this call originates. Used for access reporting.

## See Also

### Asynchronously fetching string values
- [func fetchString(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) async throws -> String?](./fetchstring%28forkey,issecret,fileid,line%29.md)
  Asynchronously fetches a config value for the given config key.
- [func fetchString(forKey: ConfigKey, isSecret: Bool, default: String, fileID: String, line: UInt) async throws -> String](./fetchstring%28forkey,issecret,default,fileid,line%29.md)
  Asynchronously fetches a config value for the given config key, with a default fallback.
- [func fetchString<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) async throws -> Value?](./fetchstring%28forkey,as,issecret,fileid,line%29-6m5tu.md)
  Asynchronously fetches a config value for the given config key, converting from string.
- [func fetchString<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) async throws -> Value?](./fetchstring%28forkey,as,issecret,fileid,line%29-2zxxs.md)
  Asynchronously fetches a config value for the given config key, converting from string.
- [func fetchString<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: Value, fileID: String, line: UInt) async throws -> Value](./fetchstring%28forkey,as,issecret,default,fileid,line%29-7hxpy.md)
  Asynchronously fetches a config value for the given config key with default fallback, converting from string.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/fetchstring(forkey:as:issecret:default:fileid:line:)-9vhmw)*
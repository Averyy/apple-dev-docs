---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/fetchstringarray(forkey:issecret:default:fileid:line:)"
framework: "swift-configuration/Configuration"
---

# fetchStringArray(forKey:isSecret:default:fileID:line:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Asynchronously fetches a config value for the given config key, with a default fallback.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func fetchStringArray(forKey key: ConfigKey, isSecret: Bool = false, default defaultValue: [String], fileID: String = #fileID, line: UInt = #line) async throws -> [String]
```

#### Return Value

The config value if found and convertible, otherwise the default value.

#### Discussion

Use this method when you need a guaranteed non-nil result from an async provider. If the configuration value is missing, the method returns the default value instead.

```swift
let maxRetries = try await config.fetchStringArray(forKey: ["network", "maxRetries"], default: ["hello", "world"])
```

> **Throws**: An error if the underlying provider throws or if the value can’t be converted to the expected type.

## Parameters

- `key`: The config key to look up.
- `isSecret`: Whether the value should be treated as secret for logging and debugging purposes.
- `defaultValue`: The fallback value returned when the config value is missing or invalid.
- `fileID`: The file ID where this call originates. Used for access reporting.
- `line`: The line number where this call originates. Used for access reporting.

## See Also

### Asynchronously fetching lists of string values
- [func fetchStringArray(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) async throws -> [String]?](./fetchstringarray%28forkey,issecret,fileid,line%29.md)
  Asynchronously fetches a config value for the given config key.
- [func fetchStringArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) async throws -> [Value]?](./fetchstringarray%28forkey,as,issecret,fileid,line%29-4yv3p.md)
  Asynchronously fetches an array of config values for the given config key, converting from strings.
- [func fetchStringArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) async throws -> [Value]?](./fetchstringarray%28forkey,as,issecret,fileid,line%29-4nmik.md)
  Asynchronously fetches an array of config values for the given config key, converting from strings.
- [func fetchStringArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: [Value], fileID: String, line: UInt) async throws -> [Value]](./fetchstringarray%28forkey,as,issecret,default,fileid,line%29-1fcex.md)
  Asynchronously fetches an array of config values for the given config key with default fallback, converting from strings.
- [func fetchStringArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: [Value], fileID: String, line: UInt) async throws -> [Value]](./fetchstringarray%28forkey,as,issecret,default,fileid,line%29-3te90.md)
  Asynchronously fetches an array of config values for the given config key with default fallback, converting from strings.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/fetchstringarray(forkey:issecret:default:fileid:line:))*
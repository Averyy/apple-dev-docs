---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/fetchstringarray(forkey:as:issecret:fileid:line:)-4nmik"
framework: "swift-configuration/Configuration"
---

# fetchStringArray(forKey:as:isSecret:fileID:line:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Asynchronously fetches an array of config values for the given config key, converting from strings.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func fetchStringArray<Value>(forKey key: ConfigKey, as type: Value.Type = Value.self, isSecret: Bool = false, fileID: String = #fileID, line: UInt = #line) async throws -> [Value]? where Value : RawRepresentable, Value.RawValue == String
```

## Return Value

An array of values converted to the expected type if found and convertible, otherwise `nil`.

## Discussion

Use this method to retrieve configuration arrays where each element can be converted from strings using async providers. If the value doesn’t exist, the method returns `nil`.

```swift
let serverModes = try await config.fetchStringArray(forKey: ["server", "allowedModes"], as: ServerMode.self)
```

> **Throws**: An error if the underlying provider throws or if the value can’t be converted to the expected type.

## Parameters

- `key`: The config key to look up.
- `type`: The element type to convert each string value to.
- `isSecret`: Whether the value should be treated as secret for logging and debugging purposes.
- `fileID`: The file ID where this call originates. Used for access reporting.
- `line`: The line number where this call originates. Used for access reporting.

## See Also

### Asynchronously fetching lists of string values
- [func fetchStringArray(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) async throws -> [String]?](./fetchstringarray%28forkey,issecret,fileid,line%29.md)
  Asynchronously fetches a config value for the given config key.
- [func fetchStringArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) async throws -> [Value]?](./fetchstringarray%28forkey,as,issecret,fileid,line%29-4yv3p.md)
  Asynchronously fetches an array of config values for the given config key, converting from strings.
- [func fetchStringArray(forKey: ConfigKey, isSecret: Bool, default: [String], fileID: String, line: UInt) async throws -> [String]](./fetchstringarray%28forkey,issecret,default,fileid,line%29.md)
  Asynchronously fetches a config value for the given config key, with a default fallback.
- [func fetchStringArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: [Value], fileID: String, line: UInt) async throws -> [Value]](./fetchstringarray%28forkey,as,issecret,default,fileid,line%29-1fcex.md)
  Asynchronously fetches an array of config values for the given config key with default fallback, converting from strings.
- [func fetchStringArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: [Value], fileID: String, line: UInt) async throws -> [Value]](./fetchstringarray%28forkey,as,issecret,default,fileid,line%29-3te90.md)
  Asynchronously fetches an array of config values for the given config key with default fallback, converting from strings.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/fetchstringarray(forkey:as:issecret:fileid:line:)-4nmik)*
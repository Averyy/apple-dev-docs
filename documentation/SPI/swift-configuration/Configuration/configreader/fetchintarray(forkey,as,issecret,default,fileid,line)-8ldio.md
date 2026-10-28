---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/fetchintarray(forkey:as:issecret:default:fileid:line:)-8ldio"
framework: "swift-configuration/Configuration"
---

# fetchIntArray(forKey:as:isSecret:default:fileID:line:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Asynchronously fetches an array of config values for the given config key with default fallback, converting from integers.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func fetchIntArray<Value>(forKey key: ConfigKey, as type: Value.Type = Value.self, isSecret: Bool = false, default defaultValue: [Value], fileID: String = #fileID, line: UInt = #line) async throws -> [Value] where Value : ExpressibleByConfigInt
```

## Return Value

The config array if found and convertible, otherwise the default array.

## Discussion

Use this method when you need a guaranteed non-nil result for integer-convertible array types from async providers. If the configuration value is missing, the method returns the default value instead.

```swift
let apiVersions = try await config.fetchIntArray(forKey: ["api", "versions"], as: APIVersion.self, default: [.version(1)])
```

> **Throws**: An error if the underlying provider throws or if the value can’t be converted to the expected type.

## Parameters

- `key`: The config key to look up.
- `type`: The element type to convert each integer value to.
- `isSecret`: Whether the value should be treated as secret for logging and debugging purposes.
- `defaultValue`: The fallback array returned when the config value is missing or invalid.
- `fileID`: The file ID where this call originates. Used for access reporting.
- `line`: The line number where this call originates. Used for access reporting.

## See Also

### Asynchronously fetching lists of integer values
- [func fetchIntArray(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) async throws -> [Int]?](./fetchintarray%28forkey,issecret,fileid,line%29.md)
  Asynchronously fetches a config value for the given config key.
- [func fetchIntArray(forKey: ConfigKey, isSecret: Bool, default: [Int], fileID: String, line: UInt) async throws -> [Int]](./fetchintarray%28forkey,issecret,default,fileid,line%29.md)
  Asynchronously fetches a config value for the given config key, with a default fallback.
- [func fetchIntArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) async throws -> [Value]?](./fetchintarray%28forkey,as,issecret,fileid,line%29-16vlr.md)
  Asynchronously fetches an array of config values for the given config key, converting from integers.
- [func fetchIntArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) async throws -> [Value]?](./fetchintarray%28forkey,as,issecret,fileid,line%29-6rhh4.md)
  Asynchronously fetches an array of config values for the given config key, converting from integers.
- [func fetchIntArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: [Value], fileID: String, line: UInt) async throws -> [Value]](./fetchintarray%28forkey,as,issecret,default,fileid,line%29-79l2m.md)
  Asynchronously fetches an array of config values for the given config key with default fallback, converting from integers.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/fetchintarray(forkey:as:issecret:default:fileid:line:)-8ldio)*
---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/fetchrequiredintarray(forkey:as:issecret:fileid:line:)-6a1e3"
framework: "swift-configuration/Configuration"
---

# fetchRequiredIntArray(forKey:as:isSecret:fileID:line:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Asynchronously fetches a required array of config values for the given config key, converting from integers.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func fetchRequiredIntArray<Value>(forKey key: ConfigKey, as type: Value.Type = Value.self, isSecret: Bool = false, fileID: String = #fileID, line: UInt = #line) async throws -> [Value] where Value : ExpressibleByConfigInt
```

#### Return Value

The config array converted to the expected type.

#### Discussion

Use this method when an integer-convertible array configuration value is mandatory for your application to function and you’re working with async providers. The method throws an error if the value is missing or can’t be converted to the expected type.

```swift
let requiredVersions = try await config.fetchRequiredIntArray(forKey: ["api", "versions"], as: APIVersion.self)
```

> **Throws**: An error if the underlying provider throws, the value is missing, or can’t be converted to the expected type.

## Parameters

- `key`: The config key to look up.
- `type`: The element type to convert each integer value to.
- `isSecret`: Whether the value should be treated as secret for logging and debugging purposes.
- `fileID`: The file ID where this call originates. Used for access reporting.
- `line`: The line number where this call originates. Used for access reporting.

## See Also

### Asynchronously fetching required lists of integer values
- [func fetchRequiredIntArray(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) async throws -> [Int]](./fetchrequiredintarray%28forkey,issecret,fileid,line%29.md)
  Asynchronously fetches a required config value for the given config key, throwing an error if it’s missing.
- [func fetchRequiredIntArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) async throws -> [Value]](./fetchrequiredintarray%28forkey,as,issecret,fileid,line%29-599c5.md)
  Asynchronously fetches a required array of config values for the given config key, converting from integers.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/fetchrequiredintarray(forkey:as:issecret:fileid:line:)-6a1e3)*
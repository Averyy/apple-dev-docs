---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/requiredint(forkey:as:issecret:fileid:line:)-3dzjk"
framework: "swift-configuration/Configuration"
---

# requiredInt(forKey:as:isSecret:fileID:line:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Synchronously gets a required config value for the given config key, converting from an integer.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func requiredInt<Value>(forKey key: ConfigKey, as type: Value.Type = Value.self, isSecret: Bool = false, fileID: String = #fileID, line: UInt = #line) throws -> Value where Value : ExpressibleByConfigInt
```

#### Return Value

The config value converted to the expected type.

#### Discussion

Use this method when an integer-convertible configuration value is mandatory for your application to function. The method throws an error if the value is missing or can’t be converted to the expected type.

```swift
let apiVersion = try config.requiredInt(forKey: ["api", "version"], as: APIVersion.self)
```

> **Throws**: An error if the value is missing or can’t be converted to the expected type.

## Parameters

- `key`: The config key to look up.
- `type`: The type to convert the integer value to.
- `isSecret`: Whether the value should be treated as secret for logging and debugging purposes.
- `fileID`: The file ID where this call originates. Used for access reporting.
- `line`: The line number where this call originates. Used for access reporting.

## See Also

### Synchronously reading required integer values
- [func requiredInt(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) throws -> Int](./requiredint%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a required config value for the given config key, throwing an error if it’s missing.
- [func requiredInt<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) throws -> Value](./requiredint%28forkey,as,issecret,fileid,line%29-2xiji.md)
  Synchronously gets a required config value for the given config key, converting from an integer.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/requiredint(forkey:as:issecret:fileid:line:)-3dzjk)*
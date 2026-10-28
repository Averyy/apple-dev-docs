---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/requiredintarray(forkey:issecret:fileid:line:)"
framework: "swift-configuration/Configuration"
---

# requiredIntArray(forKey:isSecret:fileID:line:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Synchronously gets a required config value for the given config key, throwing an error if it’s missing.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func requiredIntArray(forKey key: ConfigKey, isSecret: Bool = false, fileID: String = #fileID, line: UInt = #line) throws -> [Int]
```

## Return Value

The config value converted to the expected type.

## Discussion

Use this method when a configuration value is mandatory for your application to function. The method throws an error if the value is missing or can’t be converted to the expected type.

```swift
let apiKey = try config.requiredIntArray(forKey: ["api", "key"], isSecret: true)
```

> **Throws**: An error if the value is missing or can’t be converted to the expected type.

## Parameters

- `key`: The config key to look up.
- `isSecret`: Whether the value should be treated as secret for logging and debugging purposes.
- `fileID`: The file ID where this call originates. Used for access reporting.
- `line`: The line number where this call originates. Used for access reporting.

## See Also

### Synchronously reading required lists of integer values
- [func requiredIntArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) throws -> [Value]](./requiredintarray%28forkey,as,issecret,fileid,line%29-cyh0.md)
  Synchronously gets a required array of config values for the given config key, converting from integers.
- [func requiredIntArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) throws -> [Value]](./requiredintarray%28forkey,as,issecret,fileid,line%29-1car4.md)
  Synchronously gets a required array of config values for the given config key, converting from integers.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/requiredintarray(forkey:issecret:fileid:line:))*
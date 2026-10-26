---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/requiredintarray(forkey:as:issecret:fileid:line:)-1car4"
framework: "swift-configuration/Configuration"
---

# requiredIntArray(forKey:as:isSecret:fileID:line:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Synchronously gets a required array of config values for the given config key, converting from integers.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func requiredIntArray<Value>(forKey key: ConfigKey, as type: Value.Type = Value.self, isSecret: Bool = false, fileID: String = #fileID, line: UInt = #line) throws -> [Value] where Value : ExpressibleByConfigInt
```

#### Return Value

The config array converted to the expected type.

#### Discussion

Use this method when an integer-convertible array configuration value is mandatory for your application to function. The method throws an error if the value is missing or can’t be converted to the expected type.

```swift
let apiVersions = try config.requiredIntArray(forKey: ["api", "versions"], as: APIVersion.self)
```

> **Throws**: An error if the value is missing or can’t be converted to the expected type.

## Parameters

- `key`: The config key to look up.
- `type`: The element type to convert each integer value to.
- `isSecret`: Whether the value should be treated as secret for logging and debugging purposes.
- `fileID`: The file ID where this call originates. Used for access reporting.
- `line`: The line number where this call originates. Used for access reporting.

## See Also

### Synchronously reading required lists of integer values
- [func requiredIntArray(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) throws -> [Int]](./requiredintarray%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a required config value for the given config key, throwing an error if it’s missing.
- [func requiredIntArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) throws -> [Value]](./requiredintarray%28forkey,as,issecret,fileid,line%29-cyh0.md)
  Synchronously gets a required array of config values for the given config key, converting from integers.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/requiredintarray(forkey:as:issecret:fileid:line:)-1car4)*
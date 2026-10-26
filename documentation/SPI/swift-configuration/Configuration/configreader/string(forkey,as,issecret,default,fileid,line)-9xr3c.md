---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/string(forkey:as:issecret:default:fileid:line:)-9xr3c"
framework: "swift-configuration/Configuration"
---

# string(forKey:as:isSecret:default:fileID:line:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Synchronously gets a config value for the given config key with default fallback, converting from string.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func string<Value>(forKey key: ConfigKey, as type: Value.Type = Value.self, isSecret: Bool = false, default defaultValue: Value, fileID: String = #fileID, line: UInt = #line) -> Value where Value : RawRepresentable, Value.RawValue == String
```

#### Return Value

The config value if found and convertible, otherwise the default value.

#### Discussion

Use this method when you need a guaranteed non-nil result for string-convertible types. If the configuration value is missing or can’t be converted to the expected type, the method returns the default value instead.

```swift
let serverMode = config.string(forKey: ["server", "mode"], as: ServerMode.self, default: .production)
```

## Parameters

- `key`: The config key to look up.
- `type`: The type to convert the string value to.
- `isSecret`: Whether the value should be treated as secret for logging and debugging purposes.
- `defaultValue`: The fallback value returned when the config value is missing or invalid.
- `fileID`: The file ID where this call originates. Used for access reporting.
- `line`: The line number where this call originates. Used for access reporting.

## See Also

### Synchronously reading string values
- [func string(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) -> String?](./string%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a config value for the given config key.
- [func string(forKey: ConfigKey, isSecret: Bool, default: String, fileID: String, line: UInt) -> String](./string%28forkey,issecret,default,fileid,line%29.md)
  Synchronously gets a config value for the given config key, with a default fallback.
- [func string<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) -> Value?](./string%28forkey,as,issecret,fileid,line%29-1syvw.md)
  Synchronously gets a config value for the given config key, converting from string.
- [func string<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) -> Value?](./string%28forkey,as,issecret,fileid,line%29-4oust.md)
  Synchronously gets a config value for the given config key, converting from string.
- [func string<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: Value, fileID: String, line: UInt) -> Value](./string%28forkey,as,issecret,default,fileid,line%29-1sqv7.md)
  Synchronously gets a config value for the given config key with default fallback, converting from string.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/string(forkey:as:issecret:default:fileid:line:)-9xr3c)*
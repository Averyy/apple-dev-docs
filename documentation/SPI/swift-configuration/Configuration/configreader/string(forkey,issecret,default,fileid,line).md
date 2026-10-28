---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/string(forkey:issecret:default:fileid:line:)"
framework: "swift-configuration/Configuration"
---

# string(forKey:isSecret:default:fileID:line:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Synchronously gets a config value for the given config key, with a default fallback.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func string(forKey key: ConfigKey, isSecret: Bool = false, default defaultValue: String, fileID: String = #fileID, line: UInt = #line) -> String
```

## Return Value

The config value if found and convertible, otherwise the default value.

## Discussion

Use this method when you need a guaranteed non-nil result. If the configuration value is missing or can’t be converted to the expected type, the method returns the default value instead.

```swift
let maxRetries = config.string(forKey: ["network", "maxRetries"], default: "hello")
```

## Parameters

- `key`: The config key to look up.
- `isSecret`: Whether the value should be treated as secret for logging and debugging purposes.
- `defaultValue`: The fallback value returned when the config value is missing or invalid.
- `fileID`: The file ID where this call originates. Used for access reporting.
- `line`: The line number where this call originates. Used for access reporting.

## See Also

### Synchronously reading string values
- [func string(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) -> String?](./string%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a config value for the given config key.
- [func string<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) -> Value?](./string%28forkey,as,issecret,fileid,line%29-1syvw.md)
  Synchronously gets a config value for the given config key, converting from string.
- [func string<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) -> Value?](./string%28forkey,as,issecret,fileid,line%29-4oust.md)
  Synchronously gets a config value for the given config key, converting from string.
- [func string<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: Value, fileID: String, line: UInt) -> Value](./string%28forkey,as,issecret,default,fileid,line%29-9xr3c.md)
  Synchronously gets a config value for the given config key with default fallback, converting from string.
- [func string<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: Value, fileID: String, line: UInt) -> Value](./string%28forkey,as,issecret,default,fileid,line%29-1sqv7.md)
  Synchronously gets a config value for the given config key with default fallback, converting from string.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/string(forkey:issecret:default:fileid:line:))*
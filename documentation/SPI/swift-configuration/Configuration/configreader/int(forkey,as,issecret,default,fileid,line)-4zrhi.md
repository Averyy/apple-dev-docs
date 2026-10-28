---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/int(forkey:as:issecret:default:fileid:line:)-4zrhi"
framework: "swift-configuration/Configuration"
---

# int(forKey:as:isSecret:default:fileID:line:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Synchronously gets a config value for the given config key with default fallback, converting from an integer.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func int<Value>(forKey key: ConfigKey, as type: Value.Type = Value.self, isSecret: Bool = false, default defaultValue: Value, fileID: String = #fileID, line: UInt = #line) -> Value where Value : RawRepresentable, Value.RawValue == Int
```

## Return Value

The config value if found and convertible, otherwise the default value.

## Discussion

Use this method when you need a guaranteed non-nil result for integer-convertible types. If the configuration value is missing or can’t be converted to the expected type, the method returns the default value

```swift
let apiVersion = config.int(forKey: ["api", "version"], as: APIVersion.self, default: .version(1))
```

## Parameters

- `key`: The config key to look up.
- `type`: The type to convert the integer value to.
- `isSecret`: Whether the value should be treated as secret for logging and debugging purposes.
- `defaultValue`: The fallback value returned when the config value is missing or invalid.
- `fileID`: The file ID where this call originates. Used for access reporting.
- `line`: The line number where this call originates. Used for access reporting.

## See Also

### Synchronously reading integer values
- [func int(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) -> Int?](./int%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a config value for the given config key.
- [func int(forKey: ConfigKey, isSecret: Bool, default: Int, fileID: String, line: UInt) -> Int](./int%28forkey,issecret,default,fileid,line%29.md)
  Synchronously gets a config value for the given config key, with a default fallback.
- [func int<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) -> Value?](./int%28forkey,as,issecret,fileid,line%29-6ng32.md)
  Synchronously gets a config value for the given config key, converting from an integer.
- [func int<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) -> Value?](./int%28forkey,as,issecret,fileid,line%29-11fn2.md)
  Synchronously gets a config value for the given config key, converting from an integer.
- [func int<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: Value, fileID: String, line: UInt) -> Value](./int%28forkey,as,issecret,default,fileid,line%29-4ie6l.md)
  Synchronously gets a config value for the given config key with default fallback, converting from an integer.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/int(forkey:as:issecret:default:fileid:line:)-4zrhi)*
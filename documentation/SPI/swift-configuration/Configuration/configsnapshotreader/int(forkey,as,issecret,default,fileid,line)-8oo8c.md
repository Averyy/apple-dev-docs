---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configsnapshotreader/int(forkey:as:issecret:default:fileid:line:)-8oo8c"
framework: "swift-configuration/Configuration"
---

# int(forKey:as:isSecret:default:fileID:line:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Synchronously gets a config value for the given config key with default fallback, converting from integer.

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

Use this method when you need a guaranteed non-nil result for integer-convertible types. If the configuration value is missing or can’t be converted to the expected type, the default value is returned instead.

```swift
let apiVersion = snapshot.int(forKey: ["api", "version"], as: APIVersion.self, default: .one)
```

## Parameters

- `key`: The config key to look up.
- `type`: The type to convert the int value to.
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
- [func int<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) -> Value?](./int%28forkey,as,issecret,fileid,line%29-3edsa.md)
  Synchronously gets a config value for the given config key, converting from integer.
- [func int<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) -> Value?](./int%28forkey,as,issecret,fileid,line%29-1l91m.md)
  Synchronously gets a config value for the given config key, converting from integer.
- [func int<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: Value, fileID: String, line: UInt) -> Value](./int%28forkey,as,issecret,default,fileid,line%29-3a0gv.md)
  Synchronously gets a config value for the given config key with default fallback, converting from integer.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configsnapshotreader/int(forkey:as:issecret:default:fileid:line:)-8oo8c)*
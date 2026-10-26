---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/int(forkey:as:issecret:fileid:line:)-6ng32"
framework: "swift-configuration/Configuration"
---

# int(forKey:as:isSecret:fileID:line:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Synchronously gets a config value for the given config key, converting from an integer.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func int<Value>(forKey key: ConfigKey, as type: Value.Type = Value.self, isSecret: Bool = false, fileID: String = #fileID, line: UInt = #line) -> Value? where Value : RawRepresentable, Value.RawValue == Int
```

#### Return Value

The value converted to the expected type if found and convertible, otherwise `nil`.

#### Discussion

Use this method to retrieve configuration values that can be converted from integers, such as custom types conforming to integer conversion protocols. If the value doesn’t exist or can’t be converted to the expected type, the method returns `nil`.

```swift
let apiVersion = config.int(forKey: ["api", "version"], as: APIVersion.self)
```

## Parameters

- `key`: The config key to look up.
- `type`: The type to convert the integer value to.
- `isSecret`: Whether the value should be treated as secret for logging and debugging purposes.
- `fileID`: The file ID where this call originates. Used for access reporting.
- `line`: The line number where this call originates. Used for access reporting.

## See Also

### Synchronously reading integer values
- [func int(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) -> Int?](./int%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a config value for the given config key.
- [func int(forKey: ConfigKey, isSecret: Bool, default: Int, fileID: String, line: UInt) -> Int](./int%28forkey,issecret,default,fileid,line%29.md)
  Synchronously gets a config value for the given config key, with a default fallback.
- [func int<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) -> Value?](./int%28forkey,as,issecret,fileid,line%29-11fn2.md)
  Synchronously gets a config value for the given config key, converting from an integer.
- [func int<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: Value, fileID: String, line: UInt) -> Value](./int%28forkey,as,issecret,default,fileid,line%29-4zrhi.md)
  Synchronously gets a config value for the given config key with default fallback, converting from an integer.
- [func int<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: Value, fileID: String, line: UInt) -> Value](./int%28forkey,as,issecret,default,fileid,line%29-4ie6l.md)
  Synchronously gets a config value for the given config key with default fallback, converting from an integer.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/int(forkey:as:issecret:fileid:line:)-6ng32)*
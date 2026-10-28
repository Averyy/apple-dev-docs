---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configsnapshotreader/int(forkey:as:issecret:fileid:line:)-1l91m"
framework: "swift-configuration/Configuration"
---

# int(forKey:as:isSecret:fileID:line:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Synchronously gets a config value for the given config key, converting from integer.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func int<Value>(forKey key: ConfigKey, as type: Value.Type = Value.self, isSecret: Bool = false, fileID: String = #fileID, line: UInt = #line) -> Value? where Value : ExpressibleByConfigInt
```

## Return Value

The value converted to the expected type if found and convertible, otherwise `nil`.

## Discussion

Use this method to retrieve configuration values that can be converted from integers, such as custom types conforming to int conversion protocols. If the value doesn’t exist or can’t be converted to the expected type, the method returns `nil`.

```swift
let apiVersion = snapshot.int(forKey: ["api", "version"], as: APIVersion.self)
```

## Parameters

- `key`: The config key to look up.
- `type`: The type to convert the int value to.
- `isSecret`: Whether the value should be treated as secret for logging and debugging purposes.
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
- [func int<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: Value, fileID: String, line: UInt) -> Value](./int%28forkey,as,issecret,default,fileid,line%29-8oo8c.md)
  Synchronously gets a config value for the given config key with default fallback, converting from integer.
- [func int<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: Value, fileID: String, line: UInt) -> Value](./int%28forkey,as,issecret,default,fileid,line%29-3a0gv.md)
  Synchronously gets a config value for the given config key with default fallback, converting from integer.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configsnapshotreader/int(forkey:as:issecret:fileid:line:)-1l91m)*
---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configsnapshotreader/string(forkey:as:issecret:fileid:line:)-7bpif"
framework: "swift-configuration/Configuration"
---

# string(forKey:as:isSecret:fileID:line:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Synchronously gets a config value for the given config key, converting from string.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func string<Value>(forKey key: ConfigKey, as type: Value.Type = Value.self, isSecret: Bool = false, fileID: String = #fileID, line: UInt = #line) -> Value? where Value : RawRepresentable, Value.RawValue == String
```

#### Return Value

The value converted to the expected type if found and convertible, otherwise `nil`.

#### Discussion

Use this method to retrieve configuration values that can be converted from strings, such as custom types conforming to string conversion protocols. If the value doesn’t exist or can’t be converted to the expected type, the method returns `nil`.

```swift
let serverMode = snapshot.string(forKey: ["server", "mode"], as: ServerMode.self)
```

## Parameters

- `key`: The config key to look up.
- `type`: The type to convert the string value to.
- `isSecret`: Whether the value should be treated as secret for logging and debugging purposes.
- `fileID`: The file ID where this call originates. Used for access reporting.
- `line`: The line number where this call originates. Used for access reporting.

## See Also

### Synchronously reading string values
- [func string(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) -> String?](./string%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a config value for the given config key.
- [func string(forKey: ConfigKey, isSecret: Bool, default: String, fileID: String, line: UInt) -> String](./string%28forkey,issecret,default,fileid,line%29.md)
  Synchronously gets a config value for the given config key, with a default fallback.
- [func string<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) -> Value?](./string%28forkey,as,issecret,fileid,line%29-8hlcf.md)
  Synchronously gets a config value for the given config key, converting from string.
- [func string<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: Value, fileID: String, line: UInt) -> Value](./string%28forkey,as,issecret,default,fileid,line%29-fzpe.md)
  Synchronously gets a config value for the given config key with default fallback, converting from string.
- [func string<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: Value, fileID: String, line: UInt) -> Value](./string%28forkey,as,issecret,default,fileid,line%29-2mphx.md)
  Synchronously gets a config value for the given config key with default fallback, converting from string.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configsnapshotreader/string(forkey:as:issecret:fileid:line:)-7bpif)*
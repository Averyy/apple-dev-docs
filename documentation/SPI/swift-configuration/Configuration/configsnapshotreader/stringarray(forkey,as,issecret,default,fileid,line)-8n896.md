---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configsnapshotreader/stringarray(forkey:as:issecret:default:fileid:line:)-8n896"
framework: "swift-configuration/Configuration"
---

# stringArray(forKey:as:isSecret:default:fileID:line:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Synchronously gets an array of config values for the given config key with default fallback, converting from strings.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func stringArray<Value>(forKey key: ConfigKey, as type: Value.Type = Value.self, isSecret: Bool = false, default defaultValue: [Value], fileID: String = #fileID, line: UInt = #line) -> [Value] where Value : ExpressibleByConfigString
```

#### Return Value

The config array if found and convertible, otherwise the default array.

#### Discussion

Use this method when you need a guaranteed non-nil result for string-convertible array types. If the configuration value is missing or can’t be converted to the expected type, the method returns the default value instead.

```swift
let serverModes = snapshot.stringArray(forKey: ["server", "allowedModes"], as: ServerMode.self, default: [.production])
```

## Parameters

- `key`: The config key to look up.
- `type`: The element type to convert each string value to.
- `isSecret`: Whether the value should be treated as secret for logging and debugging purposes.
- `defaultValue`: The fallback array returned when the config value is missing or invalid.
- `fileID`: The file ID where this call originates. Used for access reporting.
- `line`: The line number where this call originates. Used for access reporting.

## See Also

### Synchronously reading lists of string values
- [func stringArray(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) -> [String]?](./stringarray%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a config value for the given config key.
- [func stringArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) -> [Value]?](./stringarray%28forkey,as,issecret,fileid,line%29-7athn.md)
  Synchronously gets an array of config values for the given config key, converting from strings.
- [func stringArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) -> [Value]?](./stringarray%28forkey,as,issecret,fileid,line%29-v5ap.md)
  Synchronously gets an array of config values for the given config key, converting from strings.
- [func stringArray(forKey: ConfigKey, isSecret: Bool, default: [String], fileID: String, line: UInt) -> [String]](./stringarray%28forkey,issecret,default,fileid,line%29.md)
  Synchronously gets a config value for the given config key, with a default fallback.
- [func stringArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: [Value], fileID: String, line: UInt) -> [Value]](./stringarray%28forkey,as,issecret,default,fileid,line%29-yx0h.md)
  Synchronously gets an array of config values for the given config key with default fallback, converting from strings.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configsnapshotreader/stringarray(forkey:as:issecret:default:fileid:line:)-8n896)*
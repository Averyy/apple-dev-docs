---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configsnapshotreader/stringarray(forkey:issecret:fileid:line:)"
framework: "swift-configuration/Configuration"
---

# stringArray(forKey:isSecret:fileID:line:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Synchronously gets a config value for the given config key.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func stringArray(forKey key: ConfigKey, isSecret: Bool = false, fileID: String = #fileID, line: UInt = #line) -> [String]?
```

#### Return Value

The value converted to the expected type if found and convertible, otherwise `nil`.

#### Discussion

Use this method to retrieve optional configuration values from a snapshot. If the value doesn’t exist or can’t be converted to the expected type, the method returns `nil`.

```swift
let port = snapshot.int(forKey: ["server", "port"])
```

## Parameters

- `key`: The config key to look up.
- `isSecret`: Whether the value should be treated as secret for logging and debugging purposes.
- `fileID`: The file ID where this call originates. Used for access reporting.
- `line`: The line number where this call originates. Used for access reporting.

## See Also

### Synchronously reading lists of string values
- [func stringArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) -> [Value]?](./stringarray%28forkey,as,issecret,fileid,line%29-7athn.md)
  Synchronously gets an array of config values for the given config key, converting from strings.
- [func stringArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) -> [Value]?](./stringarray%28forkey,as,issecret,fileid,line%29-v5ap.md)
  Synchronously gets an array of config values for the given config key, converting from strings.
- [func stringArray(forKey: ConfigKey, isSecret: Bool, default: [String], fileID: String, line: UInt) -> [String]](./stringarray%28forkey,issecret,default,fileid,line%29.md)
  Synchronously gets a config value for the given config key, with a default fallback.
- [func stringArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: [Value], fileID: String, line: UInt) -> [Value]](./stringarray%28forkey,as,issecret,default,fileid,line%29-8n896.md)
  Synchronously gets an array of config values for the given config key with default fallback, converting from strings.
- [func stringArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: [Value], fileID: String, line: UInt) -> [Value]](./stringarray%28forkey,as,issecret,default,fileid,line%29-yx0h.md)
  Synchronously gets an array of config values for the given config key with default fallback, converting from strings.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configsnapshotreader/stringarray(forkey:issecret:fileid:line:))*
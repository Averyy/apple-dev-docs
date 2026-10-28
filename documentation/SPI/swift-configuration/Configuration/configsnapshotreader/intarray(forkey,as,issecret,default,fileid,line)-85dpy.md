---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configsnapshotreader/intarray(forkey:as:issecret:default:fileid:line:)-85dpy"
framework: "swift-configuration/Configuration"
---

# intArray(forKey:as:isSecret:default:fileID:line:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Synchronously gets an array of config values for the given config key with default fallback, converting from integers.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func intArray<Value>(forKey key: ConfigKey, as type: Value.Type = Value.self, isSecret: Bool = false, default defaultValue: [Value], fileID: String = #fileID, line: UInt = #line) -> [Value] where Value : RawRepresentable, Value.RawValue == Int
```

## Return Value

The config array if found and convertible, otherwise the default array.

## Discussion

Use this method when you need a guaranteed non-nil result for integer-convertible array types. If the configuration value is missing or can’t be converted to the expected type, the default value is returned instead.

```swift
let apiVersions = snapshot.intArray(forKey: ["api", "versions"], as: APIVersion.self, default: [.one])
```

## Parameters

- `key`: The config key to look up.
- `type`: The element type to convert each int value to.
- `isSecret`: Whether the value should be treated as secret for logging and debugging purposes.
- `defaultValue`: The fallback array returned when the config value is missing or invalid.
- `fileID`: The file ID where this call originates. Used for access reporting.
- `line`: The line number where this call originates. Used for access reporting.

## See Also

### Synchronously reading lists of integer values
- [func intArray(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) -> [Int]?](./intarray%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a config value for the given config key.
- [func intArray(forKey: ConfigKey, isSecret: Bool, default: [Int], fileID: String, line: UInt) -> [Int]](./intarray%28forkey,issecret,default,fileid,line%29.md)
  Synchronously gets a config value for the given config key, with a default fallback.
- [func intArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) -> [Value]?](./intarray%28forkey,as,issecret,fileid,line%29-5dw7j.md)
  Synchronously gets an array of config values for the given config key, converting from integers.
- [func intArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) -> [Value]?](./intarray%28forkey,as,issecret,fileid,line%29-8nwxy.md)
  Synchronously gets an array of config values for the given config key, converting from integers.
- [func intArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: [Value], fileID: String, line: UInt) -> [Value]](./intarray%28forkey,as,issecret,default,fileid,line%29-4u516.md)
  Synchronously gets an array of config values for the given config key with default fallback, converting from integers.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configsnapshotreader/intarray(forkey:as:issecret:default:fileid:line:)-85dpy)*
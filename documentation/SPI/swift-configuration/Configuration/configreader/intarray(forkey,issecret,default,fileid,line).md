---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/intarray(forkey:issecret:default:fileid:line:)"
framework: "swift-configuration/Configuration"
---

# intArray(forKey:isSecret:default:fileID:line:)

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
func intArray(forKey key: ConfigKey, isSecret: Bool = false, default defaultValue: [Int], fileID: String = #fileID, line: UInt = #line) -> [Int]
```

## Return Value

The config value if found and convertible, otherwise the default value.

## Discussion

Use this method when you need a guaranteed non-nil result. If the configuration value is missing or can’t be converted to the expected type, the method returns the default value instead.

```swift
let maxRetries = config.intArray(forKey: ["network", "maxRetries"], default: [1, 2, 3])
```

## Parameters

- `key`: The config key to look up.
- `isSecret`: Whether the value should be treated as secret for logging and debugging purposes.
- `defaultValue`: The fallback value returned when the config value is missing or invalid.
- `fileID`: The file ID where this call originates. Used for access reporting.
- `line`: The line number where this call originates. Used for access reporting.

## See Also

### Synchronously reading lists of integer values
- [func intArray(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) -> [Int]?](./intarray%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a config value for the given config key.
- [func intArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) -> [Value]?](./intarray%28forkey,as,issecret,fileid,line%29-3goaq.md)
  Synchronously gets an array of config values for the given config key, converting from integers.
- [func intArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) -> [Value]?](./intarray%28forkey,as,issecret,fileid,line%29-9sp0s.md)
  Synchronously gets an array of config values for the given config key, converting from integers.
- [func intArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: [Value], fileID: String, line: UInt) -> [Value]](./intarray%28forkey,as,issecret,default,fileid,line%29-9ini5.md)
  Synchronously gets an array of config values for the given config key with default fallback, converting from integers.
- [func intArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: [Value], fileID: String, line: UInt) -> [Value]](./intarray%28forkey,as,issecret,default,fileid,line%29-1so32.md)
  Synchronously gets an array of config values for the given config key with default fallback, converting from integers.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/intarray(forkey:issecret:default:fileid:line:))*
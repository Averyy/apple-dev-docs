---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/doublearray(forkey:issecret:fileid:line:)"
framework: "swift-configuration/Configuration"
---

# doubleArray(forKey:isSecret:fileID:line:)

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
func doubleArray(forKey key: ConfigKey, isSecret: Bool = false, fileID: String = #fileID, line: UInt = #line) -> [Double]?
```

#### Return Value

The value converted to the expected type if found and convertible, otherwise `nil`.

#### Discussion

Use this method to retrieve optional configuration values. If the value doesn’t exist or can’t be converted to the expected type, the method returns `nil`.

```swift
let port = config.doubleArray(forKey: ["server", "port"])
```

## Parameters

- `key`: The config key to look up.
- `isSecret`: Whether the value should be treated as secret for logging and debugging purposes.
- `fileID`: The file ID where this call originates. Used for access reporting.
- `line`: The line number where this call originates. Used for access reporting.

## See Also

### Synchronously reading lists of double values
- [func doubleArray(forKey: ConfigKey, isSecret: Bool, default: [Double], fileID: String, line: UInt) -> [Double]](./doublearray%28forkey,issecret,default,fileid,line%29.md)
  Synchronously gets a config value for the given config key, with a default fallback.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/doublearray(forkey:issecret:fileid:line:))*
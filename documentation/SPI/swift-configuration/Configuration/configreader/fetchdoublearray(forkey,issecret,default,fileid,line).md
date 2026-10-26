---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/fetchdoublearray(forkey:issecret:default:fileid:line:)"
framework: "swift-configuration/Configuration"
---

# fetchDoubleArray(forKey:isSecret:default:fileID:line:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Asynchronously fetches a config value for the given config key, with a default fallback.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func fetchDoubleArray(forKey key: ConfigKey, isSecret: Bool = false, default defaultValue: [Double], fileID: String = #fileID, line: UInt = #line) async throws -> [Double]
```

#### Return Value

The config value if found and convertible, otherwise the default value.

#### Discussion

Use this method when you need a guaranteed non-nil result from an async provider. If the configuration value is missing, the method returns the default value instead.

```swift
let maxRetries = try await config.fetchDoubleArray(forKey: ["network", "maxRetries"], default: [1.0, 2.0, 3.0])
```

> **Throws**: An error if the underlying provider throws or if the value can’t be converted to the expected type.

## Parameters

- `key`: The config key to look up.
- `isSecret`: Whether the value should be treated as secret for logging and debugging purposes.
- `defaultValue`: The fallback value returned when the config value is missing or invalid.
- `fileID`: The file ID where this call originates. Used for access reporting.
- `line`: The line number where this call originates. Used for access reporting.

## See Also

### Asynchronously fetching lists of double values
- [func fetchDoubleArray(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) async throws -> [Double]?](./fetchdoublearray%28forkey,issecret,fileid,line%29.md)
  Asynchronously fetches a config value for the given config key.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/fetchdoublearray(forkey:issecret:default:fileid:line:))*
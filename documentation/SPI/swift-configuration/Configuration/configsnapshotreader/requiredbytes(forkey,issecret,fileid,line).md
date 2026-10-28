---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configsnapshotreader/requiredbytes(forkey:issecret:fileid:line:)"
framework: "swift-configuration/Configuration"
---

# requiredBytes(forKey:isSecret:fileID:line:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Synchronously gets a required config value for the given config key, throwing an error if it’s missing.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func requiredBytes(forKey key: ConfigKey, isSecret: Bool = false, fileID: String = #fileID, line: UInt = #line) throws -> [UInt8]
```

## Return Value

The config value converted to the expected type.

## Discussion

Use this method when a configuration value is mandatory for your application to function. The method throws an error if the value is missing or can’t be converted to the expected type.

```swift
let apiKey = try snapshot.requiredString(forKey: ["api", "key"], isSecret: true)
```

> **Throws**: An error if the value is missing or can’t be converted to the expected type.

## Parameters

- `key`: The config key to look up.
- `isSecret`: Whether the value should be treated as secret for logging and debugging purposes.
- `fileID`: The file ID where this call originates. Used for access reporting.
- `line`: The line number where this call originates. Used for access reporting.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configsnapshotreader/requiredbytes(forkey:issecret:fileid:line:))*
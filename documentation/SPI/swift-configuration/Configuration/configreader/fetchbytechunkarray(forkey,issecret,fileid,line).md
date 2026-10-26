---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/fetchbytechunkarray(forkey:issecret:fileid:line:)"
framework: "swift-configuration/Configuration"
---

# fetchByteChunkArray(forKey:isSecret:fileID:line:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Asynchronously fetches a config value for the given config key.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func fetchByteChunkArray(forKey key: ConfigKey, isSecret: Bool = false, fileID: String = #fileID, line: UInt = #line) async throws -> [[UInt8]]?
```

#### Return Value

The value converted to the expected type if found and convertible, otherwise `nil`.

#### Discussion

Use this method when you need to retrieve configuration values from providers that support asynchronous operations, such as remote configuration services. Unlike synchronous get methods, this can handle providers that need to perform network requests or other async operations.

```swift
let timeout = try await config.fetchByteChunkArray(forKey: ["network", "timeout"])
```

> **Throws**: An error if the underlying provider throws or if the value can’t be converted to the expected type.

## Parameters

- `key`: The config key to look up.
- `isSecret`: Whether the value should be treated as secret for logging and debugging purposes.
- `fileID`: The file ID where this call originates. Used for access reporting.
- `line`: The line number where this call originates. Used for access reporting.

## See Also

### Asynchronously fetching lists of byte chunks
- [func fetchByteChunkArray(forKey: ConfigKey, isSecret: Bool, default: [[UInt8]], fileID: String, line: UInt) async throws -> [[UInt8]]](./fetchbytechunkarray%28forkey,issecret,default,fileid,line%29.md)
  Asynchronously fetches a config value for the given config key, with a default fallback.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/fetchbytechunkarray(forkey:issecret:fileid:line:))*
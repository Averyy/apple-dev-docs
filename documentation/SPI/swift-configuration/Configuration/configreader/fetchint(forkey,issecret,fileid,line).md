---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/fetchint(forkey:issecret:fileid:line:)"
framework: "swift-configuration/Configuration"
---

# fetchInt(forKey:isSecret:fileID:line:)

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
func fetchInt(forKey key: ConfigKey, isSecret: Bool = false, fileID: String = #fileID, line: UInt = #line) async throws -> Int?
```

#### Return Value

The value converted to the expected type if found and convertible, otherwise `nil`.

#### Discussion

Use this method when you need to retrieve configuration values from providers that support asynchronous operations, such as remote configuration services. Unlike synchronous get methods, this can handle providers that need to perform network requests or other async operations.

```swift
let timeout = try await config.fetchInt(forKey: ["network", "timeout"])
```

> **Throws**: An error if the underlying provider throws or if the value can’t be converted to the expected type.

## Parameters

- `key`: The config key to look up.
- `isSecret`: Whether the value should be treated as secret for logging and debugging purposes.
- `fileID`: The file ID where this call originates. Used for access reporting.
- `line`: The line number where this call originates. Used for access reporting.

## See Also

### Asynchronously fetching integer values
- [func fetchInt(forKey: ConfigKey, isSecret: Bool, default: Int, fileID: String, line: UInt) async throws -> Int](./fetchint%28forkey,issecret,default,fileid,line%29.md)
  Asynchronously fetches a config value for the given config key, with a default fallback.
- [func fetchInt<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) async throws -> Value?](./fetchint%28forkey,as,issecret,fileid,line%29-107qe.md)
  Asynchronously fetches a config value for the given config key, converting from an integer.
- [func fetchInt<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) async throws -> Value?](./fetchint%28forkey,as,issecret,fileid,line%29-6tdet.md)
  Asynchronously fetches a config value for the given config key, converting from an integer.
- [func fetchInt<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: Value, fileID: String, line: UInt) async throws -> Value](./fetchint%28forkey,as,issecret,default,fileid,line%29-3161u.md)
  Asynchronously fetches a config value for the given config key with default fallback, converting from an integer.
- [func fetchInt<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: Value, fileID: String, line: UInt) async throws -> Value](./fetchint%28forkey,as,issecret,default,fileid,line%29-41vzw.md)
  Asynchronously fetches a config value for the given config key with default fallback, converting from an integer.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/fetchint(forkey:issecret:fileid:line:))*
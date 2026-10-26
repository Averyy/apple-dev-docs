---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/fetchrequiredstringarray(forkey:as:issecret:fileid:line:)-1bf0t"
framework: "swift-configuration/Configuration"
---

# fetchRequiredStringArray(forKey:as:isSecret:fileID:line:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Asynchronously fetches a required array of config values for the given config key, converting from strings.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func fetchRequiredStringArray<Value>(forKey key: ConfigKey, as type: Value.Type = Value.self, isSecret: Bool = false, fileID: String = #fileID, line: UInt = #line) async throws -> [Value] where Value : RawRepresentable, Value.RawValue == String
```

#### Return Value

The config array converted to the expected type.

#### Discussion

Use this method when a string-convertible array configuration value is mandatory for your application to function and you’re working with async providers. The method throws an error if the value is missing or can’t be converted to the expected type.

```swift
let requiredModes = try await config.fetchRequiredStringArray(forKey: ["server", "allowedModes"], as: ServerMode.self)
```

> **Throws**: An error if the underlying provider throws, the value is missing, or can’t be converted to the expected type.

## Parameters

- `key`: The config key to look up.
- `type`: The element type to convert each string value to.
- `isSecret`: Whether the value should be treated as secret for logging and debugging purposes.
- `fileID`: The file ID where this call originates. Used for access reporting.
- `line`: The line number where this call originates. Used for access reporting.

## See Also

### Asynchronously fetching required lists of string values
- [func fetchRequiredStringArray(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) async throws -> [String]](./fetchrequiredstringarray%28forkey,issecret,fileid,line%29.md)
  Asynchronously fetches a required config value for the given config key, throwing an error if it’s missing.
- [func fetchRequiredStringArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) async throws -> [Value]](./fetchrequiredstringarray%28forkey,as,issecret,fileid,line%29-6es6t.md)
  Asynchronously fetches a required array of config values for the given config key, converting from strings.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/fetchrequiredstringarray(forkey:as:issecret:fileid:line:)-1bf0t)*
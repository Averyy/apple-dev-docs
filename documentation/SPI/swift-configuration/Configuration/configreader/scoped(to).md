---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/scoped(to:)"
framework: "swift-configuration/Configuration"
---

# scoped(to:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Returns a scoped config reader with the specified key appended to the current prefix.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func scoped(to configKey: ConfigKey) -> ConfigReader
```

## Mentions

- [Migrating to Swift Configuration](../migrating-to-swift-configuration.md)

#### Return Value

A config reader for accessing values within the specified scope.

#### Discussion

```swift
let httpConfig = config.scoped(to: ConfigKey(["http", "client"]))
let timeout = httpConfig.int(forKey: "timeout", default: 30) // Reads "http.client.timeout"
```

## Parameters

- `configKey`: The key components to append to the current key prefix.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/scoped(to:))*
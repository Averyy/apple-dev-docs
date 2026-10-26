---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configsnapshotreader/scoped(to:)"
framework: "swift-configuration/Configuration"
---

# scoped(to:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Returns a scoped snapshot reader by appending the provided key to the current key prefix.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func scoped(to configKey: ConfigKey) -> ConfigSnapshotReader
```

#### Return Value

A reader for accessing scoped values.

#### Discussion

Use this method to create a reader that accesses a subset of the configuration.

```swift
let httpConfig = snapshotReader.scoped(to: ["client", "http"])
let timeout = httpConfig.int(forKey: "timeout") // Reads from "client.http.timeout" in the snapshot
```

## Parameters

- `configKey`: The key to append to the current key prefix.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configsnapshotreader/scoped(to:))*
---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/loghandler/subscript(metadatakey:)"
framework: "swift-log/Logging"
---

# subscript(metadataKey:)

**Framework**: swift-log/Logging  
**Kind**: subscript  
**Role**: Instance Subscript  
**Required**: Yes

Add, remove, or change the logging metadata.

## Declaration

```swift
subscript(metadataKey _: String) -> Logger.Metadata.Value? { get set }
```

#### Overview

> **Note**: `LogHandler`s must treat logging metadata as a value type. This means that the change in metadata must only affect this very `LogHandler`.

## Parameters

- `metadataKey`: The key for the metadata item


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/loghandler/subscript(metadatakey:))*
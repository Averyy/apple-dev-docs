---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/accesslogger/report(_:)"
framework: "swift-configuration/Configuration"
---

# report(_:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Processes a configuration access event.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func report(_ event: AccessEvent)
```

#### Discussion

This method is called whenever a configuration value is accessed through a [`ConfigReader`](../configreader.md) or a [`ConfigSnapshotReader`](../configsnapshotreader.md). Implementations should handle events efficiently as they may be called frequently.

## Parameters

- `event`: The configuration access event to process.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/accesslogger/report(_:))*
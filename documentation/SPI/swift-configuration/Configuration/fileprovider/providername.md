---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/fileprovider/providername"
framework: "swift-configuration/Configuration"
---

# providerName

**Framework**: swift-configuration/Configuration  
**Kind**: property  
**Role**: Instance Property

The human-readable name of the configuration provider.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var providerName: String { get }
```

Available when `Snapshot` conforms to `FileConfigSnapshot`.

#### Discussion

Used by [`AccessReporter`](../accessreporter.md) and other diagnostic logging.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/fileprovider/providername)*
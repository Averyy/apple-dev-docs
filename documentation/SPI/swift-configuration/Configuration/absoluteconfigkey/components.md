---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/absoluteconfigkey/components"
framework: "swift-configuration/Configuration"
---

# components

**Framework**: swift-configuration/Configuration  
**Kind**: property  
**Role**: Instance Property

The hierarchical components that make up this absolute configuration key.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var components: [String]
```

#### Discussion

Each component represents a level in the configuration hierarchy, forming a complete path from the root of the configuration structure.

## See Also

### Inspecting an absolute configuration key
- [var context: [String : ConfigContextValue]](./context.md)
  Additional context information for this configuration key.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/absoluteconfigkey/components)*
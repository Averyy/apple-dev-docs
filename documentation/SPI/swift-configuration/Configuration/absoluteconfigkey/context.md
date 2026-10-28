---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/absoluteconfigkey/context"
framework: "swift-configuration/Configuration"
---

# context

**Framework**: swift-configuration/Configuration  
**Kind**: property  
**Role**: Instance Property

Additional context information for this configuration key.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var context: [String : ConfigContextValue]
```

## Discussion

Context provides extra information that providers can use to refine lookups or return more specific values. Not all providers use context information.

## See Also

### Inspecting an absolute configuration key
- [var components: [String]](./components.md)
  The hierarchical components that make up this absolute configuration key.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/absoluteconfigkey/context)*
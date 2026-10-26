---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/absoluteconfigkey/init(_:context:)"
framework: "swift-configuration/Configuration"
---

# init(_:context:)

**Framework**: swift-configuration/Configuration  
**Kind**: init  
**Role**: Initializer

Creates a new absolute configuration key.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(_ components: [String], context: [String : ConfigContextValue] = [:])
```

## Parameters

- `components`: The hierarchical components that make up the complete key path.
- `context`: Additional context information for the key.

## See Also

### Creating an absolute configuration key
- [init(ConfigKey)](./init%28_%29.md)
  Creates a new absolute configuration key from a relative key.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/absoluteconfigkey/init(_:context:))*
---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/keymappingprovider/prefixkeys(with:)"
framework: "swift-configuration/Configuration"
---

# prefixKeys(with:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Creates a new prefixed configuration provider.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func prefixKeys(with prefix: ConfigKey) -> KeyMappingProvider<Self>
```

## Return Value

A provider which prefixes keys with the given prefix.

## Discussion

- Parameter: prefix: The configuration key to prepend to all configuration keys.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/keymappingprovider/prefixkeys(with:))*
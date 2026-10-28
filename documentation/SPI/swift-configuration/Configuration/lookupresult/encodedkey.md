---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/lookupresult/encodedkey"
framework: "swift-configuration/Configuration"
---

# encodedKey

**Framework**: swift-configuration/Configuration  
**Kind**: property  
**Role**: Instance Property

The provider-specific encoding of the configuration key.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var encodedKey: String
```

## Discussion

This string shows how the provider interpreted and encoded the key for its data source, which is useful for debugging configuration lookups.

## See Also

### Inspecting a lookup result
- [var value: ConfigValue?](./value.md)
  The configuration value found for the key, or nil if not found.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/lookupresult/encodedkey)*
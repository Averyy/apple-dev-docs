---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/keymappingprovider/value(forkey:type:)"
framework: "swift-configuration/Configuration"
---

# value(forKey:type:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Returns the current value for the specified configuration key.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func value(forKey key: AbsoluteConfigKey, type: ConfigType) throws -> LookupResult
```

Available when `Upstream` conforms to `ConfigProvider`.

#### Return Value

The lookup result containing the value and encoded key, or nil if not found.

#### Discussion

This method provides synchronous access to configuration values and should be efficient to call repeatedly. The returned value may change between calls if the underlying data source is mutable.

> **Throws**: Provider-specific errors or type conversion errors.

## Parameters

- `key`: The configuration key to look up.
- `type`: The expected configuration value type.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/keymappingprovider/value(forkey:type:))*
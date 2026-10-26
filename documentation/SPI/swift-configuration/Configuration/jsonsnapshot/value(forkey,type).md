---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/jsonsnapshot/value(forkey:type:)"
framework: "swift-configuration/Configuration"
---

# value(forKey:type:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Returns a value for the specified key from this immutable snapshot.

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

#### Return Value

The lookup result containing the value and encoded key, or nil if not found.

#### Discussion

Unlike [`value(forKey:type:)`](../configprovider/value%28forkey,type%29.md), this method always returns the same value for identical parameters because the snapshot represents a fixed point in time. Values can be accessed synchronously and efficiently.

> **Throws**: Provider-specific errors or type conversion errors.

## Parameters

- `key`: The configuration key to look up.
- `type`: The expected configuration value type.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/jsonsnapshot/value(forkey:type:))*
---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/environmentvariablesprovider/fetchvalue(forkey:type:)"
framework: "swift-configuration/Configuration"
---

# fetchValue(forKey:type:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Fetches the current value for the specified configuration key.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func fetchValue(forKey key: AbsoluteConfigKey, type: ConfigType) async throws -> LookupResult
```

## Return Value

The lookup result that contains the current value and encoded key.

## Discussion

This method provides asynchronous access and should contact the authoritative data source to retrieve the latest value. Providers may cache the fetched values to make them available through [`value(forKey:type:)`](./value%28forkey,type%29.md).

Use this method when you need to ensure you have the most up-to-date value, especially for remote or frequently changing data sources.

> **Throws**: Provider-specific errors, network errors, or type conversion errors.

## Parameters

- `key`: The configuration key to fetch.
- `type`: The expected configuration value type.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/environmentvariablesprovider/fetchvalue(forkey:type:))*
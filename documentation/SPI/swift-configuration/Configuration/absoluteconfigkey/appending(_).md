---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/absoluteconfigkey/appending(_:)"
framework: "swift-configuration/Configuration"
---

# appending(_:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Returns a new absolute configuration key by appending the given relative key.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func appending(_ relative: ConfigKey) -> AbsoluteConfigKey
```

## Return Value

A new absolute configuration key that includes the relative key at the end.

## Parameters

- `relative`: The relative configuration key to append to this key.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/absoluteconfigkey/appending(_:))*
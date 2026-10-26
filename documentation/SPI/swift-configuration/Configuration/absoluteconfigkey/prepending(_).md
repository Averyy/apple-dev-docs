---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/absoluteconfigkey/prepending(_:)"
framework: "swift-configuration/Configuration"
---

# prepending(_:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Returns a new absolute configuration key by prepending the given relative key.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func prepending(_ prefix: ConfigKey) -> AbsoluteConfigKey
```

#### Return Value

A new absolute configuration key that includes the prefix at the beginning.

## Parameters

- `prefix`: The relative configuration key to prepend to this key.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/absoluteconfigkey/prepending(_:))*
---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/inmemoryprovider/mapkeys(_:)"
framework: "swift-configuration/Configuration"
---

# mapKeys(_:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Creates a new configuration provider where each key is rewritten by the given closure.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func mapKeys(_ transform: @escaping @Sendable (AbsoluteConfigKey) -> AbsoluteConfigKey) -> KeyMappingProvider<Self>
```

#### Return Value

A provider which maps keys using the provided transformation function.

## Parameters

- `transform`: The closure applied to each key before a lookup.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/inmemoryprovider/mapkeys(_:))*
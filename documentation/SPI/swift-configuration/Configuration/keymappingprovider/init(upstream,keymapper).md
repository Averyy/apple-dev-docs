---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/keymappingprovider/init(upstream:keymapper:)"
framework: "swift-configuration/Configuration"
---

# init(upstream:keyMapper:)

**Framework**: swift-configuration/Configuration  
**Kind**: init  
**Role**: Initializer

Creates a new provider.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(upstream: Upstream, keyMapper mapKey: @escaping @Sendable (AbsoluteConfigKey) -> AbsoluteConfigKey)
```

## Parameters

- `upstream`: The upstream provider to delegate to after mapping.
- `mapKey`: A closure to remap configuration keys.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/keymappingprovider/init(upstream:keymapper:))*
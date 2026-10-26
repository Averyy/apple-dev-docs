---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/init(provider:accessreporter:)"
framework: "swift-configuration/Configuration"
---

# init(provider:accessReporter:)

**Framework**: swift-configuration/Configuration  
**Kind**: init  
**Role**: Initializer

Creates a config reader with a single provider.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(provider: some ConfigProvider, accessReporter: (any AccessReporter)? = nil)
```

## Parameters

- `provider`: The configuration provider.
- `accessReporter`: The reporter for configuration access events.

## See Also

### Creating config readers
- [init(providers: [any ConfigProvider], accessReporter: (any AccessReporter)?)](./init%28providers,accessreporter%29.md)
  Creates a config reader with multiple providers.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/init(provider:accessreporter:))*
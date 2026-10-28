---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/init(providers:accessreporter:)"
framework: "swift-configuration/Configuration"
---

# init(providers:accessReporter:)

**Framework**: swift-configuration/Configuration  
**Kind**: init  
**Role**: Initializer

Creates a config reader with multiple providers.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(providers: [any ConfigProvider], accessReporter: (any AccessReporter)? = nil)
```

## Discussion

> **Precondition**: `providers` must not be empty.

## Parameters

- `providers`: The configuration providers, queried in order until a value is found.
- `accessReporter`: The reporter for configuration access events.

## See Also

### Creating config readers
- [init(provider: some ConfigProvider, accessReporter: (any AccessReporter)?)](./init%28provider,accessreporter%29.md)
  Creates a config reader with a single provider.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/init(providers:accessreporter:))*
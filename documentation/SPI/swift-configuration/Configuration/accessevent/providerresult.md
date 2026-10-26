---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/accessevent/providerresult"
framework: "swift-configuration/Configuration"
---

# AccessEvent.ProviderResult

**Framework**: swift-configuration/Configuration  
**Kind**: struct  
**Role**: Structure

The result of a configuration lookup from a specific provider.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct ProviderResult
```

#### Overview

Contains the provider’s name and the outcome of querying that provider, which can be either a successful lookup result or an error.

## Topics

### Creating provider results
- [init(providerName: String, result: Result<LookupResult, any Error>)](./providerresult/init%28providername,result%29.md)
  Creates a provider result.
### Inspecting provider results
- [var result: Result<LookupResult, any Error>](./providerresult/result.md)
  The outcome of the configuration lookup operation.
- [var providerName: String](./providerresult/providername.md)
  The name of the configuration provider that processes the lookup.

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Creating an access event
- [init(metadata: AccessEvent.Metadata, providerResults: [AccessEvent.ProviderResult], conversionError: (any Error)?, result: Result<ConfigValue?, any Error>)](./init%28metadata,providerresults,conversionerror,result%29.md)
  Creates a configuration access event.
- [AccessEvent.Metadata](./metadata-swift.struct.md)
  Metadata describing the configuration access operation.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/accessevent/providerresult)*
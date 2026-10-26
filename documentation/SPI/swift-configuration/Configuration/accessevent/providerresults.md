---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/accessevent/providerresults"
framework: "swift-configuration/Configuration"
---

# providerResults

**Framework**: swift-configuration/Configuration  
**Kind**: property  
**Role**: Instance Property

The results from each configuration provider queried.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var providerResults: [AccessEvent.ProviderResult]
```

## See Also

### Inspecting an access event
- [var result: Result<ConfigValue?, any Error>](./result.md)
  The final outcome of the configuration access operation.
- [var conversionError: (any Error)?](./conversionerror.md)
  An error that occurred when converting the raw config value into another type, for example `RawRepresentable`.
- [var metadata: AccessEvent.Metadata](./metadata-swift.property.md)
  Metadata that describes the configuration access operation.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/accessevent/providerresults)*
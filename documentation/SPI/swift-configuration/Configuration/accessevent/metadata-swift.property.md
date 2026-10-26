---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/accessevent/metadata-swift.property"
framework: "swift-configuration/Configuration"
---

# metadata

**Framework**: swift-configuration/Configuration  
**Kind**: property  
**Role**: Instance Property

Metadata that describes the configuration access operation.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var metadata: AccessEvent.Metadata
```

## See Also

### Inspecting an access event
- [var result: Result<ConfigValue?, any Error>](./result.md)
  The final outcome of the configuration access operation.
- [var conversionError: (any Error)?](./conversionerror.md)
  An error that occurred when converting the raw config value into another type, for example `RawRepresentable`.
- [var providerResults: [AccessEvent.ProviderResult]](./providerresults.md)
  The results from each configuration provider queried.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/accessevent/metadata-swift.property)*
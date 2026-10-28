---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/accessevent/result"
framework: "swift-configuration/Configuration"
---

# result

**Framework**: swift-configuration/Configuration  
**Kind**: property  
**Role**: Instance Property

The final outcome of the configuration access operation.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var result: Result<ConfigValue?, any Error>
```

## Discussion

> **Note**: Might contain `success` even if a [`conversionError`](./conversionerror.md) occurred, which non-throwing config reader methods use.

## See Also

### Inspecting an access event
- [var conversionError: (any Error)?](./conversionerror.md)
  An error that occurred when converting the raw config value into another type, for example `RawRepresentable`.
- [var metadata: AccessEvent.Metadata](./metadata-swift.property.md)
  Metadata that describes the configuration access operation.
- [var providerResults: [AccessEvent.ProviderResult]](./providerresults.md)
  The results from each configuration provider queried.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/accessevent/result)*
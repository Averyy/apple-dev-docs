---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/accessevent/init(metadata:providerresults:conversionerror:result:)"
framework: "swift-configuration/Configuration"
---

# init(metadata:providerResults:conversionError:result:)

**Framework**: swift-configuration/Configuration  
**Kind**: init  
**Role**: Initializer

Creates a configuration access event.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(metadata: AccessEvent.Metadata, providerResults: [AccessEvent.ProviderResult], conversionError: (any Error)? = nil, result: Result<ConfigValue?, any Error>)
```

## Parameters

- `metadata`: Metadata describing the access operation.
- `providerResults`: The results from each provider queried.
- `conversionError`: An error that occurred when converting the raw config value into another type, for example `RawRepresentable`.
- `result`: The final outcome of the access operation.

## See Also

### Creating an access event
- [AccessEvent.Metadata](./metadata-swift.struct.md)
  Metadata describing the configuration access operation.
- [AccessEvent.ProviderResult](./providerresult.md)
  The result of a configuration lookup from a specific provider.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/accessevent/init(metadata:providerresults:conversionerror:result:))*
# NWParametersBuilder

**Framework**: Network  
**Kind**: struct

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
struct NWParametersBuilder<Top, each P> where Top : NetworkProtocolOptions, repeat each P : NetworkProtocolOptions
```

## Topics

### Initializers
- [init(() -> (Top, repeat each P))](nwparametersbuilder/init(_:).md)
- [init(auto: () -> (Top, repeat each P))](nwparametersbuilder/init(auto:).md)
### Instance Methods
- [func wifiAware((inout WAParameters) -> Void) -> NWParametersBuilder<Top, repeat each P>](nwparametersbuilder/wifiaware(_:).md)
  Configure Wi-Fi Aware properties on an `NetworkConnection`
### Type Methods
- [static func parameters(() -> (Top, repeat each P)) -> NWParametersBuilder<Top, repeat each P>](nwparametersbuilder/parameters(_:).md)
- [static func parameters(initialParameters: NWParameters, () -> (Top, repeat each P)) -> NWParametersBuilder<Top, repeat each P>](nwparametersbuilder/parameters(initialparameters:_:).md)

## Relationships

### Conforms To
- [NWParametersProvider](nwparametersprovider.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparametersbuilder)*
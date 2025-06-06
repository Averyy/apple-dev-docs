# DecodableWithConfiguration

**Framework**: Foundation  
**Kind**: protocol

A protocol for types that support decoding when supplied with an additional configuration type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
protocol DecodableWithConfiguration
```

## Topics

### Decoding
- [init(from: any Decoder, configuration: Self.DecodingConfiguration) throws](decodablewithconfiguration/init(from:configuration:).md)
  Creates a new instance by retrieving the instance’s data from the specified decoder with help from the provided configuration.
### Supporting Types
- [associatedtype DecodingConfiguration](decodablewithconfiguration/decodingconfiguration.md)
  The configuration type that assists in decoding.

## Relationships

### Conforming Types
- [AttributeContainer](attributecontainer.md)
- [AttributedString](attributedstring.md)
- [Expression](expression.md)
- [Predicate](predicate.md)

## See Also

- [typealias CodableWithConfiguration](codablewithconfiguration.md)
  A type that can convert itself into and out of an external representation with the help of a configuration that handles encoding contained types.
- [struct CodableConfiguration](codableconfiguration.md)
  A property wrapper that makes a type codable, by supplying a configuration that provides additional information for serialization.
- [protocol DecodingConfigurationProviding](decodingconfigurationproviding.md)
  A protocol whose conformers provide a configuration instance to help decode types that don’t support encoding by themselves.
- [protocol EncodableWithConfiguration](encodablewithconfiguration.md)
  A protocol for types that support encoding when supplied with an additional configuration type.
- [protocol EncodingConfigurationProviding](encodingconfigurationproviding.md)
  A protocol whose conformers provide a configuration instance to help encode types that don’t support encoding by themselves.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/decodablewithconfiguration)*
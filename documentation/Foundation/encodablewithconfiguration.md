# EncodableWithConfiguration

**Framework**: Foundation  
**Kind**: protocol

A protocol for types that support encoding when supplied with an additional configuration type.

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
protocol EncodableWithConfiguration
```

## Topics

### Encoding
- [func encode(to: any Encoder, configuration: Self.EncodingConfiguration) throws](encodablewithconfiguration/encode(to:configuration:).md)
  Encodes the value into the specified encoder with help from the provided configuration.
### Supporting Types
- [associatedtype EncodingConfiguration](encodablewithconfiguration/encodingconfiguration.md)
  The type of the encoding configuration.

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
- [protocol DecodableWithConfiguration](decodablewithconfiguration.md)
  A protocol for types that support decoding when supplied with an additional configuration type.
- [protocol DecodingConfigurationProviding](decodingconfigurationproviding.md)
  A protocol whose conformers provide a configuration instance to help decode types that don’t support encoding by themselves.
- [protocol EncodingConfigurationProviding](encodingconfigurationproviding.md)
  A protocol whose conformers provide a configuration instance to help encode types that don’t support encoding by themselves.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/encodablewithconfiguration)*
# CodableConfiguration

**Framework**: Foundation  
**Kind**: struct

A property wrapper that makes a type codable, by supplying a configuration that provides additional information for serialization.

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
@propertyWrapper
struct CodableConfiguration<T, ConfigurationProvider> where T : DecodableWithConfiguration, T : EncodableWithConfiguration, ConfigurationProvider : DecodingConfigurationProviding, ConfigurationProvider : EncodingConfigurationProviding, T.DecodingConfiguration == ConfigurationProvider.DecodingConfiguration, T.EncodingConfiguration == ConfigurationProvider.EncodingConfiguration
```

#### Overview

[`CodableConfiguration`](codableconfiguration.md) allows you to create [`Codable`](https://developer.apple.com/documentation/Swift/Codable) types whose members don’t all conform to [`Codable`](https://developer.apple.com/documentation/Swift/Codable). For types that can’t support encoding and decoding by themselves but could become encodable and decodable with some statically-defined information, use the `@CodableConfiguration` wrapper. This lets you assign a configuration provider — a type that conforms to both [`EncodingConfigurationProviding`](encodingconfigurationproviding.md) and [`DecodingConfigurationProviding`](decodingconfigurationproviding.md) — to supply this data.

Limiting the [`CodableConfiguration`](codableconfiguration.md) to statically-defined information protects clients from loading unexpected data, similar to the protection provided by [`NSSecureCoding`](nssecurecoding.md).

In the following example, the `Message` type uses `@CodableConfiguration` for an [`AttributedString`](attributedstring.md) property called `content`. While [`AttributedString`](attributedstring.md) does conform to [`Codable`](https://developer.apple.com/documentation/Swift/Codable), it can only encode its known attributes — those declared by the platform SDK — as part of this conformance. By adding a [`CodableConfiguration`](codableconfiguration.md) for the custom `MyAttributes` type, `Message` uses [`encode(to:configuration:)`](encodablewithconfiguration/encode(to:configuration:).md) when encoding `content`, which preserves the custom attributes.

```swift
struct Message: Codable {
    let date: Date
    let sender: Person
    @CodableConfiguration(from: MyAttributes.self) var content = AttributedString()
}
```

## Topics

### Creating a Codable Configuration
- [init(wrappedValue: T)](codableconfiguration/init(wrappedvalue:).md)
  Creates a codable configuration wrapper for the given value.
- [init(wrappedValue: T, from: ConfigurationProvider.Type)](codableconfiguration/init(wrappedvalue:from:)-46oo6.md)
  Creates a codable configuration wrapper for the given value, using the given configuration provider type.
- [init(wrappedValue: T, from: KeyPath<AttributeScopes, ConfigurationProvider.Type>)](codableconfiguration/init(wrappedvalue:from:)-8mkxk.md)
  Creates a codable configuration wrapper for the given value, using given configuration provider type identified by key path.
### Accessing the Wrapped Value
- [var wrappedValue: T](codableconfiguration/wrappedvalue.md)
  The underlying value to make codable, using data from the configuration provider.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [typealias CodableWithConfiguration](codablewithconfiguration.md)
  A type that can convert itself into and out of an external representation with the help of a configuration that handles encoding contained types.
- [protocol DecodableWithConfiguration](decodablewithconfiguration.md)
  A protocol for types that support decoding when supplied with an additional configuration type.
- [protocol DecodingConfigurationProviding](decodingconfigurationproviding.md)
  A protocol whose conformers provide a configuration instance to help decode types that don’t support encoding by themselves.
- [protocol EncodableWithConfiguration](encodablewithconfiguration.md)
  A protocol for types that support encoding when supplied with an additional configuration type.
- [protocol EncodingConfigurationProviding](encodingconfigurationproviding.md)
  A protocol whose conformers provide a configuration instance to help encode types that don’t support encoding by themselves.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/codableconfiguration)*
# CodableWithConfiguration

**Framework**: Foundation  
**Kind**: typealias

A type that can convert itself into and out of an external representation with the help of a configuration that handles encoding contained types.

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
typealias CodableWithConfiguration = DecodableWithConfiguration & EncodableWithConfiguration
```

#### Discussion

[`CodableWithConfiguration`](codablewithconfiguration.md) is a type alias for the [`EncodableWithConfiguration`](encodablewithconfiguration.md) and [`DecodableWithConfiguration`](decodablewithconfiguration.md) protocols. Use this protocol to support codability in a type that can’t conform to [`Codable`](https://developer.apple.com/documentation/Swift/Codable) by itself, but can do so with additional statically-defined configuration provided by a [`CodableConfiguration`](codableconfiguration.md) instance.

[`AttributedString`](attributedstring.md) uses this approach to allow an instance to contain arbitrary attributes, including frameworks outside of Foundation or the platform SDK. It does this by including one or more [`AttributeScope`](attributescope.md) instances, a type that conforms to [`EncodingConfigurationProviding`](encodingconfigurationproviding.md) and [`DecodingConfigurationProviding`](decodingconfigurationproviding.md). An attribute scope like [`AttributeScopes.SwiftUIAttributes`](attributescopes/swiftuiattributes.md) defines attribute keys, and conforms to [`AttributeScope`](attributescope.md) to provide configuration instances that know the [`AttributedStringKey`](attributedstringkey.md) types and their associated [`Value`](attributedstringkey/value.md) types. With this type information, an [`AttributedString`](attributedstring.md) can encode all of its attributes, even from frameworks other than Foundation.

## See Also

- [struct CodableConfiguration](codableconfiguration.md)
  A property wrapper that makes a type codable, by supplying a configuration that provides additional information for serialization.
- [protocol DecodableWithConfiguration](decodablewithconfiguration.md)
  A protocol for types that support decoding when supplied with an additional configuration type.
- [protocol DecodingConfigurationProviding](decodingconfigurationproviding.md)
  A protocol whose conformers provide a configuration instance to help decode types that don’t support encoding by themselves.
- [protocol EncodableWithConfiguration](encodablewithconfiguration.md)
  A protocol for types that support encoding when supplied with an additional configuration type.
- [protocol EncodingConfigurationProviding](encodingconfigurationproviding.md)
  A protocol whose conformers provide a configuration instance to help encode types that don’t support encoding by themselves.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/codablewithconfiguration)*
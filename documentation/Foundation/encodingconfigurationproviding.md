# EncodingConfigurationProviding

**Framework**: Foundation  
**Kind**: protocol

A protocol whose conformers provide a configuration instance to help encode types that don’t support encoding by themselves.

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
protocol EncodingConfigurationProviding
```

## Topics

### Accessing the Configuration
- [static var encodingConfiguration: Self.EncodingConfiguration](encodingconfigurationproviding/encodingconfiguration-swift.type.property.md)
  The configuration instance that assists in encoding another type.
### Supporting Types
- [associatedtype EncodingConfiguration](encodingconfigurationproviding/encodingconfiguration-swift.associatedtype.md)

## Relationships

### Inherited By
- [AttributeScope](attributescope.md)
### Conforming Types
- [AttributeScopes.AccessibilityAttributes](attributescopes/accessibilityattributes.md)
- [AttributeScopes.AppKitAttributes](attributescopes/appkitattributes.md)
- [AttributeScopes.FoundationAttributes](attributescopes/foundationattributes.md)
- [AttributeScopes.FoundationAttributes.NumberFormatAttributes](attributescopes/foundationattributes/numberformatattributes.md)
- [AttributeScopes.SpeechAttributes](attributescopes/speechattributes.md)
- [AttributeScopes.SwiftUIAttributes](attributescopes/swiftuiattributes.md)
- [AttributeScopes.UIKitAttributes](attributescopes/uikitattributes.md)

## See Also

- [typealias CodableWithConfiguration](codablewithconfiguration.md)
  A type that can convert itself into and out of an external representation with the help of a configuration that handles encoding contained types.
- [struct CodableConfiguration](codableconfiguration.md)
  A property wrapper that makes a type codable, by supplying a configuration that provides additional information for serialization.
- [protocol DecodableWithConfiguration](decodablewithconfiguration.md)
  A protocol for types that support decoding when supplied with an additional configuration type.
- [protocol DecodingConfigurationProviding](decodingconfigurationproviding.md)
  A protocol whose conformers provide a configuration instance to help decode types that don’t support encoding by themselves.
- [protocol EncodableWithConfiguration](encodablewithconfiguration.md)
  A protocol for types that support encoding when supplied with an additional configuration type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/encodingconfigurationproviding)*
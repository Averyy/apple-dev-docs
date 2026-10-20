# NormalizationScaler.Transformer

**Framework**: Create ML Components  
**Kind**: struct  
**Role**: Structure

A transformer that scales the input using a normalization strategy.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
struct Transformer
```

Available when `Element` conforms to `BinaryFloatingPoint`, `Decodable`, and `Encodable`.

## Topics

### Creating a transformer
- [init(scale: Element)](./transformer/init%28scale%29.md)
  Creates a normalization scaling transformer.
### Getting the scale
- [var scale: Element](./transformer/scale.md)
  The normalization scale used to scale the input.
### Performing the transformation
- [func applied(to: Element, eventHandler: EventHandler?) -> Element](./transformer/applied%28to,eventhandler%29.md)
  Scales the input values using the calculation `input / scale`.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [Transformer](../transformer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/normalizationscaler/transformer)*
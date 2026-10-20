# StandardScaler.Transformer

**Framework**: Create ML Components  
**Kind**: struct  
**Role**: Structure

A transformer that standardizes the input by removing the mean and scaling to unit variance.

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
- [init(mean: Element, standardDeviation: Element)](./transformer/init%28mean,standarddeviation%29.md)
  Creates a standard scaling transformer.
### Getting the properties
- [var mean: Element](./transformer/mean.md)
  The mean used for offsetting.
- [var standardDeviation: Element](./transformer/standarddeviation.md)
  The standard deviation used for scaling.
### Performing the transformation
- [func applied(to: Element, eventHandler: EventHandler?) -> Element](./transformer/applied%28to,eventhandler%29.md)
  Scales the input values using the calculation `(input - mean) / standardDeviation`.

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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/standardscaler/transformer)*
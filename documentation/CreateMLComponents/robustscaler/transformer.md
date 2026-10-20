# RobustScaler.Transformer

**Framework**: Create ML Components  
**Kind**: struct  
**Role**: Structure

A transformer that scales the input using statistics that are robust to outliers.

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
- [init(median: Element, interQuartileRange: Element)](./transformer/init%28median,interquartilerange%29.md)
  Creates a robust scaling transformer.
### Getting the properties
- [var interQuartileRange: Element](./transformer/interquartilerange.md)
  The interquartile rage  used for scaling.
- [var median: Element](./transformer/median.md)
  The median used for offsetting.
### Performing the transformation
- [func applied(to: Element, eventHandler: EventHandler?) -> Element](./transformer/applied%28to,eventhandler%29.md)
  Scales the input values using the calculation `(input - median) / interQuartileRange`.

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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/robustscaler/transformer)*
# RobustScaler.Transformer

**Framework**: Create ML Components  
**Kind**: struct

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

## Topics

### Creating a transformer
- [init(median: Element, interQuartileRange: Element)](robustscaler/transformer/init(median:interquartilerange:).md)
  Creates a robust scaling transformer.
### Getting the properties
- [var interQuartileRange: Element](robustscaler/transformer/interquartilerange.md)
  The interquartile rage  used for scaling.
- [var median: Element](robustscaler/transformer/median.md)
  The median used for offsetting.
### Performing the transformation
- [func applied(to: Element, eventHandler: EventHandler?) -> Element](robustscaler/transformer/applied(to:eventhandler:).md)
  Scales the input values using the calculation `(input - median) / interQuartileRange`.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [Transformer](transformer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/robustscaler/transformer)*
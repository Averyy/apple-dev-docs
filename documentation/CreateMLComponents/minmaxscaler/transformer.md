# MinMaxScaler.Transformer

**Framework**: Create ML Components  
**Kind**: struct  
**Role**: Structure

A transformer that scales the input values so that they all lie in a closed range.

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
- [init(desiredRange: ClosedRange<Element>, fittedRange: ClosedRange<Element>)](./transformer/init%28desiredrange,fittedrange%29.md)
  Creates a minmax scaling transformer.
### Getting the properties
- [var desiredRange: ClosedRange<Element>](./transformer/desiredrange.md)
  The desired range of transformed values.
- [var fittedRange: ClosedRange<Element>](./transformer/fittedrange.md)
  The fitted range derived by the estimator when fitting.
### Performing the transformation
- [func applied(to: Element, eventHandler: EventHandler?) -> Element](./transformer/applied%28to,eventhandler%29.md)
  Scales the input values so that they all lie in the closed range `[minimum, maximum]`.

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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/minmaxscaler/transformer)*
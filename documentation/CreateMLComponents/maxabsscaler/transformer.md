# MaxAbsScaler.Transformer

**Framework**: Create ML Components  
**Kind**: struct  
**Role**: Structure

An transformer that scales the input values so that the maximum absolute value is 1.0.

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
- [init(maximumAbsoluteValue: Element)](./transformer/init%28maximumabsolutevalue%29.md)
  Creates a max abs scaling transformer.
### Getting the absolute value
- [var maximumAbsoluteValue: Element](./transformer/maximumabsolutevalue.md)
  The fitted maximum absolute value.
### Performing the transformation
- [func applied(to: Element, eventHandler: EventHandler?) -> Element](./transformer/applied%28to,eventhandler%29.md)
  Scales the input values by `1 / maximumAbsoluteValue`.

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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/maxabsscaler/transformer)*
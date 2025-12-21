# MaxAbsScaler.Transformer

**Framework**: Create ML Components  
**Kind**: struct

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

## Topics

### Creating a transformer
- [init(maximumAbsoluteValue: Element)](maxabsscaler/transformer/init(maximumabsolutevalue:).md)
  Creates a max abs scaling transformer.
### Getting the absolute value
- [var maximumAbsoluteValue: Element](maxabsscaler/transformer/maximumabsolutevalue.md)
  The fitted maximum absolute value.
### Performing the transformation
- [func applied(to: Element, eventHandler: EventHandler?) -> Element](maxabsscaler/transformer/applied(to:eventhandler:).md)
  Scales the input values by `1 / maximumAbsoluteValue`.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Transformer](transformer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/maxabsscaler/transformer)*
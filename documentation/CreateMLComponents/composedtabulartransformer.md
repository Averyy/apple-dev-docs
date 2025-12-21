# ComposedTabularTransformer

**Framework**: Create ML Components  
**Kind**: struct

A transformer that composes two tabular transformers by applying them one after the other.

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
struct ComposedTabularTransformer<Inner, Outer> where Inner : TabularTransformer, Outer : TabularTransformer
```

#### Overview

The result of this transformer is equivalent to invoking `outer(inner(x))` on an input `x`,

## Topics

### Creating the transformer
- [init(Inner, Outer)](composedtabulartransformer/init(_:_:).md)
  Creates a composed tabular transformer from two tabular transformers.
### Getting the properties
- [var inner: Inner](composedtabulartransformer/inner.md)
  The inner transformer.
- [var outer: Outer](composedtabulartransformer/outer.md)
  The outer transformer.
### Applying a transformation
- [func applied(to: DataFrame, eventHandler: EventHandler?) async throws -> DataFrame](composedtabulartransformer/applied(to:eventhandler:).md)
  Performs the composed transformation on a single input.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TabularTransformer](tabulartransformer.md)
- [Transformer](transformer.md)

## See Also

- [struct ComposedTransformer](composedtransformer.md)
  A transformer that composes two transformers by applying them one after the other.
- [struct ComposedTemporalTransformer](composedtemporaltransformer.md)
  A temporal transformer that composes two temporal transformers by applying them one after the other.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/composedtabulartransformer)*
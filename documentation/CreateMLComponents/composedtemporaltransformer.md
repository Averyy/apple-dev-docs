# ComposedTemporalTransformer

**Framework**: Create ML Components  
**Kind**: struct

A temporal transformer that composes two temporal transformers by applying them one after the other.

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
struct ComposedTemporalTransformer<Inner, Outer> where Inner : TemporalTransformer, Outer : TemporalTransformer, Inner.Output == Outer.Input
```

#### Overview

The inner transformer’s output must match the outer transformer input. The result of this transformer is equivalent to invoking `outer(inner(x))` on an input `x`,

## Topics

### Creating the transformer
- [init(Inner, Outer)](composedtemporaltransformer/init(_:_:).md)
  Creates a transformer composition from two temporal transformers.
### Getting the properties
- [var inner: Inner](composedtemporaltransformer/inner.md)
  The inner transformer.
- [var outer: Outer](composedtemporaltransformer/outer.md)
  The outer transformer.
### Applying a transformer
- [func applied<S>(to: S, eventHandler: EventHandler?) async throws -> ComposedTemporalTransformer<Inner, Outer>.OutputSequence](composedtemporaltransformer/applied(to:eventhandler:).md)
  Performs the composed transformation on an input sequence.
- [ComposedTemporalTransformer.Intermediate](composedtemporaltransformer/intermediate.md)
  The intermediate type.
- [ComposedTemporalTransformer.Input](composedtemporaltransformer/input.md)
  The input type.
- [ComposedTemporalTransformer.Output](composedtemporaltransformer/output.md)
  The output type.
- [ComposedTemporalTransformer.OutputSequence](composedtemporaltransformer/outputsequence.md)
  The output sequence type.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TemporalTransformer](temporaltransformer.md)

## See Also

- [struct ComposedTransformer](composedtransformer.md)
  A transformer that composes two transformers by applying them one after the other.
- [struct ComposedTabularTransformer](composedtabulartransformer.md)
  A transformer that composes two tabular transformers by applying them one after the other.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/composedtemporaltransformer)*
# ComposedTransformer

**Framework**: Create ML Components  
**Kind**: struct

A transformer that composes two transformers by applying them one after the other.

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
struct ComposedTransformer<Inner, Outer> where Inner : Transformer, Outer : Transformer, Inner.Output == Outer.Input
```

#### Overview

The inner transformer’s output must match the outer transformer input. The result of this transformer is equivalent to invoking `outer(inner(x))` on an input `x`,

## Topics

### Creating the transformer
- [init(Inner, Outer)](composedtransformer/init(_:_:).md)
  Creates a transformer composition from two transformers.
### Getting the properties
- [var inner: Inner](composedtransformer/inner.md)
  The inner transformer.
- [var outer: Outer](composedtransformer/outer.md)
  The outer transformer.
### Performing the transformation
- [func applied(to: ComposedTransformer<Inner, Outer>.Input, eventHandler: EventHandler?) async throws -> ComposedTransformer<Inner, Outer>.Output](composedtransformer/applied(to:eventhandler:).md)
  Performs the composed transformation on a single input.
- [ComposedTransformer.Input](composedtransformer/input.md)
  The input type.
- [ComposedTransformer.Intermediate](composedtransformer/intermediate.md)
  The intermediate type.
- [ComposedTransformer.Output](composedtransformer/output.md)
  The output type.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [Transformer](transformer.md)

## See Also

- [struct ComposedTemporalTransformer](composedtemporaltransformer.md)
  A temporal transformer that composes two temporal transformers by applying them one after the other.
- [struct ComposedTabularTransformer](composedtabulartransformer.md)
  A transformer that composes two tabular transformers by applying them one after the other.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/composedtransformer)*
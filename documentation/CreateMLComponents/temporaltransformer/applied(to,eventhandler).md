# applied(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Performs the transformation on an input sequence.

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
func applied<S>(to input: S, eventHandler: EventHandler?) async throws -> Self.OutputSequence where S : TemporalSequence, Self.Input == S.Feature
```

#### Return Value

An async sequence produced by applying the transformation to the input.

## Parameters

- `input`: The input temporal sequence.
- `eventHandler`: An event handler.

## Default Implementations

### TemporalTransformer Implementations
- [func applied<S>(to: S, eventHandler: EventHandler?) async throws -> [Self.OutputSequence]](./applied%28to,eventhandler%29-ax6t.md)
  Performs the transformation on a sequence of input sequences.
- [func applied<S, TS, Annotation>(to: S, eventHandler: EventHandler?) async throws -> [AnnotatedFeature<Self.OutputSequence, Annotation>]](./applied%28to,eventhandler%29-q6fk.md)
  Performs the transformation on a sequence of annotated input sequences.

## See Also

### Applying and adapting
- [func adaptedAsEstimator() -> TemporalTransformerToEstimatorAdaptor<Self>](./adaptedasestimator%28%29.md)
  Exposes this temporal transformer as a trivial temporal estimator.
- [func adaptedAsUpdatableEstimator() -> TemporalTransformerToUpdatableEstimatorAdaptor<Self>](./adaptedasupdatableestimator%28%29.md)
  Exposes this temporal transformer as a trivial temporal estimator.
- [associatedtype Input](./input.md)
  The input type.
- [associatedtype Output](./output.md)
  The output type.
- [associatedtype OutputSequence : TemporalSequence](./outputsequence.md)
  The output async sequence type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/temporaltransformer/applied(to:eventhandler:))*
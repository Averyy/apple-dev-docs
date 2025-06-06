# applied(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method  
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

## See Also

- [func adaptedAsEstimator() -> TemporalTransformerToEstimatorAdaptor<Self>](temporaltransformer/adaptedasestimator.md)
  Exposes this temporal transformer as a trivial temporal estimator.
- [func adaptedAsUpdatableEstimator() -> TemporalTransformerToUpdatableEstimatorAdaptor<Self>](temporaltransformer/adaptedasupdatableestimator.md)
  Exposes this temporal transformer as a trivial temporal estimator.
- [associatedtype Input](temporaltransformer/input.md)
  The input type.
- [associatedtype Output](temporaltransformer/output.md)
  The output type.
- [associatedtype OutputSequence : TemporalSequence](temporaltransformer/outputsequence.md)
  The output async sequence type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/temporaltransformer/applied(to:eventhandler:))*
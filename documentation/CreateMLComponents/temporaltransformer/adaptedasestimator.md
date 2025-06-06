# adaptedAsEstimator()

**Framework**: Create ML Components  
**Kind**: method

Exposes this temporal transformer as a trivial temporal estimator.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func adaptedAsEstimator() -> TemporalTransformerToEstimatorAdaptor<Self>
```

## See Also

- [func applied<S>(to: S, eventHandler: EventHandler?) async throws -> Self.OutputSequence](temporaltransformer/applied(to:eventhandler:).md)
  Performs the transformation on an input sequence.
- [func adaptedAsUpdatableEstimator() -> TemporalTransformerToUpdatableEstimatorAdaptor<Self>](temporaltransformer/adaptedasupdatableestimator.md)
  Exposes this temporal transformer as a trivial temporal estimator.
- [associatedtype Input](temporaltransformer/input.md)
  The input type.
- [associatedtype Output](temporaltransformer/output.md)
  The output type.
- [associatedtype OutputSequence : TemporalSequence](temporaltransformer/outputsequence.md)
  The output async sequence type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/temporaltransformer/adaptedasestimator())*
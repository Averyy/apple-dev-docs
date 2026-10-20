# adaptedAsUpdatableEstimator()

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Exposes this temporal transformer as a trivial temporal estimator.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0
- iPadOS 16.0+ - Deprecated in 18.0
- Mac Catalyst 16.0+ - Deprecated in 18.0
- macOS 13.0+ - Deprecated in 15.0
- tvOS 16.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```swift
func adaptedAsUpdatableEstimator() -> TemporalTransformerToUpdatableEstimatorAdaptor<Self>
```

## See Also

### Applying and adapting
- [func applied<S>(to: S, eventHandler: EventHandler?) async throws -> Self.OutputSequence](./applied%28to,eventhandler%29.md)
  Performs the transformation on an input sequence.
- [func adaptedAsEstimator() -> TemporalTransformerToEstimatorAdaptor<Self>](./adaptedasestimator%28%29.md)
  Exposes this temporal transformer as a trivial temporal estimator.
- [associatedtype Input](./input.md)
  The input type.
- [associatedtype Output](./output.md)
  The output type.
- [associatedtype OutputSequence : TemporalSequence](./outputsequence.md)
  The output async sequence type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/temporaltransformer/adaptedasupdatableestimator())*
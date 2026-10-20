# OutputSequence

**Framework**: Create ML Components  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

The output async sequence type.

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
associatedtype OutputSequence : TemporalSequence
```

## See Also

### Applying and adapting
- [func applied<S>(to: S, eventHandler: EventHandler?) async throws -> Self.OutputSequence](./applied%28to,eventhandler%29.md)
  Performs the transformation on an input sequence.
- [func adaptedAsEstimator() -> TemporalTransformerToEstimatorAdaptor<Self>](./adaptedasestimator%28%29.md)
  Exposes this temporal transformer as a trivial temporal estimator.
- [func adaptedAsUpdatableEstimator() -> TemporalTransformerToUpdatableEstimatorAdaptor<Self>](./adaptedasupdatableestimator%28%29.md)
  Exposes this temporal transformer as a trivial temporal estimator.
- [associatedtype Input](./input.md)
  The input type.
- [associatedtype Output](./output.md)
  The output type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/temporaltransformer/outputsequence)*
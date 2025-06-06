# Output

**Framework**: Create ML Components  
**Kind**: associatedtype  
**Required**: Yes

The output type.

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
associatedtype Output where Self.Output == Self.OutputSequence.Feature
```

## See Also

- [func applied<S>(to: S, eventHandler: EventHandler?) async throws -> Self.OutputSequence](temporaltransformer/applied(to:eventhandler:).md)
  Performs the transformation on an input sequence.
- [func adaptedAsEstimator() -> TemporalTransformerToEstimatorAdaptor<Self>](temporaltransformer/adaptedasestimator.md)
  Exposes this temporal transformer as a trivial temporal estimator.
- [func adaptedAsUpdatableEstimator() -> TemporalTransformerToUpdatableEstimatorAdaptor<Self>](temporaltransformer/adaptedasupdatableestimator.md)
  Exposes this temporal transformer as a trivial temporal estimator.
- [associatedtype Input](temporaltransformer/input.md)
  The input type.
- [associatedtype OutputSequence : TemporalSequence](temporaltransformer/outputsequence.md)
  The output async sequence type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/temporaltransformer/output)*
# fitted(to:)

**Framework**: Create ML Components  
**Kind**: method

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
func fitted<S>(to input: S) async throws -> Self.Transformer where S : Sequence, S.Element == Self.Transformer.Input
```

## See Also

- [func adaptedAsSupervised<Annotation>(annotationType: Annotation.Type) -> EstimatorToSupervisedAdaptor<Self, Annotation>](estimator/adaptedassupervised(annotationtype:).md)
  Exposes this estimator as a supervised estimator.
- [func adaptedAsTemporal() -> EstimatorToTemporalAdaptor<Self>](estimator/adaptedastemporal.md)
  Exposes this estimator as a temporal estimator.
- [func fitted<S>(to: S, eventHandler: EventHandler?) async throws -> Self.Transformer](estimator/fitted(to:eventhandler:).md)
  Fits a transformer to a sequence of examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/estimator/fitted(to:))*
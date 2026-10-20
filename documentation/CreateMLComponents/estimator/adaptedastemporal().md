# adaptedAsTemporal()

**Framework**: Create ML Components  
**Kind**: method

Exposes this estimator as a temporal estimator.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func adaptedAsTemporal() -> EstimatorToTemporalAdaptor<Self>
```

## See Also

- [func adaptedAsSupervised<Annotation>(annotationType: Annotation.Type) -> EstimatorToSupervisedAdaptor<Self, Annotation>](estimator/adaptedassupervised(annotationtype:).md)
  Exposes this estimator as a supervised estimator.
- [func fitted<S>(to: S, eventHandler: EventHandler?) async throws -> Self.Transformer](estimator/fitted(to:eventhandler:).md)
  Fits a transformer to a sequence of examples.
- [func fitted<S>(to: S) async throws -> Self.Transformer](estimator/fitted(to:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/estimator/adaptedastemporal())*
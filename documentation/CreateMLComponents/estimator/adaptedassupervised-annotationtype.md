# adaptedAsSupervised(annotationType:)

**Framework**: Create ML Components  
**Kind**: method

Exposes this estimator as a supervised estimator.

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
func adaptedAsSupervised<Annotation>(annotationType: Annotation.Type = Annotation.self) -> EstimatorToSupervisedAdaptor<Self, Annotation> where Annotation : Equatable
```

## See Also

- [func adaptedAsTemporal() -> EstimatorToTemporalAdaptor<Self>](estimator/adaptedastemporal.md)
  Exposes this estimator as a temporal estimator.
- [func fitted<S>(to: S, eventHandler: EventHandler?) async throws -> Self.Transformer](estimator/fitted(to:eventhandler:).md)
  Fits a transformer to a sequence of examples.
- [func fitted<S>(to: S) async throws -> Self.Transformer](estimator/fitted(to:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/estimator/adaptedassupervised(annotationtype:))*
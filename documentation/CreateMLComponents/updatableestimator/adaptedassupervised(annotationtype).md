# adaptedAsSupervised(annotationType:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

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
func adaptedAsSupervised<Annotation>(annotationType: Annotation.Type = Annotation.self) -> UpdatableEstimatorToSupervisedAdaptor<Self, Annotation> where Annotation : Equatable
```

## See Also

### Adapting
- [func adaptedAsTemporal() -> UpdatableEstimatorToTemporalAdaptor<Self>](./adaptedastemporal%28%29.md)
  Exposes this estimator as a temporal estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatableestimator/adaptedassupervised(annotationtype:))*
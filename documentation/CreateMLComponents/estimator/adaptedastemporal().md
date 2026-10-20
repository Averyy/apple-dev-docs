# adaptedAsTemporal()

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Exposes this estimator as a temporal estimator.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0
- iPadOS 16.0+ - Deprecated in 18.0
- Mac Catalyst 16.0+ - Deprecated in 18.0
- macOS 13.0+ - Deprecated in 15.0
- tvOS 16.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```swift
func adaptedAsTemporal() -> EstimatorToTemporalAdaptor<Self>
```

## See Also

### Fitting and adapting
- [func adaptedAsSupervised<Annotation>(annotationType: Annotation.Type) -> EstimatorToSupervisedAdaptor<Self, Annotation>](./adaptedassupervised%28annotationtype%29.md)
  Exposes this estimator as a supervised estimator.
- [func fitted<S>(to: S, eventHandler: EventHandler?) async throws -> Self.Transformer](./fitted%28to,eventhandler%29.md)
  Fits a transformer to a sequence of examples.
- [func fitted<S>(to: S) async throws -> Self.Transformer](./fitted%28to%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/estimator/adaptedastemporal())*
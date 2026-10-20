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
func adaptedAsSupervised<Annotation>(annotationType: Annotation.Type = Annotation.self) -> EstimatorToSupervisedAdaptor<Self, Annotation> where Annotation : Equatable
```

## See Also

### Fitting and adapting
- [func adaptedAsTemporal() -> EstimatorToTemporalAdaptor<Self>](./adaptedastemporal%28%29.md)
  Exposes this estimator as a temporal estimator.
- [func fitted<S>(to: S, eventHandler: EventHandler?) async throws -> Self.Transformer](./fitted%28to,eventhandler%29.md)
  Fits a transformer to a sequence of examples.
- [func fitted<S>(to: S) async throws -> Self.Transformer](./fitted%28to%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/estimator/adaptedassupervised(annotationtype:))*
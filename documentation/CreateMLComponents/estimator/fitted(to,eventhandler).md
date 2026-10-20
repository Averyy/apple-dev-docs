# fitted(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Fits a transformer to a sequence of examples.

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
func fitted<S>(to input: S, eventHandler: EventHandler?) async throws -> Self.Transformer where S : Sequence, S.Element == Self.Transformer.Input
```

#### Return Value

The fitted transformer.

## Parameters

- `input`: A sequence of examples.
- `eventHandler`: An event handler.

## See Also

### Fitting and adapting
- [func adaptedAsSupervised<Annotation>(annotationType: Annotation.Type) -> EstimatorToSupervisedAdaptor<Self, Annotation>](./adaptedassupervised%28annotationtype%29.md)
  Exposes this estimator as a supervised estimator.
- [func adaptedAsTemporal() -> EstimatorToTemporalAdaptor<Self>](./adaptedastemporal%28%29.md)
  Exposes this estimator as a temporal estimator.
- [func fitted<S>(to: S) async throws -> Self.Transformer](./fitted%28to%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/estimator/fitted(to:eventhandler:))*
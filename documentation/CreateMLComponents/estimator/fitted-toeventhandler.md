# fitted(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method  
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

- [func adaptedAsSupervised<Annotation>(annotationType: Annotation.Type) -> EstimatorToSupervisedAdaptor<Self, Annotation>](estimator/adaptedassupervised(annotationtype:).md)
  Exposes this estimator as a supervised estimator.
- [func adaptedAsTemporal() -> EstimatorToTemporalAdaptor<Self>](estimator/adaptedastemporal.md)
  Exposes this estimator as a temporal estimator.
- [func fitted<S>(to: S) async throws -> Self.Transformer](estimator/fitted(to:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/estimator/fitted(to:eventhandler:))*
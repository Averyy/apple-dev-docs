# update(_:with:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Updates a transformer with a new sequence of examples.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func update(_ transformer: inout AnnotatedFeatureProvider<Base, UnwrappedInput>.Transformer, with input: DataFrame, eventHandler: EventHandler? = nil) async throws
```

Available when `Base` conforms to `UpdatableSupervisedEstimator` and `Base.Transformer.Input` is `UnwrappedInput?`.

## Parameters

- `transformer`: A transformer to update.
- `input`: A sequence of examples.
- `eventHandler`: An event handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/annotatedfeatureprovider/update(_:with:eventhandler:))*
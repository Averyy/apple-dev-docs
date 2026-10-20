# InferenceFunction.Inputs

**Framework**: Core AI  
**Kind**: struct  
**Role**: Structure

A collection of named input values for an inference function.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct Inputs
```

## Mentions

- [Integrating on-device AI models in your app with Core AI](../integrating-on-device-ai-models-in-your-app-with-core-ai.md)

#### Overview

Build an `Inputs` collection by calling [`insert(_:for:)`](./inputs/insert%28_,for%29-2htrp.md) for each named input the function expects, then pass it to [`run(inputs:states:outputViews:)`](./run%28inputs,states,outputviews%29-14emi.md).

## Topics

### Creating inputs
- [init()](./inputs/init%28%29.md)
  Creates an empty set of inputs.
### Adding inputs
- [func insert(consuming NDArray.RawView, for: String)](./inputs/insert%28_,for%29-3eg32.md)
  Inserts a raw array view as the input with the specified name.
- [func insert(borrowing some InferenceValue.ViewRepresentable & ~Copyable, for: String)](./inputs/insert%28_,for%29-2htrp.md)
  Inserts a view of the value as the input with the specified name.
- [func insert<Element>(consuming NDArray.View<Element>, for: String)](./inputs/insert%28_,for%29-5o5oi.md)
  Inserts a typed array view as the input with the specified name.

## See Also

### Supporting types
- [InferenceFunction.Outputs](./outputs.md)
  The output values produced by running an inference function.
- [InferenceFunction.MutableViews](./mutableviews.md)
  A collection of `InferenceValue.MutableView`s which can be updated in-place by an `InferenceFunction`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunction/inputs)*
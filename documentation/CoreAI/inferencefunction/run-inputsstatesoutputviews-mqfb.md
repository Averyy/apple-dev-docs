# run(inputs:states:outputViews:)

**Framework**: Core AI  
**Kind**: method

Runs the function on the provided input arrays and returns the output values.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
func run(inputs: [String : NDArray], states: consuming InferenceFunction.MutableViews = MutableViews(), outputViews: consuming InferenceFunction.MutableViews = MutableViews()) async throws -> InferenceFunction.Outputs
```

#### Return Value

The outputs from the function.

#### Discussion

This is a convenience overload that accepts a dictionary of [`NDArray`](ndarray.md) values instead of an [`InferenceFunction.Inputs`](inferencefunction/inputs.md) collection.

Any [`NDArray`](ndarray.md) values in the returned outputs have a row-major contiguous layout.

## Parameters

- `inputs`: A dictionary that maps input names to their [`NDArray`](ndarray.md) values.
- `states`: The in-out arguments of the function, which the function reads and writes during inference. You must provide views for all states; omitting any state produces an error.
- `outputViews`: Pre-allocated output values that the function updates during inference. Outputs with a provided view are updated in-place and are not included in the returned [`InferenceFunction.Outputs`](inferencefunction/outputs.md). Outputs without a provided view produce new values in the returned [`InferenceFunction.Outputs`](inferencefunction/outputs.md).

## See Also

- [func run(inputs: borrowing InferenceFunction.Inputs, states: consuming InferenceFunction.MutableViews, outputViews: consuming InferenceFunction.MutableViews) async throws -> InferenceFunction.Outputs](inferencefunction/run(inputs:states:outputviews:)-14emi.md)
  Runs the function on the provided input values and returns the output values.
- [func encode(inputs: [String : InferenceFunction.AsyncValue], states: consuming InferenceFunction.AsyncMutableViews, outputViews: consuming InferenceFunction.AsyncMutableViews, to: ComputeStream) throws -> [String : InferenceFunction.AsyncValue]](inferencefunction/encode(inputs:states:outputviews:to:).md)
  Encodes the inference onto the provided compute stream, returning async values for the outputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunction/run(inputs:states:outputviews:)-mqfb)*
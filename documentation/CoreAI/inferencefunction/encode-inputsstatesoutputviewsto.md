# encode(inputs:states:outputViews:to:)

**Framework**: Core AI  
**Kind**: method

Encodes the inference onto the provided compute stream, returning async values for the outputs.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
func encode(inputs: [String : InferenceFunction.AsyncValue], states: consuming InferenceFunction.AsyncMutableViews = AsyncMutableViews(), outputViews: consuming InferenceFunction.AsyncMutableViews = AsyncMutableViews(), to stream: ComputeStream) throws -> [String : InferenceFunction.AsyncValue]
```

#### Return Value

A dictionary mapping output name to an [`InferenceFunction.AsyncValue`](inferencefunction/asyncvalue.md) for each output not included in `outputViews`.

#### Discussion

When this method returns, the compute may still be running on `stream`. You can pass the returned async values as inputs to subsequent `encode` calls to build a pipeline of inferences without waiting for intermediate results, or await them to retrieve the final compute outputs on the CPU.

```swift
let computeStream = ComputeStream()
let pipelineFunctionOne: InferenceFunction = ...
let pipelineFunctionTwo: InferenceFunction = ...
let initialInput: NDArray = ...

// Run stage one of pipeline and get async value output.
let asyncInput = InferenceFunction.AsyncValue(initialInput)
let functionOneOutputs = try pipelineFunctionOne.encode(inputs: ["input": asyncInput], to: computeStream)
guard let functionOneOutput = functionOneOutputs["output"] else {
    // Handle unexpected missing output
    return
}

// Feed output from function one as an input to function two.
// Note that function one may be running the actual compute asynchronously while function two
// encodes its inference.
let functionTwoOutputs = try pipelineFunctionTwo.encode(inputs: ["input": functionOneOutput], to: computeStream)
guard let functionTwoOutput = functionTwoOutputs["output"] else {
    // Handle unexpected missing output
    return
}

// Now both inferences have been encoded
guard let finalNDArray = try await functionTwoOutput.ndArray else {
    // Handle case where output is not an NDArray
    return
}
```

## Parameters

- `inputs`: The input values.
- `states`: The `inout` arguments that the function reads and writes during inference. Note that views for states are not optional. Omitting a view for any state results in an error.
- `outputViews`: A collection of pre-allocated output values that the inference updates during execution. The returned dictionary doesn’t contain [`InferenceFunction`](inferencefunction.md) outputs for which you provide a view, because the inference updates the mutable view in place. When you don’t provide a view, the returned dictionary includes a new async output value.
- `stream`: The compute stream that receives the encoded inference.

## See Also

- [func run(inputs: [String : NDArray], states: consuming InferenceFunction.MutableViews, outputViews: consuming InferenceFunction.MutableViews) async throws -> InferenceFunction.Outputs](inferencefunction/run(inputs:states:outputviews:)-mqfb.md)
  Runs the function on the provided input arrays and returns the output values.
- [func run(inputs: borrowing InferenceFunction.Inputs, states: consuming InferenceFunction.MutableViews, outputViews: consuming InferenceFunction.MutableViews) async throws -> InferenceFunction.Outputs](inferencefunction/run(inputs:states:outputviews:)-14emi.md)
  Runs the function on the provided input values and returns the output values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunction/encode(inputs:states:outputviews:to:))*
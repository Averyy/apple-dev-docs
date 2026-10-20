# evaluate(inputs:outputs:)

**Framework**: Core ML  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Evaluates the custom layer with the given inputs.

**Availability**:
- iOS 11.2+
- iPadOS 11.2+
- Mac Catalyst 13.1+
- macOS 10.13.2+
- tvOS 11.2+
- visionOS 1.0+
- watchOS 4.2+

## Declaration

```swift
func evaluate(inputs: [MLMultiArray], outputs: [MLMultiArray]) throws
```

```objc
- (BOOL) evaluateOnCPUWithInputs:(NSArray<MLMultiArray *> *) inputs outputs:(NSArray<MLMultiArray *> *) outputs error:(NSError **) error;
```

## Mentions

- [Creating and Integrating a Model with Custom Layers](../creating-and-integrating-a-model-with-custom-layers.md)

#### Discussion

Implement this method to evaluate the inputs using your layer’s custom behavior and to populate the output arrays. It will be called for each evaluation of your model performed on the CPU.

The memory for both input and output arrays is preallocated; don’t copy or move it. The inputs and outputs will have the shapes of the most recent call to [`outputShapes(forInputShapes:)`](./outputshapes%28forinputshapes%29.md). Don’t modify the input values.

Investigate [vecLib](../../Accelerate/veclib.md) for methods that could optimize your implementation significantly.

## Parameters

- `inputs`: The array of inputs to be evaluated.
- `outputs`: The array of outputs to be populated by evaluating the given inputs.

## See Also

### Evaluating a layer
- [func encode(commandBuffer: any MTLCommandBuffer, inputs: [any MTLTexture], outputs: [any MTLTexture]) throws](./encode%28commandbuffer,inputs,outputs%29.md)
  Encodes GPU commands to evaluate the custom layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlcustomlayer/evaluate(inputs:outputs:))*
# newMachineLearningPipelineStateWithDescriptor:error:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Creates a new ML pipeline state with descriptor.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (id<MTL4MachineLearningPipelineState>) newMachineLearningPipelineStateWithDescriptor:(MTL4MachineLearningPipelineDescriptor *) descriptor error:(NSError **) error;
```

## Return Value

A machine learning pipeline state if operation is successful, otherwise `nil`.

## Parameters

- `descriptor`: A machine learning pipeline state descriptor to use for creating the new pipeline state.
- `error`: An optional parameter into which Metal stores information in case of an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4compiler/newmachinelearningpipelinestatewithdescriptor:error:)*
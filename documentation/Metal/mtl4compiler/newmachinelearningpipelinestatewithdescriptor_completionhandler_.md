# newMachineLearningPipelineStateWithDescriptor:completionHandler:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Creates a new machine learning pipeline state asynchronously.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (id<MTL4CompilerTask>) newMachineLearningPipelineStateWithDescriptor:(MTL4MachineLearningPipelineDescriptor *) descriptor completionHandler:(MTL4NewMachineLearningPipelineStateCompletionHandler) completionHandler;
```

## Return Value

A compiler task representing the asynchronous compilation task.

## Parameters

- `descriptor`: A machine learning pipeline state descriptor to use for creating the new pipeline state.
- `completionHandler`: A block Metal calls when it finishes the build task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4compiler/newmachinelearningpipelinestatewithdescriptor:completionhandler:)*
# newComputePipelineStateWithDescriptor:compilerTaskOptions:completionHandler:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Creates a new compute pipeline state asynchronously.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (id<MTL4CompilerTask>) newComputePipelineStateWithDescriptor:(MTL4ComputePipelineDescriptor *) descriptor compilerTaskOptions:(MTL4CompilerTaskOptions *) compilerTaskOptions completionHandler:(MTLNewComputePipelineStateCompletionHandler) completionHandler;
```

#### Return Value

A compiler task representing the asynchronous compilation task.

## Parameters

- `descriptor`: A compute pipeline state descriptor, describing the compute pipeline to create.
- `compilerTaskOptions`: A descriptor of the compilation itself, providing parameters that influence execution of the compilation process.
- `completionHandler`: A block Metal calls when it finishes the build task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4compiler/newcomputepipelinestatewithdescriptor:compilertaskoptions:completionhandler:)*
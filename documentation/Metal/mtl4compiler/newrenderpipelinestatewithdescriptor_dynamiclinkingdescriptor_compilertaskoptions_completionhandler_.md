# newRenderPipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:completionHandler:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Creates a new render pipeline state asynchronously.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (id<MTL4CompilerTask>) newRenderPipelineStateWithDescriptor:(MTL4PipelineDescriptor *) descriptor dynamicLinkingDescriptor:(MTL4RenderPipelineDynamicLinkingDescriptor *) dynamicLinkingDescriptor compilerTaskOptions:(MTL4CompilerTaskOptions *) compilerTaskOptions completionHandler:(MTLNewRenderPipelineStateCompletionHandler) completionHandler;
```

## Return Value

A compiler task representing the asynchronous compilation task.

## Discussion

Use this method to build any render pipeline type, including render, tile, and mesh render pipeline states. The type of the descriptor you pass indicates the pipeline type this method builds.

Passing in a compute pipeline descriptor to the `descriptor` parameter produces an error.

## Parameters

- `descriptor`: A render, tile, or mesh pipeline state descriptor that describes the pipeline to create.
- `dynamicLinkingDescriptor`: An optional parameter that provides additional configuration for linking the pipeline state object.
- `compilerTaskOptions`: A description of the compilation process itself, providing parameters that influence execution of the compilation process.
- `completionHandler`: A block Metal calls when it finishes the build task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4compiler/newrenderpipelinestatewithdescriptor:dynamiclinkingdescriptor:compilertaskoptions:completionhandler:)*
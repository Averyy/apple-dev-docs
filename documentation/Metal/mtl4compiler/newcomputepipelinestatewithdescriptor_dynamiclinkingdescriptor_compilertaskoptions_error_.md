# newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:compilerTaskOptions:error:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Creates a new compute pipeline state synchronously.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (id<MTLComputePipelineState>) newComputePipelineStateWithDescriptor:(MTL4ComputePipelineDescriptor *) descriptor dynamicLinkingDescriptor:(MTL4PipelineStageDynamicLinkingDescriptor *) dynamicLinkingDescriptor compilerTaskOptions:(MTL4CompilerTaskOptions *) compilerTaskOptions error:(NSError **) error;
```

#### Return Value

A new compute pipeline state object upon success, `nil` otherwise.

## Parameters

- `descriptor`: A compute pipeline state descriptor describing the pipeline this compiler creates.
- `dynamicLinkingDescriptor`: An optional parameter that provides additional configuration for linking the pipeline state object.
- `compilerTaskOptions`: A description of the compilation process itself, providing parameters that influence execution of the compilation process.
- `error`: An optional parameter into which Metal stores information in case of an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4compiler/newcomputepipelinestatewithdescriptor:dynamiclinkingdescriptor:compilertaskoptions:error:)*
# makeComputePipelineState(function:completionHandler:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asynchronously creates a compute pipeline state with a function instance.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func makeComputePipelineState(function computeFunction: any MTLFunction, completionHandler: @escaping @Sendable ((any MTLComputePipelineState)?, (any Error)?) -> Void)
```

```swift
func makeComputePipelineState(function computeFunction: any MTLFunction) async throws -> any MTLComputePipelineState
```

```objc
- (void) newComputePipelineStateWithFunction:(id<MTLFunction>) computeFunction completionHandler:(MTLNewComputePipelineStateCompletionHandler) completionHandler;
```

#### Discussion

Use the compute pipeline state to configure a compute pass by calling the [`setComputePipelineState(_:)`](../mtlcomputecommandencoder/setcomputepipelinestate%28_%29.md) method of an [`MTLComputeCommandEncoder`](../mtlcomputecommandencoder.md) instance.

## Parameters

- `computeFunction`: An [`MTLFunction`](../mtlfunction.md) instance.
- `completionHandler`: A Swift closure or an Objective-C block the method calls when it finishes creating the compute pipeline state.

## See Also

### Creating compute pipeline states
- [func makeComputePipelineState(descriptor: MTLComputePipelineDescriptor, options: MTLPipelineOption, reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedComputePipelineReflection?>?) throws -> any MTLComputePipelineState](./makecomputepipelinestate%28descriptor,options,reflection%29.md)
  Synchronously creates a compute pipeline state and reflection information.
- [func makeComputePipelineState(descriptor: MTLComputePipelineDescriptor, options: MTLPipelineOption, completionHandler: ((any MTLComputePipelineState)?, MTLComputePipelineReflection?, (any Error)?) -> Void)](./makecomputepipelinestate%28descriptor,options,completionhandler%29.md)
  Asynchronously creates a compute pipeline state and reflection information.
- [func makeComputePipelineState(function: any MTLFunction) throws -> any MTLComputePipelineState](./makecomputepipelinestate%28function%29.md)
  Synchronously creates a compute pipeline state with a function instance.
- [func makeComputePipelineState(function: any MTLFunction, options: MTLPipelineOption, reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedComputePipelineReflection?>?) throws -> any MTLComputePipelineState](./makecomputepipelinestate%28function,options,reflection%29.md)
  Synchronously creates a compute pipeline state and reflection with a function instance.
- [func makeComputePipelineState(function: any MTLFunction, options: MTLPipelineOption, completionHandler: ((any MTLComputePipelineState)?, MTLComputePipelineReflection?, (any Error)?) -> Void)](./makecomputepipelinestate%28function,options,completionhandler%29.md)
  Asynchronously creates a compute pipeline state and reflection with a function instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makecomputepipelinestate(function:completionhandler:))*
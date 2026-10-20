# MTLNewComputePipelineStateWithReflectionCompletionHandler

**Framework**: Metal  
**Kind**: typealias  
**Role**: Type Alias

A completion handler signature a method calls when it finishes creating a compute pipeline and reflection information.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
typealias MTLNewComputePipelineStateWithReflectionCompletionHandler = ((any MTLComputePipelineState)?, MTLComputePipelineReflection?, (any Error)?) -> Void
```

```c
typedef void (^)(id<MTLComputePipelineState>, MTLComputePipelineReflection *, NSError *) MTLNewComputePipelineStateWithReflectionCompletionHandler;
```

## Parameters

- `computePipelineState`: An [`MTLComputePipelineState`](./mtlcomputepipelinestate.md) instance if the method completes successfully; otherwise `nil`.
- `reflection`: An [`MTLComputePipelineReflection`](./mtlcomputepipelinereflection.md) instance if the method completes successfully; otherwise `nil`.
- `error`: On return, if an error occurs, a pointer to an error information instance; otherwise `nil`.

## See Also

### Supporting types
- [typealias MTLNewRenderPipelineStateCompletionHandler](./mtlnewrenderpipelinestatecompletionhandler.md)
  A completion handler signature a method calls when it finishes creating a render pipeline.
- [typealias MTLNewRenderPipelineStateWithReflectionCompletionHandler](./mtlnewrenderpipelinestatewithreflectioncompletionhandler.md)
  A completion handler signature a method calls when it finishes creating a render pipeline and reflection information.
- [typealias MTLNewComputePipelineStateCompletionHandler](./mtlnewcomputepipelinestatecompletionhandler.md)
  A completion handler signature a method calls when it finishes creating a compute pipeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlnewcomputepipelinestatewithreflectioncompletionhandler)*
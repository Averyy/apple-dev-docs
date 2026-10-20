# MTLNewRenderPipelineStateWithReflectionCompletionHandler

**Framework**: Metal  
**Kind**: typealias  
**Role**: Type Alias

A completion handler signature a method calls when it finishes creating a render pipeline and reflection information.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
typealias MTLNewRenderPipelineStateWithReflectionCompletionHandler = ((any MTLRenderPipelineState)?, MTLRenderPipelineReflection?, (any Error)?) -> Void
```

```c
typedef void (^)(id<MTLRenderPipelineState>, MTLRenderPipelineReflection *, NSError *) MTLNewRenderPipelineStateWithReflectionCompletionHandler;
```

## Parameters

- `renderPipelineState`: An [`MTLRenderPipelineState`](./mtlrenderpipelinestate.md) instance if the method successfully compiles the library without any errors; otherwise `nil`.
- `reflection`: An [`MTLRenderPipelineReflection`](./mtlrenderpipelinereflection.md) instance if the method completes successfully; otherwise `nil`.
- `error`: If an error occurs, an error information instance; otherwise `nil`.

## See Also

### Supporting types
- [typealias MTLNewRenderPipelineStateCompletionHandler](./mtlnewrenderpipelinestatecompletionhandler.md)
  A completion handler signature a method calls when it finishes creating a render pipeline.
- [typealias MTLNewComputePipelineStateCompletionHandler](./mtlnewcomputepipelinestatecompletionhandler.md)
  A completion handler signature a method calls when it finishes creating a compute pipeline.
- [typealias MTLNewComputePipelineStateWithReflectionCompletionHandler](./mtlnewcomputepipelinestatewithreflectioncompletionhandler.md)
  A completion handler signature a method calls when it finishes creating a compute pipeline and reflection information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlnewrenderpipelinestatewithreflectioncompletionhandler)*
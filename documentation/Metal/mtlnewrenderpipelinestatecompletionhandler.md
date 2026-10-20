# MTLNewRenderPipelineStateCompletionHandler

**Framework**: Metal  
**Kind**: typealias  
**Role**: Type Alias

A completion handler signature a method calls when it finishes creating a render pipeline.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
typealias MTLNewRenderPipelineStateCompletionHandler = ((any MTLRenderPipelineState)?, (any Error)?) -> Void
```

```c
typedef void (^)(id<MTLRenderPipelineState>, NSError *) MTLNewRenderPipelineStateCompletionHandler;
```

## Parameters

- `renderPipelineState`: An [`MTLRenderPipelineState`](./mtlrenderpipelinestate.md) instance if the method completes successfully; otherwise `nil`.
- `error`: If an error occurs, an error information instance; otherwise `nil`.

## See Also

### Supporting types
- [typealias MTLNewRenderPipelineStateWithReflectionCompletionHandler](./mtlnewrenderpipelinestatewithreflectioncompletionhandler.md)
  A completion handler signature a method calls when it finishes creating a render pipeline and reflection information.
- [typealias MTLNewComputePipelineStateCompletionHandler](./mtlnewcomputepipelinestatecompletionhandler.md)
  A completion handler signature a method calls when it finishes creating a compute pipeline.
- [typealias MTLNewComputePipelineStateWithReflectionCompletionHandler](./mtlnewcomputepipelinestatewithreflectioncompletionhandler.md)
  A completion handler signature a method calls when it finishes creating a compute pipeline and reflection information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlnewrenderpipelinestatecompletionhandler)*
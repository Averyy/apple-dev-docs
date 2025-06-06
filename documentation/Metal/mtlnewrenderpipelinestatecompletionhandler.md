# MTLNewRenderPipelineStateCompletionHandler

**Framework**: Metal  
**Kind**: typealias

A completion handler signature a method calls when it finishes creating a render pipeline.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias MTLNewRenderPipelineStateCompletionHandler = ((any MTLRenderPipelineState)?, (any Error)?) -> Void
```

## Parameters

- `renderPipelineState`: An   instance if the method completes successfully; otherwise  .
- `error`: If an error occurs, an error information instance; otherwise  .

## See Also

- [typealias MTLNewRenderPipelineStateWithReflectionCompletionHandler](mtlnewrenderpipelinestatewithreflectioncompletionhandler.md)
  A completion handler signature a method calls when it finishes creating a render pipeline and reflection information.
- [typealias MTLNewComputePipelineStateCompletionHandler](mtlnewcomputepipelinestatecompletionhandler.md)
  A completion handler signature a method calls when it finishes creating a compute pipeline.
- [typealias MTLNewComputePipelineStateWithReflectionCompletionHandler](mtlnewcomputepipelinestatewithreflectioncompletionhandler.md)
  A completion handler signature a method calls when it finishes creating a compute pipeline and reflection information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlnewrenderpipelinestatecompletionhandler)*
# NSWritingToolsCoordinator.State.interactiveStreaming

**Framework**: AppKit  
**Kind**: case

A state that indicates Writing Tools is processing a request and incorporating changes interactively into your view.

**Availability**:
- macOS 15.2+

## Declaration

```swift
case interactiveStreaming
```

## Mentions

- [Adding Writing Tools support to a custom AppKit view](adding-writing-tools-support-to-a-custom-nsview.md)

#### Discussion

The coordinator transitions swiftly from the [`NSWritingToolsCoordinator.State.interactiveResting`](nswritingtoolscoordinator/state-swift.enum/interactiveresting.md) state to this state at the start of an operation. In this state, the coordinator submits the request for processing and delivers the results back to your view. When the coordinator finishes delivering the results, it transitions back to the [`NSWritingToolsCoordinator.State.interactiveResting`](nswritingtoolscoordinator/state-swift.enum/interactiveresting.md) state.

## See Also

- [NSWritingToolsCoordinator.State.inactive](nswritingtoolscoordinator/state-swift.enum/inactive.md)
  A state that indicates Writing Tools isn’t currently performing any work on your view’s content.
- [NSWritingToolsCoordinator.State.noninteractive](nswritingtoolscoordinator/state-swift.enum/noninteractive.md)
  A state that indicates Writing Tools is handling interactions in the system UI, instead of in your view.
- [NSWritingToolsCoordinator.State.interactiveResting](nswritingtoolscoordinator/state-swift.enum/interactiveresting.md)
  A state that indicates Writing Tools is in the resting state for an inline editing experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/state-swift.enum/interactivestreaming)*
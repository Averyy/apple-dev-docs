# NSWritingToolsCoordinator.State.inactive

**Framework**: AppKit  
**Kind**: case

A state that indicates Writing Tools isn’t currently performing any work on your view’s content.

**Availability**:
- macOS 15.2+

## Declaration

```swift
case inactive
```

## Mentions

- [Adding Writing Tools support to a custom AppKit view](adding-writing-tools-support-to-a-custom-nsview.md)

#### Discussion

The coordinator starts in the `inactive` state, and transitions immediately to the [`NSWritingToolsCoordinator.State.noninteractive`](nswritingtoolscoordinator/state-swift.enum/noninteractive.md) or [`NSWritingToolsCoordinator.State.interactiveResting`](nswritingtoolscoordinator/state-swift.enum/interactiveresting.md) state when someone chooses an option from the Writing Tools UI. After the coordinator finishes incorporating any changes for the current operation, it returns to the `inactive` state and waits for the person to choose a different option or dismiss the Writing Tools UI.

## See Also

- [NSWritingToolsCoordinator.State.noninteractive](nswritingtoolscoordinator/state-swift.enum/noninteractive.md)
  A state that indicates Writing Tools is handling interactions in the system UI, instead of in your view.
- [NSWritingToolsCoordinator.State.interactiveResting](nswritingtoolscoordinator/state-swift.enum/interactiveresting.md)
  A state that indicates Writing Tools is in the resting state for an inline editing experience.
- [NSWritingToolsCoordinator.State.interactiveStreaming](nswritingtoolscoordinator/state-swift.enum/interactivestreaming.md)
  A state that indicates Writing Tools is processing a request and incorporating changes interactively into your view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/state-swift.enum/inactive)*
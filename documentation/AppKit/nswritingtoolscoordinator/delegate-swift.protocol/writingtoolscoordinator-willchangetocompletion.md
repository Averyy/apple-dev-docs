# writingToolsCoordinator(_:willChangeTo:completion:)

**Framework**: AppKit  
**Kind**: method

Notifies your delegate of relevant state changes when Writing Tools is running in your view.

**Availability**:
- macOS 15.2+

## Declaration

```swift
optional func writingToolsCoordinator(_ writingToolsCoordinator: NSWritingToolsCoordinator, willChangeTo newState: NSWritingToolsCoordinator.State) async
```

## Mentions

- [Adding Writing Tools support to a custom AppKit view](adding-writing-tools-support-to-a-custom-nsview.md)

#### Discussion

Use state transitions to perform actions related to your view or text storage. When Writing Tools is active, it updates its state to indicate what task it’s currently performing. Writing Tools starts in the [`NSWritingToolsCoordinator.State.inactive`](nswritingtoolscoordinator/state-swift.enum/inactive.md) state and moves to other states as it presents UI and starts interacting with your view’s content. For example, it moves to the `NSWritingToolsCoordinator/State/interactiveUpdating` state when it’s making changes to your view’s text storage.

## Parameters

- `writingToolsCoordinator`: The coordinator object providing   information to your custom view.
- `completion`: A handler to execute when your delegate finishes processing   the change of state. The handler has no parameters or return value. You   must call this handler at some point during the implementation of your method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:willchangeto:completion:))*
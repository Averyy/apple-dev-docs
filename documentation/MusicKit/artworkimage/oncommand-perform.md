# onCommand(_:perform:)

**Framework**: MusicKit  
**Kind**: method

Adds an action to perform in response to the given selector.

**Availability**:
- macOS 10.15+

## Declaration

```swift
nonisolated
func onCommand(_ selector: Selector, perform action: (() -> Void)?) -> some View
```

#### Return Value

A view that triggers `action` when the `command` occurs.

#### Discussion

This view or one of the views it contains must be in focus in order for the action to trigger. Other actions for the same command on views  to the view in focus take priority, potentially overriding this action.

## Parameters

- `selector`: The selector to register for  .
- `action`: The action to perform. If   is  ,    keeps its association with this view but doesn’t trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/artworkimage/oncommand(_:perform:))*
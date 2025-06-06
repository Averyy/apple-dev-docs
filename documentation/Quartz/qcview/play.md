# play(_:)

**Framework**: Quartz  
**Kind**: method

Plays or pauses a composition in a view.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@IBAction
@MainActor func play(_ sender: Any!)
```

#### Discussion

This method starts rendering a composition if it is not already rendering, pauses a composition that is rendering, or resumes rendering for a composition whose rendering is paused. The method is invoked when the user clicks a button or issues a command from some other user interface element, such as a menu.

## Parameters

- `sender`: The object (such as a button or menu item) sending the message to play the composition. You need to connect the object in the interface to the action.

## See Also

- [func start(Any!)](qcview/start(_:).md)
  Starts rendering a composition in a view.
- [func stop(Any!)](qcview/stop(_:).md)
  Stops rendering a composition in a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcview/play(_:))*
# start(_:)

**Framework**: Quartz  
**Kind**: method

Starts rendering a composition in a view.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@IBAction
@MainActor func start(_ sender: Any!)
```

#### Discussion

The method is invoked when the user clicks a button or issues a command from some other user interface element, such as a menu. It is equivalent to the [`startRendering()`](qcview/startrendering().md) method.

## Parameters

- `sender`: The object (such as a button or menu item) sending the message to start rendering. You need to connect the object in the interface to the action.

## See Also

- [func play(Any!)](qcview/play(_:).md)
  Plays or pauses a composition in a view.
- [func stop(Any!)](qcview/stop(_:).md)
  Stops rendering a composition in a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcview/start(_:))*
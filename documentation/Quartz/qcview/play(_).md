# play(_:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Plays or pauses a composition in a view.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@IBAction
func play(_ sender: Any!)
```

```objc
- (void) play:(id) sender;
```

## Discussion

This method starts rendering a composition if it is not already rendering, pauses a composition that is rendering, or resumes rendering for a composition whose rendering is paused. The method is invoked when the user clicks a button or issues a command from some other user interface element, such as a menu.

## Parameters

- `sender`: The object (such as a button or menu item) sending the message to play the composition. You need to connect the object in the interface to the action.

## See Also

### Using Interface Builder
- [func start(Any!)](./start%28_%29.md)
  Starts rendering a composition in a view.
- [func stop(Any!)](./stop%28_%29.md)
  Stops rendering a composition in a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcview/play(_:))*
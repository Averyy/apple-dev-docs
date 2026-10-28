# stop(_:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Stops rendering a composition in a view.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@IBAction
func stop(_ sender: Any!)
```

```objc
- (void) stop:(id) sender;
```

## Discussion

The method is invoked when the user clicks a button or issues a command from some other user interface element, such as a menu. It is equivalent to the [`stopRendering()`](./stoprendering%28%29.md) method.

## Parameters

- `sender`: The object (such as a button or menu item) sending the message to stop rendering. You need to connect the object in the interface to the action.

## See Also

### Using Interface Builder
- [func play(Any!)](./play%28_%29.md)
  Plays or pauses a composition in a view.
- [func start(Any!)](./start%28_%29.md)
  Starts rendering a composition in a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcview/stop(_:))*
# viewWillAppear()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Called after the title bar accessory view controller’s view has been loaded into memory is about to be added to the view hierarchy in the window.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func viewWillAppear()
```

```objc
- (void) viewWillAppear;
```

## Discussion

This method is called when the accessory view is about to be added to the window’s view hierarchy or the window is about to become visible, such as coming to the front or becoming unhidden. If you override this method, you must call `super` in your implementation.

## See Also

### Responding to view events
- [func viewDidAppear()](./viewdidappear%28%29.md)
  Called when the title bar accessory view controller’s view is fully transitioned onto the screen.
- [func viewDidDisappear()](./viewdiddisappear%28%29.md)
  Called after the title bar accessory view controller’s view is removed from the window’s view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstitlebaraccessoryviewcontroller/viewwillappear())*
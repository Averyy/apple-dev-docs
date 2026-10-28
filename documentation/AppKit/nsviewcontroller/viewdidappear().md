# viewDidAppear()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Called when the view controller’s view is fully transitioned onto the screen.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func viewDidAppear()
```

```objc
- (void) viewDidAppear;
```

## Discussion

This method is called after the completion of any drawing and animations involved in the initial appearance of the view. You can override this method to perform tasks appropriate for that time, such as work that should not interfere with the presentation animation, or starting an animation that you want to begin after the view appears.

If you override this method, call this method on `super` at some point in your implementation in case a superclass also overrides this method.

The default implementation of this method does nothing.

## See Also

### Responding to View Events
- [func viewDidLoad()](./viewdidload%28%29.md)
  Called after the view controller’s view has been loaded into memory.
- [func loadViewIfNeeded()](./loadviewifneeded%28%29.md)
- [var isViewLoaded: Bool](./isviewloaded.md)
  A Boolean value indicating whether the view controller’s view is loaded into memory.
- [var viewIfLoaded: NSView?](./viewifloaded.md)
- [func viewWillAppear()](./viewwillappear%28%29.md)
  Called after the view controller’s view has been loaded into memory is about to be added to the view hierarchy in the window.
- [func viewWillDisappear()](./viewwilldisappear%28%29.md)
  Called when the view controller’s view is about to be removed from the view hierarchy in the window.
- [func viewDidDisappear()](./viewdiddisappear%28%29.md)
  Called after the view controller’s view is removed from the view hierarchy in a window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/viewdidappear())*
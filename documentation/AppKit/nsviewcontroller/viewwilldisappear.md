# viewWillDisappear()

**Framework**: AppKit  
**Kind**: method

Called when the view controller’s view is about to be removed from the view hierarchy in the window.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func viewWillDisappear()
```

#### Discussion

You can override this method to perform tasks that are to precede the disappearance of the view controller’s view, such as stopping a continuous animation that you started in response to the [`viewDidAppear()`](nsviewcontroller/viewdidappear().md) method call. This method is called when:

- The view is about to be removed from the view hierarchy of the window
- The view is about to be hidden or obscured, such as in the case of a view controller whose parent is a tab view controller and the user switched to another tab
- The window is being closed

If you override this method, call this method on `super` at some point in your implementation in case a superclass also overrides this method.

The default implementation of this method does nothing.

## See Also

- [func viewDidLoad()](nsviewcontroller/viewdidload.md)
  Called after the view controller’s view has been loaded into memory.
- [func loadViewIfNeeded()](nsviewcontroller/loadviewifneeded.md)
- [var isViewLoaded: Bool](nsviewcontroller/isviewloaded.md)
  A Boolean value indicating whether the view controller’s view is loaded into memory.
- [var viewIfLoaded: NSView?](nsviewcontroller/viewifloaded.md)
- [func viewWillAppear()](nsviewcontroller/viewwillappear.md)
  Called after the view controller’s view has been loaded into memory is about to be added to the view hierarchy in the window.
- [func viewDidAppear()](nsviewcontroller/viewdidappear.md)
  Called when the view controller’s view is fully transitioned onto the screen.
- [func viewDidDisappear()](nsviewcontroller/viewdiddisappear.md)
  Called after the view controller’s view is removed from the view hierarchy in a window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/viewwilldisappear())*
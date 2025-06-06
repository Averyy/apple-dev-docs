# viewDidAppear()

**Framework**: AppKit  
**Kind**: method

Called when the view controller’s view is fully transitioned onto the screen.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func viewDidAppear()
```

#### Discussion

This method is called after the completion of any drawing and animations involved in the initial appearance of the view. You can override this method to perform tasks appropriate for that time, such as work that should not interfere with the presentation animation, or starting an animation that you want to begin after the view appears.

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
- [func viewWillDisappear()](nsviewcontroller/viewwilldisappear.md)
  Called when the view controller’s view is about to be removed from the view hierarchy in the window.
- [func viewDidDisappear()](nsviewcontroller/viewdiddisappear.md)
  Called after the view controller’s view is removed from the view hierarchy in a window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/viewdidappear())*
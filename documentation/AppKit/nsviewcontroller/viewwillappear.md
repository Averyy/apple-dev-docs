# viewWillAppear()

**Framework**: AppKit  
**Kind**: method

Called after the view controller’s view has been loaded into memory is about to be added to the view hierarchy in the window.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func viewWillAppear()
```

#### Discussion

You can override this method to perform tasks prior to a view controller’s view getting added to view hierarchy, such as setting the view’s highlight color. This method is called when:

- The view is about to be added to the view hierarchy of the view controller
- The view controller’s window is about to become visible, such as coming to the front or becoming unhidden

If you override this method, call this method on `super` at some point in your implementation in case a superclass also overrides this method.

The default implementation of this method does nothing.

## See Also

- [func viewDidLoad()](nsviewcontroller/viewdidload.md)
  Called after the view controller’s view has been loaded into memory.
- [func loadViewIfNeeded()](nsviewcontroller/loadviewifneeded.md)
- [var isViewLoaded: Bool](nsviewcontroller/isviewloaded.md)
  A Boolean value indicating whether the view controller’s view is loaded into memory.
- [var viewIfLoaded: NSView?](nsviewcontroller/viewifloaded.md)
- [func viewDidAppear()](nsviewcontroller/viewdidappear.md)
  Called when the view controller’s view is fully transitioned onto the screen.
- [func viewWillDisappear()](nsviewcontroller/viewwilldisappear.md)
  Called when the view controller’s view is about to be removed from the view hierarchy in the window.
- [func viewDidDisappear()](nsviewcontroller/viewdiddisappear.md)
  Called after the view controller’s view is removed from the view hierarchy in a window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/viewwillappear())*
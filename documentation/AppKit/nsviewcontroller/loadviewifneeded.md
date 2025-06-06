# loadViewIfNeeded()

**Framework**: AppKit  
**Kind**: method

**Availability**:
- macOS 14.0+

## Declaration

```swift
@MainActor
func loadViewIfNeeded()
```

## See Also

- [func viewDidLoad()](nsviewcontroller/viewdidload.md)
  Called after the view controller’s view has been loaded into memory.
- [var isViewLoaded: Bool](nsviewcontroller/isviewloaded.md)
  A Boolean value indicating whether the view controller’s view is loaded into memory.
- [var viewIfLoaded: NSView?](nsviewcontroller/viewifloaded.md)
- [func viewWillAppear()](nsviewcontroller/viewwillappear.md)
  Called after the view controller’s view has been loaded into memory is about to be added to the view hierarchy in the window.
- [func viewDidAppear()](nsviewcontroller/viewdidappear.md)
  Called when the view controller’s view is fully transitioned onto the screen.
- [func viewWillDisappear()](nsviewcontroller/viewwilldisappear.md)
  Called when the view controller’s view is about to be removed from the view hierarchy in the window.
- [func viewDidDisappear()](nsviewcontroller/viewdiddisappear.md)
  Called after the view controller’s view is removed from the view hierarchy in a window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/loadviewifneeded())*
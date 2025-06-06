# viewDidLoad()

**Framework**: AppKit  
**Kind**: method

Called after the view controller’s view has been loaded into memory.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func viewDidLoad()
```

#### Discussion

You can override this method to perform tasks to immediately follow the setting of the [`view`](nsviewcontroller/view.md) property.

Typically, your override would perform one-time instantiation and initialization of the contents of the view controller’s view. If you override this method, call this method on `super` at some point in your implementation in case a superclass also overrides this method.

For a view controller originating in a nib file, this method is called immediately after the [`view`](nsviewcontroller/view.md) property is set. For a view controller created programmatically, this method is called immediately after the [`loadView()`](nsviewcontroller/loadview().md) method completes.

The default implementation of this method does nothing.

## See Also

- [func loadViewIfNeeded()](nsviewcontroller/loadviewifneeded.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/viewdidload())*
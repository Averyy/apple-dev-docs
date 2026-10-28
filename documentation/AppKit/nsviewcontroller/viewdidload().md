# viewDidLoad()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Called after the view controller’s view has been loaded into memory.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func viewDidLoad()
```

```objc
- (void) viewDidLoad;
```

## Discussion

You can override this method to perform tasks to immediately follow the setting of the [`view`](./view.md) property.

Typically, your override would perform one-time instantiation and initialization of the contents of the view controller’s view. If you override this method, call this method on `super` at some point in your implementation in case a superclass also overrides this method.

For a view controller originating in a nib file, this method is called immediately after the [`view`](./view.md) property is set. For a view controller created programmatically, this method is called immediately after the [`loadView()`](./loadview%28%29.md) method completes.

The default implementation of this method does nothing.

## See Also

### Responding to View Events
- [func loadViewIfNeeded()](./loadviewifneeded%28%29.md)
- [var isViewLoaded: Bool](./isviewloaded.md)
  A Boolean value indicating whether the view controller’s view is loaded into memory.
- [var viewIfLoaded: NSView?](./viewifloaded.md)
- [func viewWillAppear()](./viewwillappear%28%29.md)
  Called after the view controller’s view has been loaded into memory is about to be added to the view hierarchy in the window.
- [func viewDidAppear()](./viewdidappear%28%29.md)
  Called when the view controller’s view is fully transitioned onto the screen.
- [func viewWillDisappear()](./viewwilldisappear%28%29.md)
  Called when the view controller’s view is about to be removed from the view hierarchy in the window.
- [func viewDidDisappear()](./viewdiddisappear%28%29.md)
  Called after the view controller’s view is removed from the view hierarchy in a window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/viewdidload())*
# viewWillLayout()

**Framework**: AppKit  
**Kind**: method

Called just before the [`layout()`](nsview/layout().md) method of the view controller’s view is called.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func viewWillLayout()
```

#### Discussion

You can override this method to perform tasks to precede the layout of the view controller’s view, such as adjusting Auto Layout constraints. If you override this method, call this method on `super` at some point in your implementation in case a superclass also overrides this method.

The default implementation of this method does nothing.

## See Also

- [var preferredContentSize: NSSize](nsviewcontroller/preferredcontentsize.md)
  The desired size of the view controller’s view, in screen units.
- [func updateViewConstraints()](nsviewcontroller/updateviewconstraints.md)
  Called during Auto Layout constraint updating to enable the view controller to mediate the process.
- [func viewDidLayout()](nsviewcontroller/viewdidlayout.md)
  Called immediately after the [`layout()`](nsview/layout().md) method of the view controller’s view is called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/viewwilllayout())*
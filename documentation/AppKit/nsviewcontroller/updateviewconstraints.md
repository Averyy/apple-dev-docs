# updateViewConstraints()

**Framework**: AppKit  
**Kind**: method

Called during Auto Layout constraint updating to enable the view controller to mediate the process.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func updateViewConstraints()
```

#### Discussion

This method gets called, for example, when the user interacts with a view in a way that causes the layout to change. When called, the default implementation of this method in turn calls the [`updateConstraints()`](nsview/updateconstraints().md) method on the view controller’s view.

You can override this method to update custom view constraints, as an alternative to subclassing the view controller’s view and overriding its [`updateConstraints()`](nsview/updateconstraints().md) method.

If you override this method, you must call this method on `super` at some point in your implementation or call the [`updateConstraints()`](nsview/updateconstraints().md) method on the view controller’s view.

This method is called only for apps that link against macOS 10.10 or later.

## See Also

- [var preferredContentSize: NSSize](nsviewcontroller/preferredcontentsize.md)
  The desired size of the view controller’s view, in screen units.
- [func viewWillLayout()](nsviewcontroller/viewwilllayout.md)
  Called just before the [`layout()`](nsview/layout().md) method of the view controller’s view is called.
- [func viewDidLayout()](nsviewcontroller/viewdidlayout.md)
  Called immediately after the [`layout()`](nsview/layout().md) method of the view controller’s view is called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/updateviewconstraints())*
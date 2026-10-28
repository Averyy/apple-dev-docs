# updateViewConstraints()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Called during Auto Layout constraint updating to enable the view controller to mediate the process.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func updateViewConstraints()
```

```objc
- (void) updateViewConstraints;
```

## Discussion

This method gets called, for example, when the user interacts with a view in a way that causes the layout to change. When called, the default implementation of this method in turn calls the [`updateConstraints()`](../nsview/updateconstraints%28%29.md) method on the view controller’s view.

You can override this method to update custom view constraints, as an alternative to subclassing the view controller’s view and overriding its [`updateConstraints()`](../nsview/updateconstraints%28%29.md) method.

If you override this method, you must call this method on `super` at some point in your implementation or call the [`updateConstraints()`](../nsview/updateconstraints%28%29.md) method on the view controller’s view.

This method is called only for apps that link against macOS 10.10 or later.

This method supports automatic observation tracking. For more information, see [Updating views automatically with observation tracking in AppKit](../updating-views-automatically-with-observation-tracking-in-appkit.md).

## See Also

### Observing data in view controllers
- [func viewWillLayout()](./viewwilllayout%28%29.md)
  Called just before the [`layout()`](../nsview/layout%28%29.md) method of the view controller’s view is called.
- [func viewDidLayout()](./viewdidlayout%28%29.md)
  Called immediately after the [`layout()`](../nsview/layout%28%29.md) method of the view controller’s view is called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/updateviewconstraints())*
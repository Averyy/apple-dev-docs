# viewDidLayout()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Called immediately after the [`layout()`](../nsview/layout%28%29.md) method of the view controller’s view is called.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func viewDidLayout()
```

```objc
- (void) viewDidLayout;
```

#### Discussion

You can override this method to perform tasks to follow the completion of layout of the view controller’s view. If you override this method, call this method on `super` at some point in your implementation in case a superclass also overrides this method.

The default implementation of this method does nothing.

This method supports automatic observation tracking. For more information, see [Updating views automatically with observation tracking in AppKit](../updating-views-automatically-with-observation-tracking-in-appkit.md).

## See Also

### Observing data in view controllers
- [func viewWillLayout()](./viewwilllayout%28%29.md)
  Called just before the [`layout()`](../nsview/layout%28%29.md) method of the view controller’s view is called.
- [func updateViewConstraints()](./updateviewconstraints%28%29.md)
  Called during Auto Layout constraint updating to enable the view controller to mediate the process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/viewdidlayout())*
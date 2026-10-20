# removeFromParent()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes the called view controller from its parent view controller.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func removeFromParent()
```

```objc
- (void) removeFromParentViewController;
```

#### Discussion

Use this method to remove a child view controller from its parent view controller, unless you want to perform work during the removal. In that case, instead override the [`removeChild(at:)`](./removechild%28at%29.md) method to perform that work and call that method.

This is a convenience method that calls the [`removeChild(at:)`](./removechild%28at%29.md) method, automatically supplying the appropriate index value as an argument.

## See Also

### Managing Child View Controllers in a Custom Container
- [func addChild(NSViewController)](./addchild%28_%29.md)
  A convenience method for adding a child view controller at the end of the [`children`](./children.md) array.
- [var children: [NSViewController]](./children.md)
  An array of view controllers that are hierarchical children of the view controller.
- [func transition(from: NSViewController, to: NSViewController, options: NSViewController.TransitionOptions, completionHandler: (() -> Void)?)](./transition%28from,to,options,completionhandler%29.md)
  Performs a transition between two sibling child view controllers of the view controller.
- [func insertChild(NSViewController, at: Int)](./insertchild%28_,at%29.md)
  Inserts a specified child view controller into the [`children`](./children.md) array at a specified position.
- [func removeChild(at: Int)](./removechild%28at%29.md)
  Removes a specified child controller from the view controller.
- [func preferredContentSizeDidChange(for: NSViewController)](./preferredcontentsizedidchange%28for%29.md)
  Called when there is a change in value of the [`preferredContentSize`](./preferredcontentsize.md) property of a child view controller or a presented view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/removefromparent())*
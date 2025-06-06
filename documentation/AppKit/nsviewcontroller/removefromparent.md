# removeFromParent()

**Framework**: AppKit  
**Kind**: method

Removes the called view controller from its parent view controller.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func removeFromParent()
```

#### Discussion

Use this method to remove a child view controller from its parent view controller, unless you want to perform work during the removal. In that case, instead override the [`removeChild(at:)`](nsviewcontroller/removechild(at:).md) method to perform that work and call that method.

This is a convenience method that calls the [`removeChild(at:)`](nsviewcontroller/removechild(at:).md) method, automatically supplying the appropriate index value as an argument.

## See Also

- [func addChild(NSViewController)](nsviewcontroller/addchild(_:).md)
  A convenience method for adding a child view controller at the end of the [`children`](nsviewcontroller/children.md) array.
- [var children: [NSViewController]](nsviewcontroller/children.md)
  An array of view controllers that are hierarchical children of the view controller.
- [func transition(from: NSViewController, to: NSViewController, options: NSViewController.TransitionOptions, completionHandler: (() -> Void)?)](nsviewcontroller/transition(from:to:options:completionhandler:).md)
  Performs a transition between two sibling child view controllers of the view controller.
- [func insertChild(NSViewController, at: Int)](nsviewcontroller/insertchild(_:at:).md)
  Inserts a specified child view controller into the [`children`](nsviewcontroller/children.md) array at a specified position.
- [func removeChild(at: Int)](nsviewcontroller/removechild(at:).md)
  Removes a specified child controller from the view controller.
- [func preferredContentSizeDidChange(for: NSViewController)](nsviewcontroller/preferredcontentsizedidchange(for:).md)
  Called when there is a change in value of the [`preferredContentSize`](nsviewcontroller/preferredcontentsize.md) property of a child view controller or a presented view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/removefromparent())*
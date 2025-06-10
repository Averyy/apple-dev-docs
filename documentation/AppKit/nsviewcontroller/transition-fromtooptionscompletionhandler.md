# transition(from:to:options:completionHandler:)

**Framework**: AppKit  
**Kind**: method

Performs a transition between two sibling child view controllers of the view controller.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func transition(from fromViewController: NSViewController, to toViewController: NSViewController, options: NSViewController.TransitionOptions = []) async
```

#### Discussion

Use this method to transition between sibling child view controllers owned by a parent view controller (which is the receiver of this method).

This method adds the view in the `toViewController` view controller to the superview of the view in the `fromViewController` view controller. Likewise, this method removes the `fromViewController` view from the parent view controller’s view hierarchy at the appropriate time. It is important to allow this method to add and remove these views.

> **Note**:  The receiver of this method must be the parent view controller of the `fromViewController` and `toViewController` view controllers, or else this method raises an exception.

To create a parent/child relationship between view controllers, use the [`addChild(_:)`](nsviewcontroller/addchild(_:).md) method or the [`insertChild(_:at:)`](nsviewcontroller/insertchild(_:at:).md) method.

## Parameters

- `fromViewController`: A child view controller whose view is visible in the view controller’s view hierarchy.
- `toViewController`: A child view controller whose view is not in the view controller’s view hierarchy.
- `options`: A bitmask of options that specify how you want to perform the transition animation. For the options, see the   enumeration.
- `completion`: A block called immediately after the transition animation completes.

## See Also

- [func addChild(NSViewController)](nsviewcontroller/addchild(_:).md)
  A convenience method for adding a child view controller at the end of the [`children`](nsviewcontroller/children.md) array.
- [var children: [NSViewController]](nsviewcontroller/children.md)
  An array of view controllers that are hierarchical children of the view controller.
- [func insertChild(NSViewController, at: Int)](nsviewcontroller/insertchild(_:at:).md)
  Inserts a specified child view controller into the [`children`](nsviewcontroller/children.md) array at a specified position.
- [func removeChild(at: Int)](nsviewcontroller/removechild(at:).md)
  Removes a specified child controller from the view controller.
- [func removeFromParent()](nsviewcontroller/removefromparent.md)
  Removes the called view controller from its parent view controller.
- [func preferredContentSizeDidChange(for: NSViewController)](nsviewcontroller/preferredcontentsizedidchange(for:).md)
  Called when there is a change in value of the [`preferredContentSize`](nsviewcontroller/preferredcontentsize.md) property of a child view controller or a presented view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/transition(from:to:options:completionhandler:))*
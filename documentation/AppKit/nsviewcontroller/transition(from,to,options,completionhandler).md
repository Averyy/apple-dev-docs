# transition(from:to:options:completionHandler:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Performs a transition between two sibling child view controllers of the view controller.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func transition(from fromViewController: NSViewController, to toViewController: NSViewController, options: NSViewController.TransitionOptions = [], completionHandler completion: (@Sendable () -> Void)? = nil)
```

```swift
func transition(from fromViewController: NSViewController, to toViewController: NSViewController, options: NSViewController.TransitionOptions = []) async
```

```objc
- (void) transitionFromViewController:(NSViewController *) fromViewController toViewController:(NSViewController *) toViewController options:(NSViewControllerTransitionOptions) options completionHandler:(void (^)()) completion;
```

#### Discussion

Use this method to transition between sibling child view controllers owned by a parent view controller (which is the receiver of this method).

This method adds the view in the `toViewController` view controller to the superview of the view in the `fromViewController` view controller. Likewise, this method removes the `fromViewController` view from the parent view controller’s view hierarchy at the appropriate time. It is important to allow this method to add and remove these views.

> **Note**:  The receiver of this method must be the parent view controller of the `fromViewController` and `toViewController` view controllers, or else this method raises an exception.

To create a parent/child relationship between view controllers, use the [`addChild(_:)`](./addchild%28_%29.md) method or the [`insertChild(_:at:)`](./insertchild%28_,at%29.md) method.

## Parameters

- `fromViewController`: A child view controller whose view is visible in the view controller’s view hierarchy.

  > **Note**:  The view of this view controller must have a superview, or else this method raises an exception.
- `toViewController`: A child view controller whose view is not in the view controller’s view hierarchy.
- `options`: A bitmask of options that specify how you want to perform the transition animation. For the options, see the [`NSViewController.TransitionOptions`](./transitionoptions.md) enumeration.
- `completion`: A block called immediately after the transition animation completes.

## See Also

### Managing Child View Controllers in a Custom Container
- [func addChild(NSViewController)](./addchild%28_%29.md)
  A convenience method for adding a child view controller at the end of the [`children`](./children.md) array.
- [var children: [NSViewController]](./children.md)
  An array of view controllers that are hierarchical children of the view controller.
- [func insertChild(NSViewController, at: Int)](./insertchild%28_,at%29.md)
  Inserts a specified child view controller into the [`children`](./children.md) array at a specified position.
- [func removeChild(at: Int)](./removechild%28at%29.md)
  Removes a specified child controller from the view controller.
- [func removeFromParent()](./removefromparent%28%29.md)
  Removes the called view controller from its parent view controller.
- [func preferredContentSizeDidChange(for: NSViewController)](./preferredcontentsizedidchange%28for%29.md)
  Called when there is a change in value of the [`preferredContentSize`](./preferredcontentsize.md) property of a child view controller or a presented view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/transition(from:to:options:completionhandler:))*
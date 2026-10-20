# addChild(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

A convenience method for adding a child view controller at the end of the [`children`](./children.md) array.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func addChild(_ childViewController: NSViewController)
```

```objc
- (void) addChildViewController:(NSViewController *) childViewController;
```

## Parameters

- `childViewController`: The view controller to be added to the end of the [`children`](./children.md) array.

## See Also

### Managing Child View Controllers in a Custom Container
- [var children: [NSViewController]](./children.md)
  An array of view controllers that are hierarchical children of the view controller.
- [func transition(from: NSViewController, to: NSViewController, options: NSViewController.TransitionOptions, completionHandler: (() -> Void)?)](./transition%28from,to,options,completionhandler%29.md)
  Performs a transition between two sibling child view controllers of the view controller.
- [func insertChild(NSViewController, at: Int)](./insertchild%28_,at%29.md)
  Inserts a specified child view controller into the [`children`](./children.md) array at a specified position.
- [func removeChild(at: Int)](./removechild%28at%29.md)
  Removes a specified child controller from the view controller.
- [func removeFromParent()](./removefromparent%28%29.md)
  Removes the called view controller from its parent view controller.
- [func preferredContentSizeDidChange(for: NSViewController)](./preferredcontentsizedidchange%28for%29.md)
  Called when there is a change in value of the [`preferredContentSize`](./preferredcontentsize.md) property of a child view controller or a presented view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/addchild(_:))*
# insertChild(_:at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Inserts a specified child view controller into the [`children`](./children.md) array at a specified position.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func insertChild(_ childViewController: NSViewController, at index: Int)
```

```objc
- (void) insertChildViewController:(NSViewController *) childViewController atIndex:(NSInteger) index;
```

## Discussion

You should instead use the [`addChild(_:)`](./addchild%28_%29.md) method unless you want to perform work on child view controllers as you add them. In that case, override this method to perform that work.

If a child view controller has a different parent when you call this method, the child is first be removed from its existing parent by calling the child’s [`removeFromParent()`](./removefromparent%28%29.md) method.

## Parameters

- `childViewController`: The child view controller to add to the [`children`](./children.md) array.
- `index`: The index in the [`children`](./children.md) array at which to insert the child view controller. This value must not be greater than the count of elements in the array.

## See Also

### Managing Child View Controllers in a Custom Container
- [func addChild(NSViewController)](./addchild%28_%29.md)
  A convenience method for adding a child view controller at the end of the [`children`](./children.md) array.
- [var children: [NSViewController]](./children.md)
  An array of view controllers that are hierarchical children of the view controller.
- [func transition(from: NSViewController, to: NSViewController, options: NSViewController.TransitionOptions, completionHandler: (() -> Void)?)](./transition%28from,to,options,completionhandler%29.md)
  Performs a transition between two sibling child view controllers of the view controller.
- [func removeChild(at: Int)](./removechild%28at%29.md)
  Removes a specified child controller from the view controller.
- [func removeFromParent()](./removefromparent%28%29.md)
  Removes the called view controller from its parent view controller.
- [func preferredContentSizeDidChange(for: NSViewController)](./preferredcontentsizedidchange%28for%29.md)
  Called when there is a change in value of the [`preferredContentSize`](./preferredcontentsize.md) property of a child view controller or a presented view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/insertchild(_:at:))*
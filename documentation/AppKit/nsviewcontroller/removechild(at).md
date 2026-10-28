# removeChild(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes a specified child controller from the view controller.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func removeChild(at index: Int)
```

```objc
- (void) removeChildViewControllerAtIndex:(NSInteger) index;
```

## Discussion

Override this method if you want to perform work during the removal of a child view controller. If you do override this method, in your implementation call this method on `super`.

If you just want to remove a child view controller, instead use the [`removeFromParent()`](./removefromparent%28%29.md) method

## Parameters

- `index`: The index in the [`children`](./children.md) array for the child view controller you want to remove.

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
- [func removeFromParent()](./removefromparent%28%29.md)
  Removes the called view controller from its parent view controller.
- [func preferredContentSizeDidChange(for: NSViewController)](./preferredcontentsizedidchange%28for%29.md)
  Called when there is a change in value of the [`preferredContentSize`](./preferredcontentsize.md) property of a child view controller or a presented view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/removechild(at:))*
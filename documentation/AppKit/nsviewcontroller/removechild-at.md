# removeChild(at:)

**Framework**: AppKit  
**Kind**: method

Removes a specified child controller from the view controller.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func removeChild(at index: Int)
```

#### Discussion

Override this method if you want to perform work during the removal of a child view controller. If you do override this method, in your implementation call this method on `super`.

If you just want to remove a child view controller, instead use the [`removeFromParent()`](nsviewcontroller/removefromparent().md) method

## Parameters

- `index`: The index in the   array for the child view controller you want to remove.

## See Also

- [func addChild(NSViewController)](nsviewcontroller/addchild(_:).md)
  A convenience method for adding a child view controller at the end of the [`children`](nsviewcontroller/children.md) array.
- [var children: [NSViewController]](nsviewcontroller/children.md)
  An array of view controllers that are hierarchical children of the view controller.
- [func transition(from: NSViewController, to: NSViewController, options: NSViewController.TransitionOptions, completionHandler: (() -> Void)?)](nsviewcontroller/transition(from:to:options:completionhandler:).md)
  Performs a transition between two sibling child view controllers of the view controller.
- [func insertChild(NSViewController, at: Int)](nsviewcontroller/insertchild(_:at:).md)
  Inserts a specified child view controller into the [`children`](nsviewcontroller/children.md) array at a specified position.
- [func removeFromParent()](nsviewcontroller/removefromparent.md)
  Removes the called view controller from its parent view controller.
- [func preferredContentSizeDidChange(for: NSViewController)](nsviewcontroller/preferredcontentsizedidchange(for:).md)
  Called when there is a change in value of the [`preferredContentSize`](nsviewcontroller/preferredcontentsize.md) property of a child view controller or a presented view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/removechild(at:))*
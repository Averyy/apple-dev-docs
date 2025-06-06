# insertChild(_:at:)

**Framework**: AppKit  
**Kind**: method

Inserts a specified child view controller into the [`children`](nsviewcontroller/children.md) array at a specified position.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func insertChild(_ childViewController: NSViewController, at index: Int)
```

#### Discussion

You should instead use the [`addChild(_:)`](nsviewcontroller/addchild(_:).md) method unless you want to perform work on child view controllers as you add them. In that case, override this method to perform that work.

If a child view controller has a different parent when you call this method, the child is first be removed from its existing parent by calling the child’s [`removeFromParent()`](nsviewcontroller/removefromparent().md) method.

## Parameters

- `childViewController`: The child view controller to add to the   array.
- `index`: The index in the   array at which to insert the child view controller. This value must not be greater than the count of elements in the array.

## See Also

- [func addChild(NSViewController)](nsviewcontroller/addchild(_:).md)
  A convenience method for adding a child view controller at the end of the [`children`](nsviewcontroller/children.md) array.
- [var children: [NSViewController]](nsviewcontroller/children.md)
  An array of view controllers that are hierarchical children of the view controller.
- [func transition(from: NSViewController, to: NSViewController, options: NSViewController.TransitionOptions, completionHandler: (() -> Void)?)](nsviewcontroller/transition(from:to:options:completionhandler:).md)
  Performs a transition between two sibling child view controllers of the view controller.
- [func removeChild(at: Int)](nsviewcontroller/removechild(at:).md)
  Removes a specified child controller from the view controller.
- [func removeFromParent()](nsviewcontroller/removefromparent.md)
  Removes the called view controller from its parent view controller.
- [func preferredContentSizeDidChange(for: NSViewController)](nsviewcontroller/preferredcontentsizedidchange(for:).md)
  Called when there is a change in value of the [`preferredContentSize`](nsviewcontroller/preferredcontentsize.md) property of a child view controller or a presented view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/insertchild(_:at:))*
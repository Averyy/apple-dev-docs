# children

**Framework**: AppKit  
**Kind**: property

An array of view controllers that are hierarchical children of the view controller.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var children: [NSViewController] { get set }
```

#### Discussion

You can add or remove child view controllers by using this property. When you do, the [`addChild(_:)`](nsviewcontroller/addchild(_:).md) or [`removeFromParent()`](nsviewcontroller/removefromparent().md) method gets called accordingly.

## See Also

- [func addChild(NSViewController)](nsviewcontroller/addchild(_:).md)
  A convenience method for adding a child view controller at the end of the [`children`](nsviewcontroller/children.md) array.
- [func transition(from: NSViewController, to: NSViewController, options: NSViewController.TransitionOptions, completionHandler: (() -> Void)?)](nsviewcontroller/transition(from:to:options:completionhandler:).md)
  Performs a transition between two sibling child view controllers of the view controller.
- [func insertChild(NSViewController, at: Int)](nsviewcontroller/insertchild(_:at:).md)
  Inserts a specified child view controller into the [`children`](nsviewcontroller/children.md) array at a specified position.
- [func removeChild(at: Int)](nsviewcontroller/removechild(at:).md)
  Removes a specified child controller from the view controller.
- [func removeFromParent()](nsviewcontroller/removefromparent.md)
  Removes the called view controller from its parent view controller.
- [func preferredContentSizeDidChange(for: NSViewController)](nsviewcontroller/preferredcontentsizedidchange(for:).md)
  Called when there is a change in value of the [`preferredContentSize`](nsviewcontroller/preferredcontentsize.md) property of a child view controller or a presented view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/children)*
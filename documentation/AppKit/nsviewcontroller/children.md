# children

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array of view controllers that are hierarchical children of the view controller.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var children: [NSViewController] { get set }
```

```objc
@property (copy) NSArray<__kindof NSViewController *> * childViewControllers;
```

## Discussion

You can add or remove child view controllers by using this property. When you do, the [`addChild(_:)`](./addchild%28_%29.md) or [`removeFromParent()`](./removefromparent%28%29.md) method gets called accordingly.

## See Also

### Managing Child View Controllers in a Custom Container
- [func addChild(NSViewController)](./addchild%28_%29.md)
  A convenience method for adding a child view controller at the end of the [`children`](./children.md) array.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/children)*
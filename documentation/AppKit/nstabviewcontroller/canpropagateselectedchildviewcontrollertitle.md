# canPropagateSelectedChildViewControllerTitle

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the tab view controller gets its title from the selected child view controller.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var canPropagateSelectedChildViewControllerTitle: Bool { get set }
```

```objc
@property BOOL canPropagateSelectedChildViewControllerTitle;
```

## Discussion

When this property is [`true`](../../Swift/true.md) and the tab view controller’s own title is `nil`, the tab view controller gets its title from the [`title`](../nsviewcontroller/title.md) property of the selected child view controller. When this property is [`false`](../../Swift/false.md), the tab view controller always provides the title, which may be `nil`. The default value of this property is [`true`](../../Swift/true.md).

## See Also

### Configuring the Tab View
- [var tabStyle: NSTabViewController.TabStyle](./tabstyle-swift.property.md)
  The style used to display the tabs.
- [var tabView: NSTabView](./tabview.md)
  The tab view that manages the views of the interface.
- [var transitionOptions: NSViewController.TransitionOptions](./transitionoptions.md)
  The animation options to use when switching between tabs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewcontroller/canpropagateselectedchildviewcontrollertitle)*
# canPropagateSelectedChildViewControllerTitle

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the tab view controller gets its title from the selected child view controller.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var canPropagateSelectedChildViewControllerTitle: Bool { get set }
```

#### Discussion

When this property is [`true`](https://developer.apple.com/documentation/Swift/true) and the tab view controller’s own title is `nil`, the tab view controller gets its title from the [`title`](nsviewcontroller/title.md) property of the selected child view controller. When this property is [`false`](https://developer.apple.com/documentation/Swift/false), the tab view controller always provides the title, which may be `nil`. The default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var tabStyle: NSTabViewController.TabStyle](nstabviewcontroller/tabstyle-swift.property.md)
  The style used to display the tabs.
- [var tabView: NSTabView](nstabviewcontroller/tabview.md)
  The tab view that manages the views of the interface.
- [var transitionOptions: NSViewController.TransitionOptions](nstabviewcontroller/transitionoptions.md)
  The animation options to use when switching between tabs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewcontroller/canpropagateselectedchildviewcontrollertitle)*
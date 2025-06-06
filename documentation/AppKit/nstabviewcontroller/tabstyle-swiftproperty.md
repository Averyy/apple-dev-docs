# tabStyle

**Framework**: AppKit  
**Kind**: property

The style used to display the tabs.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var tabStyle: NSTabViewController.TabStyle { get set }
```

#### Discussion

The default value of this property is [`NSTabViewController.TabStyle.segmentedControlOnTop`](nstabviewcontroller/tabstyle-swift.enum/segmentedcontrolontop.md). Changing the style at runtime updates the appearance of the tab view controller interface.

## See Also

- [var tabView: NSTabView](nstabviewcontroller/tabview.md)
  The tab view that manages the views of the interface.
- [var transitionOptions: NSViewController.TransitionOptions](nstabviewcontroller/transitionoptions.md)
  The animation options to use when switching between tabs.
- [var canPropagateSelectedChildViewControllerTitle: Bool](nstabviewcontroller/canpropagateselectedchildviewcontrollertitle.md)
  A Boolean value indicating whether the tab view controller gets its title from the selected child view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewcontroller/tabstyle-swift.property)*
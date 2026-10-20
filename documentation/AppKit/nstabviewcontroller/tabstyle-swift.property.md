# tabStyle

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The style used to display the tabs.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var tabStyle: NSTabViewController.TabStyle { get set }
```

```objc
@property NSTabViewControllerTabStyle tabStyle;
```

#### Discussion

The default value of this property is [`NSTabViewController.TabStyle.segmentedControlOnTop`](./tabstyle-swift.enum/segmentedcontrolontop.md). Changing the style at runtime updates the appearance of the tab view controller interface.

## See Also

### Configuring the Tab View
- [var tabView: NSTabView](./tabview.md)
  The tab view that manages the views of the interface.
- [var transitionOptions: NSViewController.TransitionOptions](./transitionoptions.md)
  The animation options to use when switching between tabs.
- [var canPropagateSelectedChildViewControllerTitle: Bool](./canpropagateselectedchildviewcontrollertitle.md)
  A Boolean value indicating whether the tab view controller gets its title from the selected child view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewcontroller/tabstyle-swift.property)*
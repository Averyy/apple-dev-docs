# transitionOptions

**Framework**: AppKit  
**Kind**: property

The animation options to use when switching between tabs.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var transitionOptions: NSViewController.TransitionOptions { get set }
```

#### Discussion

By default, this property is set to the [`crossfade`](nsviewcontroller/transitionoptions/crossfade.md) and [`allowUserInteraction`](nsviewcontroller/transitionoptions/allowuserinteraction.md) options.

The tab view controller uses the [`transition(from:to:options:completionHandler:)`](nsviewcontroller/transition(from:to:options:completionhandler:).md) method to perform transitions between tabs. For more information about how transitions happen, see the description of that method.

## See Also

- [var tabStyle: NSTabViewController.TabStyle](nstabviewcontroller/tabstyle-swift.property.md)
  The style used to display the tabs.
- [var tabView: NSTabView](nstabviewcontroller/tabview.md)
  The tab view that manages the views of the interface.
- [var canPropagateSelectedChildViewControllerTitle: Bool](nstabviewcontroller/canpropagateselectedchildviewcontrollertitle.md)
  A Boolean value indicating whether the tab view controller gets its title from the selected child view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewcontroller/transitionoptions)*
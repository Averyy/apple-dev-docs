# transitionOptions

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The animation options to use when switching between tabs.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var transitionOptions: NSViewController.TransitionOptions { get set }
```

```objc
@property NSViewControllerTransitionOptions transitionOptions;
```

## Discussion

By default, this property is set to the [`crossfade`](../nsviewcontroller/transitionoptions/crossfade.md) and [`allowUserInteraction`](../nsviewcontroller/transitionoptions/allowuserinteraction.md) options.

The tab view controller uses the [`transition(from:to:options:completionHandler:)`](../nsviewcontroller/transition%28from,to,options,completionhandler%29.md) method to perform transitions between tabs. For more information about how transitions happen, see the description of that method.

## See Also

### Configuring the Tab View
- [var tabStyle: NSTabViewController.TabStyle](./tabstyle-swift.property.md)
  The style used to display the tabs.
- [var tabView: NSTabView](./tabview.md)
  The tab view that manages the views of the interface.
- [var canPropagateSelectedChildViewControllerTitle: Bool](./canpropagateselectedchildviewcontrollertitle.md)
  A Boolean value indicating whether the tab view controller gets its title from the selected child view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewcontroller/transitionoptions)*
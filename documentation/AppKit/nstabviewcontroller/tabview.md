# tabView

**Framework**: AppKit  
**Kind**: property

The tab view that manages the views of the interface.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var tabView: NSTabView { get set }
```

#### Discussion

Use this property to access the tab view controller’s content view. The object in this property may not be the same as the one in the tab view controller’s [`view`](nsviewcontroller/view.md) property. The tab view controller works directly with the [`NSTabView`](nstabview.md) object, setting itself as the tab view’s delegate. You must not modify the items of the tab view directly or change its delegate. Instead, use the methods of this class to make your changes.

Accessing this property creates the tab view object if it does not already exist. To determine whether the tab view has been created (without creating it prematurely), use the [`isViewLoaded`](nsviewcontroller/isviewloaded.md) property.

You may provide your own tab view by assigning it to this property. If you do so, you must assign your custom object before the tab view controller creates one of its own. In other words, you must assign your tab view object to this property while the [`isViewLoaded`](nsviewcontroller/isviewloaded.md) property is still [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var tabStyle: NSTabViewController.TabStyle](nstabviewcontroller/tabstyle-swift.property.md)
  The style used to display the tabs.
- [var transitionOptions: NSViewController.TransitionOptions](nstabviewcontroller/transitionoptions.md)
  The animation options to use when switching between tabs.
- [var canPropagateSelectedChildViewControllerTitle: Bool](nstabviewcontroller/canpropagateselectedchildviewcontrollertitle.md)
  A Boolean value indicating whether the tab view controller gets its title from the selected child view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewcontroller/tabview)*
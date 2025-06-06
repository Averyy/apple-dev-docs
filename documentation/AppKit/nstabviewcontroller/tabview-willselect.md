# tabView(_:willSelect:)

**Framework**: AppKit  
**Kind**: method

Informs the tab view controller that the specified tab is about to be selected.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func tabView(_ tabView: NSTabView, willSelect tabViewItem: NSTabViewItem?)
```

#### Discussion

This method is a delegate method called by the [`NSTabView`](nstabview.md) object when changes occur. Use it to update your UI or perform any tasks before a tab is selected.

If you override this method, you must call `super` at some point in your implementation.

## Parameters

- `tabView`: The tab view object whose tab is about to be selected.
- `tabViewItem`: The tab view item that will be selected.

## See Also

- [func viewDidLoad()](nstabviewcontroller/viewdidload.md)
  Called after the view controller’s view has been loaded into memory.
- [func tabView(NSTabView, shouldSelect: NSTabViewItem?) -> Bool](nstabviewcontroller/tabview(_:shouldselect:).md)
  Asks the tab view controller if the specified tab should be selected.
- [func tabView(NSTabView, didSelect: NSTabViewItem?)](nstabviewcontroller/tabview(_:didselect:).md)
  Informs the tab view controller that the specified tab was selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewcontroller/tabview(_:willselect:))*
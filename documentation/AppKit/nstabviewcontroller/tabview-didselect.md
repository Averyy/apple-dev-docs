# tabView(_:didSelect:)

**Framework**: AppKit  
**Kind**: method

Informs the tab view controller that the specified tab was selected.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func tabView(_ tabView: NSTabView, didSelect tabViewItem: NSTabViewItem?)
```

#### Discussion

This method is a delegate method called by the [`NSTabView`](nstabview.md) object when changes occur. Use it to perform any necessary tasks after a tab is selected.

If you override this method, you must call `super` at some point in your implementation.

## Parameters

- `tabView`: The tab view object whose tab was selected.
- `tabViewItem`: The tab view item that was selected.

## See Also

- [func viewDidLoad()](nstabviewcontroller/viewdidload.md)
  Called after the view controller’s view has been loaded into memory.
- [func tabView(NSTabView, shouldSelect: NSTabViewItem?) -> Bool](nstabviewcontroller/tabview(_:shouldselect:).md)
  Asks the tab view controller if the specified tab should be selected.
- [func tabView(NSTabView, willSelect: NSTabViewItem?)](nstabviewcontroller/tabview(_:willselect:).md)
  Informs the tab view controller that the specified tab is about to be selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewcontroller/tabview(_:didselect:))*
# tabView(_:willSelect:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Informs the tab view controller that the specified tab is about to be selected.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func tabView(_ tabView: NSTabView, willSelect tabViewItem: NSTabViewItem?)
```

```objc
- (void) tabView:(NSTabView *) tabView willSelectTabViewItem:(NSTabViewItem *) tabViewItem;
```

## Discussion

This method is a delegate method called by the [`NSTabView`](../nstabview.md) object when changes occur. Use it to update your UI or perform any tasks before a tab is selected.

If you override this method, you must call `super` at some point in your implementation.

## Parameters

- `tabView`: The tab view object whose tab is about to be selected.
- `tabViewItem`: The tab view item that will be selected.

## See Also

### Responding to Tab View Events
- [func viewDidLoad()](./viewdidload%28%29.md)
  Called after the view controller’s view has been loaded into memory.
- [func tabView(NSTabView, shouldSelect: NSTabViewItem?) -> Bool](./tabview%28_,shouldselect%29.md)
  Asks the tab view controller if the specified tab should be selected.
- [func tabView(NSTabView, didSelect: NSTabViewItem?)](./tabview%28_,didselect%29.md)
  Informs the tab view controller that the specified tab was selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewcontroller/tabview(_:willselect:))*
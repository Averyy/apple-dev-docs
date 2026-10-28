# tabView(_:shouldSelect:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Asks the tab view controller if the specified tab should be selected.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func tabView(_ tabView: NSTabView, shouldSelect tabViewItem: NSTabViewItem?) -> Bool
```

```objc
- (BOOL) tabView:(NSTabView *) tabView shouldSelectTabViewItem:(NSTabViewItem *) tabViewItem;
```

## Return Value

[`true`](../../Swift/true.md) if the tab should be selected or [`false`](../../Swift/false.md) if it should not be selected.

## Discussion

This method is a delegate method called by the [`NSTabView`](../nstabview.md) object when changes occur. Use it to dynamically determine whether a tab should be selected.

If you override this method, you must call `super` at some point in your implementation.

## Parameters

- `tabView`: The tab view object making the request.
- `tabViewItem`: The tab view item to select.

## See Also

### Responding to Tab View Events
- [func viewDidLoad()](./viewdidload%28%29.md)
  Called after the view controller’s view has been loaded into memory.
- [func tabView(NSTabView, willSelect: NSTabViewItem?)](./tabview%28_,willselect%29.md)
  Informs the tab view controller that the specified tab is about to be selected.
- [func tabView(NSTabView, didSelect: NSTabViewItem?)](./tabview%28_,didselect%29.md)
  Informs the tab view controller that the specified tab was selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewcontroller/tabview(_:shouldselect:))*
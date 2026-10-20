# tabView(_:willSelect:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Informs the delegate that `tabView` is about to select `tabViewItem`.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func tabView(_ tabView: NSTabView, willSelect tabViewItem: NSTabViewItem?)
```

```objc
- (void) tabView:(NSTabView *) tabView willSelectTabViewItem:(NSTabViewItem *) tabViewItem;
```

## Parameters

- `tabView`: The tab view that sent the request.
- `tabViewItem`: The tab view item that is about to be selected.

## See Also

### Selecting a Tab
- [func tabView(NSTabView, shouldSelect: NSTabViewItem?) -> Bool](./tabview%28_,shouldselect%29.md)
  Invoked just before `tabViewItem` in `tabView` is selected.
- [func tabView(NSTabView, didSelect: NSTabViewItem?)](./tabview%28_,didselect%29.md)
  Informs the delegate that `tabView` has selected `tabViewItem`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewdelegate/tabview(_:willselect:))*
# tabView(_:didSelect:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Informs the delegate that `tabView` has selected `tabViewItem`.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func tabView(_ tabView: NSTabView, didSelect tabViewItem: NSTabViewItem?)
```

```objc
- (void) tabView:(NSTabView *) tabView didSelectTabViewItem:(NSTabViewItem *) tabViewItem;
```

## Parameters

- `tabView`: The tab view that sent the request.
- `tabViewItem`: The tab view item that was selected.

## See Also

### Selecting a Tab
- [func tabView(NSTabView, shouldSelect: NSTabViewItem?) -> Bool](./tabview%28_,shouldselect%29.md)
  Invoked just before `tabViewItem` in `tabView` is selected.
- [func tabView(NSTabView, willSelect: NSTabViewItem?)](./tabview%28_,willselect%29.md)
  Informs the delegate that `tabView` is about to select `tabViewItem`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewdelegate/tabview(_:didselect:))*
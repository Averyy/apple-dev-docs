# tabView(_:shouldSelect:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked just before `tabViewItem` in `tabView` is selected.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func tabView(_ tabView: NSTabView, shouldSelect tabViewItem: NSTabViewItem?) -> Bool
```

```objc
- (BOOL) tabView:(NSTabView *) tabView shouldSelectTabViewItem:(NSTabViewItem *) tabViewItem;
```

## Return Value

[`true`](../../Swift/true.md) if the tab view item should be selected, otherwise [`false`](../../Swift/false.md).

## Parameters

- `tabView`: The tab view that sent the request.
- `tabViewItem`: The tab view item to select.

## See Also

### Selecting a Tab
- [func tabView(NSTabView, willSelect: NSTabViewItem?)](./tabview%28_,willselect%29.md)
  Informs the delegate that `tabView` is about to select `tabViewItem`.
- [func tabView(NSTabView, didSelect: NSTabViewItem?)](./tabview%28_,didselect%29.md)
  Informs the delegate that `tabView` has selected `tabViewItem`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewdelegate/tabview(_:shouldselect:))*
# tabView(_:didSelect:)

**Framework**: AppKit  
**Kind**: method

Informs the delegate that `tabView` has selected `tabViewItem`.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func tabView(_ tabView: NSTabView, didSelect tabViewItem: NSTabViewItem?)
```

## Parameters

- `tabView`: The tab view that sent the request.
- `tabViewItem`: The tab view item that was selected.

## See Also

- [func tabView(NSTabView, shouldSelect: NSTabViewItem?) -> Bool](nstabviewdelegate/tabview(_:shouldselect:).md)
  Invoked just before `tabViewItem` in `tabView` is selected.
- [func tabView(NSTabView, willSelect: NSTabViewItem?)](nstabviewdelegate/tabview(_:willselect:).md)
  Informs the delegate that `tabView` is about to select `tabViewItem`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewdelegate/tabview(_:didselect:))*
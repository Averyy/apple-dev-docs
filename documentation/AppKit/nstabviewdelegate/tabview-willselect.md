# tabView(_:willSelect:)

**Framework**: AppKit  
**Kind**: method

Informs the delegate that `tabView` is about to select `tabViewItem`.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func tabView(_ tabView: NSTabView, willSelect tabViewItem: NSTabViewItem?)
```

## Parameters

- `tabView`: The tab view that sent the request.
- `tabViewItem`: The tab view item that is about to be selected.

## See Also

- [func tabView(NSTabView, shouldSelect: NSTabViewItem?) -> Bool](nstabviewdelegate/tabview(_:shouldselect:).md)
  Invoked just before `tabViewItem` in `tabView` is selected.
- [func tabView(NSTabView, didSelect: NSTabViewItem?)](nstabviewdelegate/tabview(_:didselect:).md)
  Informs the delegate that `tabView` has selected `tabViewItem`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewdelegate/tabview(_:willselect:))*
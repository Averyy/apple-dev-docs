# tabView(_:shouldSelect:)

**Framework**: AppKit  
**Kind**: method

Invoked just before `tabViewItem` in `tabView` is selected.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func tabView(_ tabView: NSTabView, shouldSelect tabViewItem: NSTabViewItem?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the tab view item should be selected, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `tabView`: The tab view that sent the request.
- `tabViewItem`: The tab view item to select.

## See Also

- [func tabView(NSTabView, willSelect: NSTabViewItem?)](nstabviewdelegate/tabview(_:willselect:).md)
  Informs the delegate that `tabView` is about to select `tabViewItem`.
- [func tabView(NSTabView, didSelect: NSTabViewItem?)](nstabviewdelegate/tabview(_:didselect:).md)
  Informs the delegate that `tabView` has selected `tabViewItem`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewdelegate/tabview(_:shouldselect:))*
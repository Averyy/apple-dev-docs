# selectTabViewItem(_:)

**Framework**: AppKit  
**Kind**: method

Selects the specified tab view item.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func selectTabViewItem(_ tabViewItem: NSTabViewItem?)
```

#### Discussion

If there is a delegate and the delegate supports it, sends the delegate the [`tabView(_:shouldSelect:)`](nstabviewdelegate/tabview(_:shouldselect:).md) message.

## Parameters

- `tabViewItem`: The tab item to select.

## See Also

- [func insertTabViewItem(NSTabViewItem, at: Int)](nstabview/inserttabviewitem(_:at:).md)
  Inserts the specified item into the tab view’s array of tab view items at the specified index.
- [func selectFirstTabViewItem(Any?)](nstabview/selectfirsttabviewitem(_:).md)
  This action method selects the first tab view item.
- [func selectLastTabViewItem(Any?)](nstabview/selectlasttabviewitem(_:).md)
  This action method selects the last tab view item.
- [func selectNextTabViewItem(Any?)](nstabview/selectnexttabviewitem(_:).md)
  This action method selects the next tab view item in the sequence.
- [func selectPreviousTabViewItem(Any?)](nstabview/selectprevioustabviewitem(_:).md)
  This action method selects the previous tab view item in the sequence.
- [func selectTabViewItem(at: Int)](nstabview/selecttabviewitem(at:).md)
  Selects the tab view item specified by `index`.
- [func selectTabViewItem(withIdentifier: Any)](nstabview/selecttabviewitem(withidentifier:).md)
  Selects the tab view item specified by `identifier`.
- [var selectedTabViewItem: NSTabViewItem?](nstabview/selectedtabviewitem.md)
  The tab view item for the currently selected tab.
- [func takeSelectedTabViewItemFromSender(Any?)](nstabview/takeselectedtabviewitemfromsender(_:).md)
  Sets the selected tab view item to the selected item obtained from the sender.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabview/selecttabviewitem(_:))*
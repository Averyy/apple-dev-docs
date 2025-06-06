# selectTabViewItem(withIdentifier:)

**Framework**: AppKit  
**Kind**: method

Selects the tab view item specified by `identifier`.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func selectTabViewItem(withIdentifier identifier: Any)
```

## Parameters

- `identifier`: The identifier of the tab item to select.

## See Also

- [var identifier: Any?](nstabviewitem/identifier.md)
  Sets the receiver’s optional identifier object to `identifier`.
- [func selectFirstTabViewItem(Any?)](nstabview/selectfirsttabviewitem(_:).md)
  This action method selects the first tab view item.
- [func selectLastTabViewItem(Any?)](nstabview/selectlasttabviewitem(_:).md)
  This action method selects the last tab view item.
- [func selectNextTabViewItem(Any?)](nstabview/selectnexttabviewitem(_:).md)
  This action method selects the next tab view item in the sequence.
- [func selectPreviousTabViewItem(Any?)](nstabview/selectprevioustabviewitem(_:).md)
  This action method selects the previous tab view item in the sequence.
- [func selectTabViewItem(NSTabViewItem?)](nstabview/selecttabviewitem(_:).md)
  Selects the specified tab view item.
- [func selectTabViewItem(at: Int)](nstabview/selecttabviewitem(at:).md)
  Selects the tab view item specified by `index`.
- [var selectedTabViewItem: NSTabViewItem?](nstabview/selectedtabviewitem.md)
  The tab view item for the currently selected tab.
- [func takeSelectedTabViewItemFromSender(Any?)](nstabview/takeselectedtabviewitemfromsender(_:).md)
  Sets the selected tab view item to the selected item obtained from the sender.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabview/selecttabviewitem(withidentifier:))*
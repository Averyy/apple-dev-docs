# selectPreviousTabViewItem(_:)

**Framework**: AppKit  
**Kind**: method

This action method selects the previous tab view item in the sequence.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func selectPreviousTabViewItem(_ sender: Any?)
```

#### Discussion

If the currently visible item is the first item in the sequence, this method does nothing, and the first pane remains displayed.

## Parameters

- `sender`: Typically the object that sent the message.

## See Also

- [func selectFirstTabViewItem(Any?)](nstabview/selectfirsttabviewitem(_:).md)
  This action method selects the first tab view item.
- [func selectLastTabViewItem(Any?)](nstabview/selectlasttabviewitem(_:).md)
  This action method selects the last tab view item.
- [func selectNextTabViewItem(Any?)](nstabview/selectnexttabviewitem(_:).md)
  This action method selects the next tab view item in the sequence.
- [func selectTabViewItem(NSTabViewItem?)](nstabview/selecttabviewitem(_:).md)
  Selects the specified tab view item.
- [func selectTabViewItem(at: Int)](nstabview/selecttabviewitem(at:).md)
  Selects the tab view item specified by `index`.
- [func selectTabViewItem(withIdentifier: Any)](nstabview/selecttabviewitem(withidentifier:).md)
  Selects the tab view item specified by `identifier`.
- [var selectedTabViewItem: NSTabViewItem?](nstabview/selectedtabviewitem.md)
  The tab view item for the currently selected tab.
- [func takeSelectedTabViewItemFromSender(Any?)](nstabview/takeselectedtabviewitemfromsender(_:).md)
  Sets the selected tab view item to the selected item obtained from the sender.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabview/selectprevioustabviewitem(_:))*
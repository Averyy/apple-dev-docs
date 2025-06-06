# selectedTabViewItem

**Framework**: AppKit  
**Kind**: property

The tab view item for the currently selected tab.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var selectedTabViewItem: NSTabViewItem? { get }
```

#### Discussion

If no item is selected, the value of this property is `nil`.

## See Also

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
- [func selectTabViewItem(withIdentifier: Any)](nstabview/selecttabviewitem(withidentifier:).md)
  Selects the tab view item specified by `identifier`.
- [func takeSelectedTabViewItemFromSender(Any?)](nstabview/takeselectedtabviewitemfromsender(_:).md)
  Sets the selected tab view item to the selected item obtained from the sender.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabview/selectedtabviewitem)*
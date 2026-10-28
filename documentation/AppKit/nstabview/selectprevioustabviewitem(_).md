# selectPreviousTabViewItem(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

This action method selects the previous tab view item in the sequence.

**Availability**:
- macOS

## Declaration

```swift
func selectPreviousTabViewItem(_ sender: Any?)
```

```objc
- (void) selectPreviousTabViewItem:(id) sender;
```

## Discussion

If the currently visible item is the first item in the sequence, this method does nothing, and the first pane remains displayed.

## Parameters

- `sender`: Typically the object that sent the message.

## See Also

### Selecting a Tab
- [func selectFirstTabViewItem(Any?)](./selectfirsttabviewitem%28_%29.md)
  This action method selects the first tab view item.
- [func selectLastTabViewItem(Any?)](./selectlasttabviewitem%28_%29.md)
  This action method selects the last tab view item.
- [func selectNextTabViewItem(Any?)](./selectnexttabviewitem%28_%29.md)
  This action method selects the next tab view item in the sequence.
- [func selectTabViewItem(NSTabViewItem?)](./selecttabviewitem%28_%29.md)
  Selects the specified tab view item.
- [func selectTabViewItem(at: Int)](./selecttabviewitem%28at%29.md)
  Selects the tab view item specified by `index`.
- [func selectTabViewItem(withIdentifier: Any)](./selecttabviewitem%28withidentifier%29.md)
  Selects the tab view item specified by `identifier`.
- [var selectedTabViewItem: NSTabViewItem?](./selectedtabviewitem.md)
  The tab view item for the currently selected tab.
- [func takeSelectedTabViewItemFromSender(Any?)](./takeselectedtabviewitemfromsender%28_%29.md)
  Sets the selected tab view item to the selected item obtained from the sender.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabview/selectprevioustabviewitem(_:))*
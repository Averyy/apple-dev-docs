# selectTabViewItem(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Selects the tab view item specified by `index`.

**Availability**:
- macOS

## Declaration

```swift
func selectTabViewItem(at index: Int)
```

```objc
- (void) selectTabViewItemAtIndex:(NSInteger) index;
```

#### Discussion

The `index` parameter is base 0. If there is a delegate and the delegate supports it, sends the delegate the [`tabView(_:shouldSelect:)`](../nstabviewdelegate/tabview%28_,shouldselect%29.md) message.

## Parameters

- `index`: The index of the tab item to selected.

## See Also

### Related Documentation
- [func insertTabViewItem(NSTabViewItem, at: Int)](./inserttabviewitem%28_,at%29.md)
  Inserts the specified item into the tab view’s array of tab view items at the specified index.
### Selecting a Tab
- [func selectFirstTabViewItem(Any?)](./selectfirsttabviewitem%28_%29.md)
  This action method selects the first tab view item.
- [func selectLastTabViewItem(Any?)](./selectlasttabviewitem%28_%29.md)
  This action method selects the last tab view item.
- [func selectNextTabViewItem(Any?)](./selectnexttabviewitem%28_%29.md)
  This action method selects the next tab view item in the sequence.
- [func selectPreviousTabViewItem(Any?)](./selectprevioustabviewitem%28_%29.md)
  This action method selects the previous tab view item in the sequence.
- [func selectTabViewItem(NSTabViewItem?)](./selecttabviewitem%28_%29.md)
  Selects the specified tab view item.
- [func selectTabViewItem(withIdentifier: Any)](./selecttabviewitem%28withidentifier%29.md)
  Selects the tab view item specified by `identifier`.
- [var selectedTabViewItem: NSTabViewItem?](./selectedtabviewitem.md)
  The tab view item for the currently selected tab.
- [func takeSelectedTabViewItemFromSender(Any?)](./takeselectedtabviewitemfromsender%28_%29.md)
  Sets the selected tab view item to the selected item obtained from the sender.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabview/selecttabviewitem(at:))*
# selectTabViewItem(withIdentifier:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Selects the tab view item specified by `identifier`.

**Availability**:
- macOS

## Declaration

```swift
func selectTabViewItem(withIdentifier identifier: Any)
```

```objc
- (void) selectTabViewItemWithIdentifier:(id) identifier;
```

## Parameters

- `identifier`: The identifier of the tab item to select.

## See Also

### Related Documentation
- [var identifier: Any?](../nstabviewitem/identifier.md)
  Sets the receiver’s optional identifier object to `identifier`.
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
- [func selectTabViewItem(at: Int)](./selecttabviewitem%28at%29.md)
  Selects the tab view item specified by `index`.
- [var selectedTabViewItem: NSTabViewItem?](./selectedtabviewitem.md)
  The tab view item for the currently selected tab.
- [func takeSelectedTabViewItemFromSender(Any?)](./takeselectedtabviewitemfromsender%28_%29.md)
  Sets the selected tab view item to the selected item obtained from the sender.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabview/selecttabviewitem(withidentifier:))*
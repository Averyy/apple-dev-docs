# selectedTabViewItem

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The tab view item for the currently selected tab.

**Availability**:
- macOS

## Declaration

```swift
var selectedTabViewItem: NSTabViewItem? { get }
```

```objc
@property (strong, readonly, nullable) NSTabViewItem * selectedTabViewItem;
```

#### Discussion

If no item is selected, the value of this property is `nil`.

## See Also

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
- [func selectTabViewItem(withIdentifier: Any)](./selecttabviewitem%28withidentifier%29.md)
  Selects the tab view item specified by `identifier`.
- [func takeSelectedTabViewItemFromSender(Any?)](./takeselectedtabviewitemfromsender%28_%29.md)
  Sets the selected tab view item to the selected item obtained from the sender.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabview/selectedtabviewitem)*
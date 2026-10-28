# selectedTabViewItemIndex

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The index of the selected tab.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var selectedTabViewItemIndex: Int { get set }
```

```objc
@property NSInteger selectedTabViewItemIndex;
```

## Discussion

Use this property to get and set the selected tab. The property is key-value coding compliant and can be the target of bindings.

## See Also

### Managing Tab View Items
- [var tabViewItems: [NSTabViewItem]](./tabviewitems.md)
  The array of tab view items used to manage each of the child view controllers.
- [func tabViewItem(for: NSViewController) -> NSTabViewItem?](./tabviewitem%28for%29.md)
  Returns the tab view item for the specified child view controller.
- [func addTabViewItem(NSTabViewItem)](./addtabviewitem%28_%29.md)
  Adds the specified tab to the end of the tab view controller’s list of tabs.
- [func insertTabViewItem(NSTabViewItem, at: Int)](./inserttabviewitem%28_,at%29.md)
  Inserts a tab view into the tab view controller’s list of tabs.
- [func removeTabViewItem(NSTabViewItem)](./removetabviewitem%28_%29.md)
  Removes the specified tab view item from the tab view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewcontroller/selectedtabviewitemindex)*
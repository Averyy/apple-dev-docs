# tabViewDidChangeNumberOfTabViewItems(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Informs the delegate that the number of tab view items in `tabView` has changed.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func tabViewDidChangeNumberOfTabViewItems(_ tabView: NSTabView)
```

```objc
- (void) tabViewDidChangeNumberOfTabViewItems:(NSTabView *) tabView;
```

## Parameters

- `tabView`: The tab view that added or removed tabview items.

## See Also

### Related Documentation
- [Tab View Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TabView/TabView.html#//apple_ref/doc/uid/10000074i)
- [var numberOfTabViewItems: Int](../nstabview/numberoftabviewitems.md)
  The number of items in the tab view’s array of tab view items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewdelegate/tabviewdidchangenumberoftabviewitems(_:))*
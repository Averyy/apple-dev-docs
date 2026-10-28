# minimumVisibleRowCount

**Framework**: Notification Center  
**Kind**: property  
**Role**: Instance Property

The minimum number of visible rows to display.

**Availability**:
- macOS 10.10+ - Deprecated in 11.0

> **Deprecated**: Use [WidgetKit](../../WidgetKit/WidgetKit.md) instead.

## Declaration

```swift
var minimumVisibleRowCount: Int { get set }
```

```objc
@property (assign) NSUInteger minimumVisibleRowCount;
```

## Discussion

Set this property to ensure that the widget’s list displays a minimum number of rows. The default value of this property is `0`.

If the value of `minimumVisibleRowCount` is nonzero and the number of items in [`contents`](./contents.md) is greater than this value, the list view controller displays the minimum number of rows and adds a “Show More…” button.

## See Also

### Customizing the List Appearance
- [var hasDividerLines: Bool](./hasdividerlines.md)
  A Boolean value that indicates whether list displays divider lines between rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetlistviewcontroller/minimumvisiblerowcount)*
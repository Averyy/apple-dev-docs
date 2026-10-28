# showsAddButtonWhenEditing

**Framework**: Notification Center  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether an Add (+) button is displayed while the list is in editing mode.

**Availability**:
- macOS 10.10+ - Deprecated in 11.0

> **Deprecated**: Use [WidgetKit](../../WidgetKit/WidgetKit.md) instead.

## Declaration

```swift
var showsAddButtonWhenEditing: Bool { get set }
```

```objc
@property (assign) BOOL showsAddButtonWhenEditing;
```

## Discussion

If users click the Add (+) button while in editing mode, the button’s action send the [`widgetListPerformAddAction(_:)`](../ncwidgetlistviewdelegate/widgetlistperformaddaction%28_%29.md) message to the [`delegate`](./delegate.md).

## See Also

### Supporting Editing
- [var editing: Bool](./editing.md)
  A Boolean value that indicates whether the list is in editing mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetlistviewcontroller/showsaddbuttonwhenediting)*
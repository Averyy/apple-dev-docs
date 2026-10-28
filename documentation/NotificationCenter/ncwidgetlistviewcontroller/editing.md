# editing

**Framework**: Notification Center  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the list is in editing mode.

**Availability**:
- macOS 10.10+ - Deprecated in 11.0

> **Deprecated**: Use [WidgetKit](../../WidgetKit/WidgetKit.md) instead.

## Declaration

```swift
var editing: Bool { get set }
```

```objc
@property (assign) BOOL editing;
```

## Discussion

When you set this property to [`true`](../../Swift/true.md), the list view controller can display controls for reordering and removing rows. The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Supporting Editing
- [var showsAddButtonWhenEditing: Bool](./showsaddbuttonwhenediting.md)
  A Boolean value that indicates whether an Add (+) button is displayed while the list is in editing mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetlistviewcontroller/editing)*
# showsAddButtonWhenEditing

**Framework**: Notification Center  
**Kind**: property

A Boolean value that indicates whether an Add (+) button is displayed while the list is in editing mode.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var showsAddButtonWhenEditing: Bool { get set }
```

#### Discussion

If users click the Add (+) button while in editing mode, the button’s action send the [`widgetListPerformAddAction(_:)`](ncwidgetlistviewdelegate/widgetlistperformaddaction(_:).md) message to the [`delegate`](ncwidgetlistviewcontroller/delegate.md).

## See Also

- [var editing: Bool](ncwidgetlistviewcontroller/editing.md)
  A Boolean value that indicates whether the list is in editing mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetlistviewcontroller/showsaddbuttonwhenediting)*
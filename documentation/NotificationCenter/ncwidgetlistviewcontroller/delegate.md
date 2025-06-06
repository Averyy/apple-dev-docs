# delegate

**Framework**: Notification Center  
**Kind**: property

The list view controller’s delegate or `nil` if the receiver doesn’t have a delegate.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@IBOutlet
@MainActor weak var delegate: (any NCWidgetListViewDelegate)? { get set }
```

#### Discussion

A list view controller’s delegate provides a custom view controller for each object in [`contents`](ncwidgetlistviewcontroller/contents.md). The delegate also performs editing-related functions, such as responding to interaction with an Add (+) button and reordering and removing rows.

To learn about the methods the delegate can implement, see [`NCWidgetListViewDelegate`](ncwidgetlistviewdelegate.md).

## See Also

- [protocol NCWidgetListViewDelegate](ncwidgetlistviewdelegate.md)
  The interface for handling content display and editing in the list view of a macOS Today widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetlistviewcontroller/delegate)*
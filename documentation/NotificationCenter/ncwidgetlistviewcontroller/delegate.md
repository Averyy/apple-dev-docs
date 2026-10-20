# delegate

**Framework**: Notification Center  
**Kind**: property  
**Role**: Instance Property

The list view controller’s delegate or `nil` if the receiver doesn’t have a delegate.

**Availability**:
- macOS 10.10+ - Deprecated in 11.0

> **Deprecated**: Use [WidgetKit](../../WidgetKit/WidgetKit.md) instead.

## Declaration

```swift
@IBOutlet
weak var delegate: (any NCWidgetListViewDelegate)? { get set }
```

```objc
@property (weak, nullable) id<NCWidgetListViewDelegate> delegate;
```

#### Discussion

A list view controller’s delegate provides a custom view controller for each object in [`contents`](./contents.md). The delegate also performs editing-related functions, such as responding to interaction with an Add (+) button and reordering and removing rows.

To learn about the methods the delegate can implement, see [`NCWidgetListViewDelegate`](../ncwidgetlistviewdelegate.md).

## See Also

### Displaying and Editing List Content
- [protocol NCWidgetListViewDelegate](../ncwidgetlistviewdelegate.md)
  The interface for handling content display and editing in the list view of a macOS Today widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetlistviewcontroller/delegate)*
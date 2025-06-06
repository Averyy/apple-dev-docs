# delegate

**Framework**: AppKit  
**Kind**: property

The table view’s delegate.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
weak var delegate: (any NSTableViewDelegate)? { get set }
```

#### Discussion

The delegate must conform to the [`NSTableViewDelegate`](nstableviewdelegate.md) protocol. Setting the delegate will implicitly reload the table view. Note that in versions of macOS prior to v10.12, the table view did not retain the delegate in a managed memory environment.

##### Special Considerations

When you set the table view’s delegate, it is automatically registered for the following notifications with the following delegate methods:

- The notification named [`selectionDidChangeNotification`](nstableview/selectiondidchangenotification.md) is configured to notify the delegate’s [`tableViewSelectionDidChange(_:)`](nstableviewdelegate/tableviewselectiondidchange(_:).md).
- The notification named [`columnDidMoveNotification`](nstableview/columndidmovenotification.md) is configured to notify the delegate’s [`tableViewColumnDidMove(_:)`](nstableviewdelegate/tableviewcolumndidmove(_:).md).
- The notification named [`columnDidResizeNotification`](nstableview/columndidresizenotification.md) is configured to notify the delegate’s [`tableViewColumnDidResize(_:)`](nstableviewdelegate/tableviewcolumndidresize(_:).md).
- The notification named [`selectionIsChangingNotification`](nstableview/selectionischangingnotification.md) is configured to notify the delegate’s [`tableViewSelectionIsChanging(_:)`](nstableviewdelegate/tableviewselectionischanging(_:).md).

Setting the delegate to `nil` causes these notifications to be disconnected. Rather than setting the delegate to `nil` and listening for notifications (and expecting `NSTableView` to still function correctly) you should instead implement the appropriate delegate method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/delegate)*
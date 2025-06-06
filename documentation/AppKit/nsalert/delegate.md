# delegate

**Framework**: AppKit  
**Kind**: property

The alert’s delegate.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
weak var delegate: (any NSAlertDelegate)? { get set }
```

#### Discussion

To set a delegate for the alert, provide an object conforming to the [`NSAlertDelegate`](nsalertdelegate.md)protocol to this property. To remove the delegate, set this property’s value to `nil`.

## See Also

- [func layout()](nsalert/layout.md)
  Specifies that the alert must do immediate layout instead of lazily just before display.
- [var alertStyle: NSAlert.Style](nsalert/alertstyle.md)
  Indicates the alert’s severity level.
- [var accessoryView: NSView?](nsalert/accessoryview.md)
  The alert’s accessory view.
- [var showsHelp: Bool](nsalert/showshelp.md)
  Specifies whether the alert has a help button.
- [var helpAnchor: NSHelpManager.AnchorName?](nsalert/helpanchor.md)
  The alert’s HTML help anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalert/delegate)*
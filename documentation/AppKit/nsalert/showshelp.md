# showsHelp

**Framework**: AppKit  
**Kind**: property

Specifies whether the alert has a help button.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var showsHelp: Bool { get set }
```

#### Discussion

Set this property’s value to [`true`](https://developer.apple.com/documentation/swift/true) to specify that the alert has a help button, or [`false`](https://developer.apple.com/documentation/swift/false) to specify it does not.

When a user clicks an alert’s help button, the alert delegate ([`delegate`](nsalert/delegate.md)) receives an [`alertShowHelp(_:)`](nsalertdelegate/alertshowhelp(_:).md) message. The delegate is responsible for displaying the help information related to this particular alert.

Clicking an alert’s help button can alternately cause the [`openHelpAnchor(_:inBook:)`](nshelpmanager/openhelpanchor(_:inbook:).md) message to be sent to the app’s help manager with a `nil` book and the anchor specified by the [`helpAnchor`](nsalert/helpanchor.md) property, if any of the following conditions are true:

- There is no alert delegate.
- The alert delegate does not implement [`alertShowHelp(_:)`](nsalertdelegate/alertshowhelp(_:).md).
- The alert delegate implements [`alertShowHelp(_:)`](nsalertdelegate/alertshowhelp(_:).md) but returns [`false`](https://developer.apple.com/documentation/swift/false). When this is the case, an exception is raised if no help anchor is set.

## See Also

- [func layout()](nsalert/layout.md)
  Specifies that the alert must do immediate layout instead of lazily just before display.
- [var alertStyle: NSAlert.Style](nsalert/alertstyle.md)
  Indicates the alert’s severity level.
- [var accessoryView: NSView?](nsalert/accessoryview.md)
  The alert’s accessory view.
- [var helpAnchor: NSHelpManager.AnchorName?](nsalert/helpanchor.md)
  The alert’s HTML help anchor.
- [var delegate: (any NSAlertDelegate)?](nsalert/delegate.md)
  The alert’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalert/showshelp)*
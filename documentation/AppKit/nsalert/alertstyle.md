# alertStyle

**Framework**: AppKit  
**Kind**: property

Indicates the alert’s severity level.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var alertStyle: NSAlert.Style { get set }
```

#### Discussion

See the [`NSAlert.Style`](nsalert/style.md) enumeration for the list of alert style constants.

## See Also

- [func layout()](nsalert/layout.md)
  Specifies that the alert must do immediate layout instead of lazily just before display.
- [var accessoryView: NSView?](nsalert/accessoryview.md)
  The alert’s accessory view.
- [var showsHelp: Bool](nsalert/showshelp.md)
  Specifies whether the alert has a help button.
- [var helpAnchor: NSHelpManager.AnchorName?](nsalert/helpanchor.md)
  The alert’s HTML help anchor.
- [var delegate: (any NSAlertDelegate)?](nsalert/delegate.md)
  The alert’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalert/alertstyle)*
# helpAnchor

**Framework**: AppKit  
**Kind**: property

The alert’s HTML help anchor.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var helpAnchor: NSHelpManager.AnchorName? { get set }
```

#### Discussion

To provide a help anchor for the alert, set this property to the appropriate string value. To remove the help anchor, set this property’s value to `nil`.

## See Also

- [func layout()](nsalert/layout.md)
  Specifies that the alert must do immediate layout instead of lazily just before display.
- [var alertStyle: NSAlert.Style](nsalert/alertstyle.md)
  Indicates the alert’s severity level.
- [var accessoryView: NSView?](nsalert/accessoryview.md)
  The alert’s accessory view.
- [var showsHelp: Bool](nsalert/showshelp.md)
  Specifies whether the alert has a help button.
- [var delegate: (any NSAlertDelegate)?](nsalert/delegate.md)
  The alert’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalert/helpanchor)*
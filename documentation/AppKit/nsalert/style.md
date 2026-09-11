# NSAlert.Style

**Framework**: AppKit  
**Kind**: enum

The set of alert styles to style alerts in your app.

**Availability**:
- macOS ?+

## Declaration

```swift
enum Style
```

#### Overview

Currently, there’s no visual difference between informational and warning alerts. You should only use the critical (or “caution”) alert style if warranted. For design guidance on alert styles, see [`Human Interface Guidelines > Alerts`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/alerts#macOS). The default alert style is [`NSAlert.Style.warning`](nsalert/style/warning.md).

## Topics

### Enumeration Cases
- [NSAlert.Style.critical](nsalert/style/critical.md)
  An alert style to inform someone about a critical event.
- [NSAlert.Style.warning](nsalert/style/warning.md)
  An alert style to warn someone about a current or impending event.
- [NSAlert.Style.informational](nsalert/style/informational.md)
  An alert style to inform someone about a current or impending event.
### Initializers
- [init?(rawValue: UInt)](nsalert/style/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

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
- [var delegate: (any NSAlertDelegate)?](nsalert/delegate.md)
  The alert’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalert/style)*
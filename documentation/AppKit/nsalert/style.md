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
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [NSApplication.ModalResponse](nsapplication/modalresponse.md)
  A set of button return values for modal dialogs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalert/style)*
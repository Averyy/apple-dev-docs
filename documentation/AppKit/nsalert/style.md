# NSAlert.Style

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

The set of alert styles to style alerts in your app.

**Availability**:
- macOS

## Declaration

```swift
enum Style
```

```c
enum NSAlertStyle : NSUInteger;
```

## Overview

Currently, there’s no visual difference between informational and warning alerts. You should only use the critical (or “caution”) alert style if warranted. For design guidance on alert styles, see [Human Interface Guidelines > Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts#macOS). The default alert style is [`NSAlert.Style.warning`](./style/warning.md).

## Topics

### Enumeration Cases
- [NSAlert.Style.critical](./style/critical.md)
  An alert style to inform someone about a critical event.
- [NSAlert.Style.warning](./style/warning.md)
  An alert style to warn someone about a current or impending event.
- [NSAlert.Style.informational](./style/informational.md)
  An alert style to inform someone about a current or impending event.
### Initializers
- [init?(rawValue: UInt)](./style/init%28rawvalue%29.md)
### Deprecated
- [NSCriticalAlertStyle](../nscriticalalertstyle.md)
- [NSWarningAlertStyle](../nswarningalertstyle.md)
  An alert used to warn the user about a current or impending event. The purpose is more than informational but not critical. This is the default alert style.
- [NSInformationalAlertStyle](../nsinformationalalertstyle.md)
  An alert used to inform the user about a current or impending event.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring alerts
- [func layout()](./layout%28%29.md)
  Specifies that the alert must do immediate layout instead of lazily just before display.
- [var alertStyle: NSAlert.Style](./alertstyle.md)
  Indicates the alert’s severity level.
- [var accessoryView: NSView?](./accessoryview.md)
  The alert’s accessory view.
- [var showsHelp: Bool](./showshelp.md)
  Specifies whether the alert has a help button.
- [var helpAnchor: NSHelpManager.AnchorName?](./helpanchor.md)
  The alert’s HTML help anchor.
- [var delegate: (any NSAlertDelegate)?](./delegate.md)
  The alert’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalert/style)*
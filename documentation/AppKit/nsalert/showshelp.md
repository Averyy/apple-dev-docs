# showsHelp

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Specifies whether the alert has a help button.

**Availability**:
- macOS

## Declaration

```swift
var showsHelp: Bool { get set }
```

```objc
@property BOOL showsHelp;
```

## Discussion

Set this property’s value to [`true`](../../Swift/true.md) to specify that the alert has a help button, or [`false`](../../Swift/false.md) to specify it does not.

When a user clicks an alert’s help button, the alert delegate ([`delegate`](./delegate.md)) receives an [`alertShowHelp(_:)`](../nsalertdelegate/alertshowhelp%28_%29.md) message. The delegate is responsible for displaying the help information related to this particular alert.

Clicking an alert’s help button can alternately cause the [`openHelpAnchor(_:inBook:)`](../nshelpmanager/openhelpanchor%28_,inbook%29.md) message to be sent to the app’s help manager with a `nil` book and the anchor specified by the [`helpAnchor`](./helpanchor.md) property, if any of the following conditions are true:

- There is no alert delegate.
- The alert delegate does not implement [`alertShowHelp(_:)`](../nsalertdelegate/alertshowhelp%28_%29.md).
- The alert delegate implements [`alertShowHelp(_:)`](../nsalertdelegate/alertshowhelp%28_%29.md) but returns [`false`](../../Swift/false.md). When this is the case, an exception is raised if no help anchor is set.

## See Also

### Configuring alerts
- [func layout()](./layout%28%29.md)
  Specifies that the alert must do immediate layout instead of lazily just before display.
- [var alertStyle: NSAlert.Style](./alertstyle.md)
  Indicates the alert’s severity level.
- [NSAlert.Style](./style.md)
  The set of alert styles to style alerts in your app.
- [var accessoryView: NSView?](./accessoryview.md)
  The alert’s accessory view.
- [var helpAnchor: NSHelpManager.AnchorName?](./helpanchor.md)
  The alert’s HTML help anchor.
- [var delegate: (any NSAlertDelegate)?](./delegate.md)
  The alert’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalert/showshelp)*
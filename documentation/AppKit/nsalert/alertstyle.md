# alertStyle

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Indicates the alert’s severity level.

**Availability**:
- macOS

## Declaration

```swift
var alertStyle: NSAlert.Style { get set }
```

```objc
@property NSAlertStyle alertStyle;
```

## Discussion

See the [`NSAlert.Style`](./style.md) enumeration for the list of alert style constants.

## See Also

### Configuring alerts
- [func layout()](./layout%28%29.md)
  Specifies that the alert must do immediate layout instead of lazily just before display.
- [NSAlert.Style](./style.md)
  The set of alert styles to style alerts in your app.
- [var accessoryView: NSView?](./accessoryview.md)
  The alert’s accessory view.
- [var showsHelp: Bool](./showshelp.md)
  Specifies whether the alert has a help button.
- [var helpAnchor: NSHelpManager.AnchorName?](./helpanchor.md)
  The alert’s HTML help anchor.
- [var delegate: (any NSAlertDelegate)?](./delegate.md)
  The alert’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalert/alertstyle)*
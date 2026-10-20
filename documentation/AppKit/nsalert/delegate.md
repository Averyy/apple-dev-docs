# delegate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The alert’s delegate.

**Availability**:
- macOS

## Declaration

```swift
weak var delegate: (any NSAlertDelegate)? { get set }
```

```objc
@property (weak, nullable) id<NSAlertDelegate> delegate;
```

#### Discussion

To set a delegate for the alert, provide an object conforming to the [`NSAlertDelegate`](../nsalertdelegate.md)protocol to this property. To remove the delegate, set this property’s value to `nil`.

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
- [var showsHelp: Bool](./showshelp.md)
  Specifies whether the alert has a help button.
- [var helpAnchor: NSHelpManager.AnchorName?](./helpanchor.md)
  The alert’s HTML help anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalert/delegate)*
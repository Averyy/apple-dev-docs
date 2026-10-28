# helpAnchor

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The alert’s HTML help anchor.

**Availability**:
- macOS

## Declaration

```swift
var helpAnchor: NSHelpManager.AnchorName? { get set }
```

```objc
@property (copy, nullable) NSHelpAnchorName helpAnchor;
```

## Discussion

To provide a help anchor for the alert, set this property to the appropriate string value. To remove the help anchor, set this property’s value to `nil`.

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
- [var delegate: (any NSAlertDelegate)?](./delegate.md)
  The alert’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalert/helpanchor)*
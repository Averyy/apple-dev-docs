# layout()

**Framework**: AppKit  
**Kind**: method

Specifies that the alert must do immediate layout instead of lazily just before display.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func layout()
```

#### Discussion

You need to call this method only when you need to customize the alert’s layout. Call this method after all the alert’s attributes have been customized, including the suppression checkbox and the accessory layout. After the method returns, you can make the necessary layout changes; for example, adjusting the frame of the accessory view.

> **Note**:  The standard alert layout is subject to change in future system software versions. Therefore, if you rely on custom alert layout, you should make sure your layouts work as expected in future releases of  macOS.

## See Also

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalert/layout())*
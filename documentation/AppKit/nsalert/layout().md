# layout()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Specifies that the alert must do immediate layout instead of lazily just before display.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func layout()
```

```objc
- (void) layout;
```

#### Discussion

You need to call this method only when you need to customize the alert’s layout. Call this method after all the alert’s attributes have been customized, including the suppression checkbox and the accessory layout. After the method returns, you can make the necessary layout changes; for example, adjusting the frame of the accessory view.

> **Note**:  The standard alert layout is subject to change in future system software versions. Therefore, if you rely on custom alert layout, you should make sure your layouts work as expected in future releases of  macOS.

## See Also

### Configuring alerts
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
- [var delegate: (any NSAlertDelegate)?](./delegate.md)
  The alert’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalert/layout())*
# accessoryView

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The alert’s accessory view.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var accessoryView: NSView? { get set }
```

```objc
@property (strong, nullable) NSView * accessoryView;
```

#### Discussion

The [`NSAlert`](../nsalert.md) class places the accessory view between the informative text or suppression checkbox (if present) and the response buttons. Before you change the location of the accessory view, first call the [`layout()`](./layout%28%29.md) method.

[`alertStyle`](./alertstyle.md) shows an example of adding an accessory view to an alert. [`buttons`](./buttons.md) shows the alert generated.

Listing 1. Adding an accessory view to an alert

```objc
NSTextView *accessory = [[NSTextView alloc] initWithFrame:NSMakeRect(0,0,200,15)];
NSFont *font = [NSFont systemFontOfSize:[NSFont systemFontSize]];
NSDictionary *textAttributes = [NSDictionary dictionaryWithObject:font forKey:NSFontAttributeName];
[accessory insertText:[[NSAttributedString alloc] initWithString:@"Text in accessory view."
                                                      attributes:textAttributes]];
[accessory setEditable:NO];
[accessory setDrawsBackground:NO];
 
NSAlert *alert = [[NSAlert alloc] init];
alert.messageText = @"Message text.";
[alert setInformativeText:@"Informative text."];
alert.accessoryView = accessory;
[alert runModal];
[alert release];
```

![A screenshot of an alert with a document, pencil, and ruler icon on the left. The alert shows the message text, the informative text, and the text from the accessory view below them, followed by an OK button at the bottom right.](https://developer.apple.com/tutorials/images/com.apple.appkit/media-1965585@2x.png)

## See Also

### Configuring alerts
- [func layout()](./layout%28%29.md)
  Specifies that the alert must do immediate layout instead of lazily just before display.
- [var alertStyle: NSAlert.Style](./alertstyle.md)
  Indicates the alert’s severity level.
- [NSAlert.Style](./style.md)
  The set of alert styles to style alerts in your app.
- [var showsHelp: Bool](./showshelp.md)
  Specifies whether the alert has a help button.
- [var helpAnchor: NSHelpManager.AnchorName?](./helpanchor.md)
  The alert’s HTML help anchor.
- [var delegate: (any NSAlertDelegate)?](./delegate.md)
  The alert’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalert/accessoryview)*
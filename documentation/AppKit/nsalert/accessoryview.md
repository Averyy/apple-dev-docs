# accessoryView

**Framework**: AppKit  
**Kind**: property

The alert’s accessory view.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
var accessoryView: NSView? { get set }
```

#### Discussion

The [`NSAlert`](nsalert.md) class places the accessory view between the informative text or suppression checkbox (if present) and the response buttons. Before you change the location of the accessory view, first call the [`layout()`](nsalert/layout().md) method.

[`alertStyle`](nsalert/alertstyle.md) shows an example of adding an accessory view to an alert. [`buttons`](nsalert/buttons.md) shows the alert generated.

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

![None](https://docs-assets.developer.apple.com/published/a66bc4535988ee27489e23008187dfb6/media-1965585%402x.png)

## See Also

- [func layout()](nsalert/layout.md)
  Specifies that the alert must do immediate layout instead of lazily just before display.
- [var alertStyle: NSAlert.Style](nsalert/alertstyle.md)
  Indicates the alert’s severity level.
- [var showsHelp: Bool](nsalert/showshelp.md)
  Specifies whether the alert has a help button.
- [var helpAnchor: NSHelpManager.AnchorName?](nsalert/helpanchor.md)
  The alert’s HTML help anchor.
- [var delegate: (any NSAlertDelegate)?](nsalert/delegate.md)
  The alert’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalert/accessoryview)*
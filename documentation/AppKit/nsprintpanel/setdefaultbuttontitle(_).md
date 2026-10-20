# setDefaultButtonTitle(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the title of the Print panel’s default button.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func setDefaultButtonTitle(_ defaultButtonTitle: String?)
```

```objc
- (void) setDefaultButtonTitle:(NSString *) defaultButtonTitle;
```

#### Discussion

You can use this method to change the default button title from “Print” to something more appropriate for your usage of the panel. For example, if you are using the Print panel to save a representation of the document to a file, you might change the title to “Save”.

## Parameters

- `defaultButtonTitle`: The string to use for the button title.

## See Also

### Customizing the Panel
- [var jobStyleHint: NSPrintPanel.JobStyleHint?](./jobstylehint-swift.property.md)
  The type of settings that the print panel displays.
- [NSPrintPanel.JobStyleHint](./jobstylehint-swift.struct.md)
  Constants that specify job style hints for activating the simplified Print panel interface and setting the options to display.
- [var options: NSPrintPanel.Options](./options-swift.property.md)
  The current configuration options for the Print panel.
- [NSPrintPanel.Options](./options-swift.struct.md)
  Constants that specify options for configuring the contents of the main Print panel.
- [func defaultButtonTitle() -> String?](./defaultbuttontitle%28%29.md)
  Returns the title of the Print panel’s default button.
- [var helpAnchor: NSHelpManager.AnchorName?](./helpanchor.md)
  The HTML help anchor associated with the Print panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintpanel/setdefaultbuttontitle(_:))*
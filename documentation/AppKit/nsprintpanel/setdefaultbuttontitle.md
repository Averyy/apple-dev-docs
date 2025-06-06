# setDefaultButtonTitle(_:)

**Framework**: AppKit  
**Kind**: method

Sets the title of the Print panel’s default button.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func setDefaultButtonTitle(_ defaultButtonTitle: String?)
```

#### Discussion

You can use this method to change the default button title from “Print” to something more appropriate for your usage of the panel. For example, if you are using the Print panel to save a representation of the document to a file, you might change the title to “Save”.

## Parameters

- `defaultButtonTitle`: The string to use for the button title.

## See Also

- [var jobStyleHint: NSPrintPanel.JobStyleHint?](nsprintpanel/jobstylehint-swift.property.md)
  The type of settings that the print panel displays.
- [NSPrintPanel.JobStyleHint](nsprintpanel/jobstylehint-swift.struct.md)
  Constants that specify job style hints for activating the simplified Print panel interface and setting the options to display.
- [var options: NSPrintPanel.Options](nsprintpanel/options-swift.property.md)
  The current configuration options for the Print panel.
- [NSPrintPanel.Options](nsprintpanel/options-swift.struct.md)
  Constants that specify options for configuring the contents of the main Print panel.
- [func defaultButtonTitle() -> String?](nsprintpanel/defaultbuttontitle.md)
  Returns the title of the Print panel’s default button.
- [var helpAnchor: NSHelpManager.AnchorName?](nsprintpanel/helpanchor.md)
  The HTML help anchor associated with the Print panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintpanel/setdefaultbuttontitle(_:))*
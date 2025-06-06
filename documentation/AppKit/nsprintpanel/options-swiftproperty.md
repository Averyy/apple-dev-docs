# options

**Framework**: AppKit  
**Kind**: property

The current configuration options for the Print panel.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
var options: NSPrintPanel.Options { get set }
```

#### Discussion

You can specify multiple options by adding them together. For a list of supported options, see [`NSPrintPanel.Options`](nsprintpanel/options-swift.struct.md).

## See Also

- [var jobStyleHint: NSPrintPanel.JobStyleHint?](nsprintpanel/jobstylehint-swift.property.md)
  The type of settings that the print panel displays.
- [NSPrintPanel.JobStyleHint](nsprintpanel/jobstylehint-swift.struct.md)
  Constants that specify job style hints for activating the simplified Print panel interface and setting the options to display.
- [NSPrintPanel.Options](nsprintpanel/options-swift.struct.md)
  Constants that specify options for configuring the contents of the main Print panel.
- [func defaultButtonTitle() -> String?](nsprintpanel/defaultbuttontitle.md)
  Returns the title of the Print panel’s default button.
- [func setDefaultButtonTitle(String?)](nsprintpanel/setdefaultbuttontitle(_:).md)
  Sets the title of the Print panel’s default button.
- [var helpAnchor: NSHelpManager.AnchorName?](nsprintpanel/helpanchor.md)
  The HTML help anchor associated with the Print panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintpanel/options-swift.property)*
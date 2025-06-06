# helpAnchor

**Framework**: AppKit  
**Kind**: property

The HTML help anchor associated with the Print panel.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
var helpAnchor: NSHelpManager.AnchorName? { get set }
```

#### Discussion

Use this property to specify the anchor name in your Apple Help file. The string you assign should contain only the name portion of the HTML anchor element.

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
- [func setDefaultButtonTitle(String?)](nsprintpanel/setdefaultbuttontitle(_:).md)
  Sets the title of the Print panel’s default button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintpanel/helpanchor)*
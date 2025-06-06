# jobStyleHint

**Framework**: AppKit  
**Kind**: property

The type of settings that the print panel displays.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var jobStyleHint: NSPrintPanel.JobStyleHint? { get set }
```

#### Discussion

This property controls the set of items that appear in the Presets menu of the simplified Print panel interface. For a list of supported job style hints, see `Job Style Hints`. Set this property to `nil` to deactivate the simplified Print panel interface and use the standard interface instead (the equivalent of Core Printing’s `kPMPresetGraphicsTypeGeneral`).

## See Also

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
- [var helpAnchor: NSHelpManager.AnchorName?](nsprintpanel/helpanchor.md)
  The HTML help anchor associated with the Print panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintpanel/jobstylehint-swift.property)*
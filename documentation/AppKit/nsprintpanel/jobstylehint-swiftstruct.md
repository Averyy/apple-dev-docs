# NSPrintPanel.JobStyleHint

**Framework**: AppKit  
**Kind**: struct

Constants that specify job style hints for activating the simplified Print panel interface and setting the options to display.

**Availability**:
- macOS ?+

## Declaration

```swift
struct JobStyleHint
```

## Topics

### Constants
- [static let photo: NSPrintPanel.JobStyleHint](nsprintpanel/jobstylehint-swift.struct/photo.md)
  Output contains photographic data.
- [static let allPresets: NSPrintPanel.JobStyleHint](nsprintpanel/jobstylehint-swift.struct/allpresets.md)
  Output appropriate to all graphics types.
- [static let noPresets: NSPrintPanel.JobStyleHint](nsprintpanel/jobstylehint-swift.struct/nopresets.md)
  Output excludes all graphics printing.
### Initializers
- [init(rawValue: String)](nsprintpanel/jobstylehint-swift.struct/init(rawvalue:).md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var jobStyleHint: NSPrintPanel.JobStyleHint?](nsprintpanel/jobstylehint-swift.property.md)
  The type of settings that the print panel displays.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintpanel/jobstylehint-swift.struct)*
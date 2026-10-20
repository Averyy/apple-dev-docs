# NSPrintPanel.JobStyleHint

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants that specify job style hints for activating the simplified Print panel interface and setting the options to display.

**Availability**:
- macOS

## Declaration

```swift
struct JobStyleHint
```

```c
typedef NSString * NSPrintPanelJobStyleHint;
```

## Topics

### Constants
- [static let photo: NSPrintPanel.JobStyleHint](./jobstylehint-swift.struct/photo.md)
  Output contains photographic data.
- [static let allPresets: NSPrintPanel.JobStyleHint](./jobstylehint-swift.struct/allpresets.md)
  Output appropriate to all graphics types.
- [static let noPresets: NSPrintPanel.JobStyleHint](./jobstylehint-swift.struct/nopresets.md)
  Output excludes all graphics printing.
### Initializers
- [init(rawValue: String)](./jobstylehint-swift.struct/init%28rawvalue%29.md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Customizing the Panel
- [var jobStyleHint: NSPrintPanel.JobStyleHint?](./jobstylehint-swift.property.md)
  The type of settings that the print panel displays.
- [var options: NSPrintPanel.Options](./options-swift.property.md)
  The current configuration options for the Print panel.
- [NSPrintPanel.Options](./options-swift.struct.md)
  Constants that specify options for configuring the contents of the main Print panel.
- [func defaultButtonTitle() -> String?](./defaultbuttontitle%28%29.md)
  Returns the title of the Print panel’s default button.
- [func setDefaultButtonTitle(String?)](./setdefaultbuttontitle%28_%29.md)
  Sets the title of the Print panel’s default button.
- [var helpAnchor: NSHelpManager.AnchorName?](./helpanchor.md)
  The HTML help anchor associated with the Print panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintpanel/jobstylehint-swift.struct)*
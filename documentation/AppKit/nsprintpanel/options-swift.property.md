# options

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The current configuration options for the Print panel.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var options: NSPrintPanel.Options { get set }
```

```objc
@property NSPrintPanelOptions options;
```

#### Discussion

You can specify multiple options by adding them together. For a list of supported options, see [`NSPrintPanel.Options`](./options-swift.struct.md).

## See Also

### Customizing the Panel
- [var jobStyleHint: NSPrintPanel.JobStyleHint?](./jobstylehint-swift.property.md)
  The type of settings that the print panel displays.
- [NSPrintPanel.JobStyleHint](./jobstylehint-swift.struct.md)
  Constants that specify job style hints for activating the simplified Print panel interface and setting the options to display.
- [NSPrintPanel.Options](./options-swift.struct.md)
  Constants that specify options for configuring the contents of the main Print panel.
- [func defaultButtonTitle() -> String?](./defaultbuttontitle%28%29.md)
  Returns the title of the Print panel’s default button.
- [func setDefaultButtonTitle(String?)](./setdefaultbuttontitle%28_%29.md)
  Sets the title of the Print panel’s default button.
- [var helpAnchor: NSHelpManager.AnchorName?](./helpanchor.md)
  The HTML help anchor associated with the Print panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintpanel/options-swift.property)*
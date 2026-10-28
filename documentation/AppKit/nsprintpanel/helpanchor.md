# helpAnchor

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The HTML help anchor associated with the Print panel.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var helpAnchor: NSHelpManager.AnchorName? { get set }
```

```objc
@property (copy, nullable) NSHelpAnchorName helpAnchor;
```

## Discussion

Use this property to specify the anchor name in your Apple Help file. The string you assign should contain only the name portion of the HTML anchor element.

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
- [func setDefaultButtonTitle(String?)](./setdefaultbuttontitle%28_%29.md)
  Sets the title of the Print panel’s default button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintpanel/helpanchor)*
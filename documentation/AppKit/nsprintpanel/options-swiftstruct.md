# NSPrintPanel.Options

**Framework**: AppKit  
**Kind**: struct

Constants that specify options for configuring the contents of the main Print panel.

**Availability**:
- macOS 10.5+

## Declaration

```swift
struct Options
```

## Topics

### Constants
- [static var showsCopies: NSPrintPanel.Options](nsprintpanel/options-swift.struct/showscopies.md)
  The Print panel includes a field for manipulating the number of copies being printed.
- [static var showsPageRange: NSPrintPanel.Options](nsprintpanel/options-swift.struct/showspagerange.md)
  The Print panel includes a set of fields for manipulating the range of pages being printed.
- [static var showsPaperSize: NSPrintPanel.Options](nsprintpanel/options-swift.struct/showspapersize.md)
  The Print panel includes a control for manipulating the paper size of the printer.
- [static var showsOrientation: NSPrintPanel.Options](nsprintpanel/options-swift.struct/showsorientation.md)
  The Print panel includes a control for manipulating the page orientation.
- [static var showsScaling: NSPrintPanel.Options](nsprintpanel/options-swift.struct/showsscaling.md)
  The Print panel includes a control for scaling the printed output.
- [static var showsPrintSelection: NSPrintPanel.Options](nsprintpanel/options-swift.struct/showsprintselection.md)
  The Print panel includes an additional selection option for paper range.
- [static var showsPageSetupAccessory: NSPrintPanel.Options](nsprintpanel/options-swift.struct/showspagesetupaccessory.md)
  The Print panel includes a separate accessory view for manipulating the paper size, orientation, and scaling attributes.
- [static var showsPreview: NSPrintPanel.Options](nsprintpanel/options-swift.struct/showspreview.md)
  The Print panel displays a built-in preview of the document contents.
### Initializers
- [init(rawValue: UInt)](nsprintpanel/options-swift.struct/init(rawvalue:).md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var jobStyleHint: NSPrintPanel.JobStyleHint?](nsprintpanel/jobstylehint-swift.property.md)
  The type of settings that the print panel displays.
- [NSPrintPanel.JobStyleHint](nsprintpanel/jobstylehint-swift.struct.md)
  Constants that specify job style hints for activating the simplified Print panel interface and setting the options to display.
- [var options: NSPrintPanel.Options](nsprintpanel/options-swift.property.md)
  The current configuration options for the Print panel.
- [func defaultButtonTitle() -> String?](nsprintpanel/defaultbuttontitle.md)
  Returns the title of the Print panel’s default button.
- [func setDefaultButtonTitle(String?)](nsprintpanel/setdefaultbuttontitle(_:).md)
  Sets the title of the Print panel’s default button.
- [var helpAnchor: NSHelpManager.AnchorName?](nsprintpanel/helpanchor.md)
  The HTML help anchor associated with the Print panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintpanel/options-swift.struct)*
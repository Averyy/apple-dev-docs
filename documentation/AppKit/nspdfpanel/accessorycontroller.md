# accessoryController

**Framework**: AppKit  
**Kind**: property

A view controller for the accessory view that the panel can present.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
var accessoryController: NSViewController? { get set }
```

#### Discussion

The PDF panel passes an [`NSPDFInfo`](nspdfinfo.md) object to the accessory view controller to display the various attributes associated with the PDF file. Unlike a print panel (that is, an [`NSPrintPanel`](nsprintpanel.md) object), a PDF panel can have only one accessory view.

## See Also

- [var options: NSPDFPanel.Options](nspdfpanel/options-swift.property.md)
  A set of configuration options that determine the accessory views the PDF panel should display.
- [var defaultFileName: String](nspdfpanel/defaultfilename.md)
  The initial value for the user-editable filename shown in the name field of the PDF panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspdfpanel/accessorycontroller)*
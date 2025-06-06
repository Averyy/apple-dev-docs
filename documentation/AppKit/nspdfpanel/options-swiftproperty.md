# options

**Framework**: AppKit  
**Kind**: property

A set of configuration options that determine the accessory views the PDF panel should display.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
var options: NSPDFPanel.Options { get set }
```

#### Discussion

You specify a set of options by combining the appropriate constants defined in [`NSPDFPanel.Options`](nspdfpanel/options-swift.struct.md).

## See Also

- [var accessoryController: NSViewController?](nspdfpanel/accessorycontroller.md)
  A view controller for the accessory view that the panel can present.
- [var defaultFileName: String](nspdfpanel/defaultfilename.md)
  The initial value for the user-editable filename shown in the name field of the PDF panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspdfpanel/options-swift.property)*
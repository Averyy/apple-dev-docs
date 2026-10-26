# printPanel

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The print panel object to use during the operation.

**Availability**:
- macOS

## Declaration

```swift
var printPanel: NSPrintPanel { get set }
```

```objc
@property (strong) NSPrintPanel * printPanel;
```

## Parameters

- `panel`: The print panel object to use for the operation.

## See Also

### Modifying the User Interface
- [var showsPrintPanel: Bool](./showsprintpanel.md)
  A Boolean value that determines whether the print operation displays a print panel.
- [var showsProgressPanel: Bool](./showsprogresspanel.md)
  A Boolean value that determines whether the print operation displays a progress panel.
- [var jobTitle: String?](./jobtitle.md)
  The custom title of the print job.
- [var pdfPanel: NSPDFPanel](./pdfpanel.md)
  The PDF panel object to use during the operation.
### Related Documentation
- [- showPanels](./showpanels.md)
  Returns a Boolean value that indicates whether the print panel is to be displayed.
- [- accessoryView](./accessoryview.md)
  Returns the accessory view used by the print operation’s print panel.
- [- setAccessoryView:](./setaccessoryview_.md)
  Sets the custom accessory view to be displayed by the print operation’s print panel.
- [- setShowPanels:](./setshowpanels_.md)
  Sets whether the print operation should display a print panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintoperation/printpanel)*
# showsPreview

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The Print panel displays a built-in preview of the document contents.

**Availability**:
- macOS 10.5+

## Declaration

```swift
static var showsPreview: NSPrintPanel.Options { get }
```

```c
NSPrintPanelShowsPreview
```

## Discussion

This option is only appropriate when the Print panel is used in conjunction with an [`NSPrintOperation`](../../nsprintoperation.md) object to print a document.

## See Also

### Constants
- [static var showsCopies: NSPrintPanel.Options](./showscopies.md)
  The Print panel includes a field for manipulating the number of copies being printed.
- [static var showsPageRange: NSPrintPanel.Options](./showspagerange.md)
  The Print panel includes a set of fields for manipulating the range of pages being printed.
- [static var showsPaperSize: NSPrintPanel.Options](./showspapersize.md)
  The Print panel includes a control for manipulating the paper size of the printer.
- [static var showsOrientation: NSPrintPanel.Options](./showsorientation.md)
  The Print panel includes a control for manipulating the page orientation.
- [static var showsScaling: NSPrintPanel.Options](./showsscaling.md)
  The Print panel includes a control for scaling the printed output.
- [static var showsPrintSelection: NSPrintPanel.Options](./showsprintselection.md)
  The Print panel includes an additional selection option for paper range.
- [static var showsPageSetupAccessory: NSPrintPanel.Options](./showspagesetupaccessory.md)
  The Print panel includes a separate accessory view for manipulating the paper size, orientation, and scaling attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintpanel/options-swift.struct/showspreview)*
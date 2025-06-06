# showsProgressPanel

**Framework**: AppKit  
**Kind**: property

A Boolean value that determines whether the print operation displays a progress panel.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var showsProgressPanel: Bool { get set }
```

#### Discussion

This method does not affect the display of a print panel; that operation is controlled by the [`showsPrintPanel`](nsprintoperation/showsprintpanel.md) method.

Operations that generate EPS or PDF data do no display a progress panel, regardless of the value in the `flag` parameter.

## Parameters

- `flag`:   if you want to display a progress panel; otherwise,  .

## See Also

- [var showsPrintPanel: Bool](nsprintoperation/showsprintpanel.md)
  A Boolean value that determines whether the print operation displays a print panel.
- [var jobTitle: String?](nsprintoperation/jobtitle.md)
  The custom title of the print job.
- [var printPanel: NSPrintPanel](nsprintoperation/printpanel.md)
  The print panel object to use during the operation.
- [var pdfPanel: NSPDFPanel](nsprintoperation/pdfpanel.md)
  The PDF panel object to use during the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintoperation/showsprogresspanel)*
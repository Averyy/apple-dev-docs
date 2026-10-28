# showsPrintPanel

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the print operation displays a print panel.

**Availability**:
- macOS

## Declaration

```swift
var showsPrintPanel: Bool { get set }
```

```objc
@property BOOL showsPrintPanel;
```

## Discussion

This method does not affect the display of a progress panel; that operation is controlled by the [`showsProgressPanel`](./showsprogresspanel.md) method.

Operations that generate EPS or PDF data do no display a progress panel, regardless of the value in the `flag` parameter.

## Parameters

- `flag`: [`true`](../../Swift/true.md) if you want to display a print panel; otherwise, [`false`](../../Swift/false.md).

## See Also

### Modifying the User Interface
- [var showsProgressPanel: Bool](./showsprogresspanel.md)
  A Boolean value that determines whether the print operation displays a progress panel.
- [var jobTitle: String?](./jobtitle.md)
  The custom title of the print job.
- [var printPanel: NSPrintPanel](./printpanel.md)
  The print panel object to use during the operation.
- [var pdfPanel: NSPDFPanel](./pdfpanel.md)
  The PDF panel object to use during the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintoperation/showsprintpanel)*
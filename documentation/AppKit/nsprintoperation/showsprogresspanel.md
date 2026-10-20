# showsProgressPanel

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the print operation displays a progress panel.

**Availability**:
- macOS

## Declaration

```swift
var showsProgressPanel: Bool { get set }
```

```objc
@property BOOL showsProgressPanel;
```

#### Discussion

This method does not affect the display of a print panel; that operation is controlled by the [`showsPrintPanel`](./showsprintpanel.md) method.

Operations that generate EPS or PDF data do no display a progress panel, regardless of the value in the `flag` parameter.

## Parameters

- `flag`: [`true`](../../Swift/true.md) if you want to display a progress panel; otherwise, [`false`](../../Swift/false.md).

## See Also

### Modifying the User Interface
- [var showsPrintPanel: Bool](./showsprintpanel.md)
  A Boolean value that determines whether the print operation displays a print panel.
- [var jobTitle: String?](./jobtitle.md)
  The custom title of the print job.
- [var printPanel: NSPrintPanel](./printpanel.md)
  The print panel object to use during the operation.
- [var pdfPanel: NSPDFPanel](./pdfpanel.md)
  The PDF panel object to use during the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintoperation/showsprogresspanel)*
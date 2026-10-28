# jobTitle

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The custom title of the print job.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var jobTitle: String? { get set }
```

```objc
@property (copy, nullable) NSString * jobTitle;
```

## Discussion

Assigning a title with this method overrides the job title provided by the printing view’s [`printJobTitle`](../nsview/printjobtitle.md) method. Specifying `nil` for the `jobTitle` parameter causes the receiver to once again take its title from the printing view.

## Parameters

- `jobTitle`: The print job title. The receiver makes its own copy of the specified string.

## See Also

### Related Documentation
- [var printJobTitle: String](../nsview/printjobtitle.md)
  The view’s print job title.
### Modifying the User Interface
- [var showsPrintPanel: Bool](./showsprintpanel.md)
  A Boolean value that determines whether the print operation displays a print panel.
- [var showsProgressPanel: Bool](./showsprogresspanel.md)
  A Boolean value that determines whether the print operation displays a progress panel.
- [var printPanel: NSPrintPanel](./printpanel.md)
  The print panel object to use during the operation.
- [var pdfPanel: NSPDFPanel](./pdfpanel.md)
  The PDF panel object to use during the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintoperation/jobtitle)*
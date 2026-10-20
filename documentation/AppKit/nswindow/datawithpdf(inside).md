# dataWithPDF(inside:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns PDF data that draws the region of the window within a given rectangle.

**Availability**:
- macOS

## Declaration

```swift
func dataWithPDF(inside rect: NSRect) -> Data
```

```objc
- (NSData *) dataWithPDFInsideRect:(NSRect) rect;
```

#### Return Value

The region in the window (identified by `rect`) as PDF data.

#### Discussion

This data can be placed on a pasteboard, written to a file, or used to create an `NSImage` object.

## Parameters

- `rect`: A rectangle (expressed in the window’s coordinate system) that identifies the region to be expressed as PDF data.

## See Also

### Related Documentation
- [func writePDF(inside: NSRect, to: NSPasteboard)](../nsview/writepdf%28inside,to%29.md)
  Writes PDF data that draws the region of the view within a specified rectangle onto a pasteboard.
- [func dataWithPDF(inside: NSRect) -> Data](../nsview/datawithpdf%28inside%29.md)
  Returns PDF data that draws the region of the view within a specified rectangle.
### Printing Windows
- [func printWindow(Any?)](./printwindow%28_%29.md)
  Runs the Print panel, and if the user chooses an option other than canceling, prints the window (its frame view and all subviews).
- [func dataWithEPS(inside: NSRect) -> Data](./datawitheps%28inside%29.md)
  Returns EPS data that draws the region of the window within a given rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/datawithpdf(inside:))*
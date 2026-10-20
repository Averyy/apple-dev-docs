# dataWithEPS(inside:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns EPS data that draws the region of the window within a given rectangle.

**Availability**:
- macOS

## Declaration

```swift
func dataWithEPS(inside rect: NSRect) -> Data
```

```objc
- (NSData *) dataWithEPSInsideRect:(NSRect) rect;
```

#### Return Value

The region in the window (identified by `rect`) as EPS data.

#### Discussion

This data can be placed on a pasteboard, written to a file, or used to create an `NSImage` object.

## Parameters

- `rect`: A rectangle (expressed in the window’s coordinate system) that identifies the region to be expressed as EPS data.

## See Also

### Related Documentation
- [func dataWithEPS(inside: NSRect) -> Data](../nsview/datawitheps%28inside%29.md)
  Returns EPS data that draws the region of the view within a specified rectangle.
- [func writeEPS(inside: NSRect, to: NSPasteboard)](../nsview/writeeps%28inside,to%29.md)
  Writes EPS data that draws the region of the view within a specified rectangle onto a pasteboard.
### Printing Windows
- [func printWindow(Any?)](./printwindow%28_%29.md)
  Runs the Print panel, and if the user chooses an option other than canceling, prints the window (its frame view and all subviews).
- [func dataWithPDF(inside: NSRect) -> Data](./datawithpdf%28inside%29.md)
  Returns PDF data that draws the region of the window within a given rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/datawitheps(inside:))*
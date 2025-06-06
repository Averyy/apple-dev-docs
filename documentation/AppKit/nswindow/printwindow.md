# printWindow(_:)

**Framework**: AppKit  
**Kind**: method

Runs the Print panel, and if the user chooses an option other than canceling, prints the window (its frame view and all subviews).

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func printWindow(_ sender: Any?)
```

## Parameters

- `sender`: The message’s sender.

## See Also

- [func dataWithEPS(inside: NSRect) -> Data](nswindow/datawitheps(inside:).md)
  Returns EPS data that draws the region of the window within a given rectangle.
- [func dataWithPDF(inside: NSRect) -> Data](nswindow/datawithpdf(inside:).md)
  Returns PDF data that draws the region of the window within a given rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/printwindow(_:))*
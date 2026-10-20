# printWindow(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Runs the Print panel, and if the user chooses an option other than canceling, prints the window (its frame view and all subviews).

**Availability**:
- macOS

## Declaration

```swift
func printWindow(_ sender: Any?)
```

```objc
- (void) print:(id) sender;
```

## Parameters

- `sender`: The message’s sender.

## See Also

### Printing Windows
- [func dataWithEPS(inside: NSRect) -> Data](./datawitheps%28inside%29.md)
  Returns EPS data that draws the region of the window within a given rectangle.
- [func dataWithPDF(inside: NSRect) -> Data](./datawithpdf%28inside%29.md)
  Returns PDF data that draws the region of the window within a given rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/printwindow(_:))*
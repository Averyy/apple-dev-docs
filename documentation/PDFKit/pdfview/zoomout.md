# zoomOut(_:)

**Framework**: PDFKit  
**Kind**: method

Zooms out by decreasing the scaling factor.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@IBAction
@MainActor func zoomOut(_ sender: Any?)
```

#### Discussion

Each invocation of `zoomOut` divides the scaling factor by the square root of 2.

## See Also

- [func zoomIn(Any?)](pdfview/zoomin(_:).md)
  Zooms in by increasing the scaling factor.
- [var canZoomIn: Bool](pdfview/canzoomin.md)
  Returns a Boolean value indicating whether the user can magnify the view and zoom in.
- [var canZoomOut: Bool](pdfview/canzoomout.md)
  Returns a Boolean value indicating whether the user can view an expanded area and zoom out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/zoomout(_:))*
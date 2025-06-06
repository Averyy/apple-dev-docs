# zoomIn(_:)

**Framework**: PDFKit  
**Kind**: method

Zooms in by increasing the scaling factor.

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
@MainActor func zoomIn(_ sender: Any?)
```

#### Discussion

Each invocation of `zoomIn` muliplies the scaling factor by the square root of 2.

## See Also

- [var canZoomIn: Bool](pdfview/canzoomin.md)
  Returns a Boolean value indicating whether the user can magnify the view and zoom in.
- [func zoomOut(Any?)](pdfview/zoomout(_:).md)
  Zooms out by decreasing the scaling factor.
- [var canZoomOut: Bool](pdfview/canzoomout.md)
  Returns a Boolean value indicating whether the user can view an expanded area and zoom out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/zoomin(_:))*
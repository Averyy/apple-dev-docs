# frameResize(position:directions:)

**Framework**: SwiftUI  
**Kind**: method

The pointer style for resizing a rectangular frame from a specific edge or corner.

**Availability**:
- macOS 15.0+

## Declaration

```swift
static func frameResize(position: FrameResizePosition, directions: FrameResizeDirection.Set = .all) -> PointerStyle
```

## Parameters

- `position`: The position along the perimeter of the frame (its edges   and corners) from which it’s resized.
- `directions`: The directions in which the frame can be resized.

## See Also

- [static let `default`: PointerStyle](pointerstyle/default.md)
  The pointer style that uses the default platform appearance.
- [static let horizontalText: PointerStyle](pointerstyle/horizontaltext.md)
  The pointer style appropriate for selecting or inserting text in a horizontal layout.
- [static let verticalText: PointerStyle](pointerstyle/verticaltext.md)
  The pointer style appropriate for selecting or inserting text in a vertical layout.
- [static let rectSelection: PointerStyle](pointerstyle/rectselection.md)
  The pointer style appropriate for precise rectangular selection, such as selecting a portion of an image or multiple lines of text.
- [static let grabIdle: PointerStyle](pointerstyle/grabidle.md)
  The pointer style appropriate to indicate that dragging to reposition content within specific bounds, such as panning a large image, is possible.
- [static let grabActive: PointerStyle](pointerstyle/grabactive.md)
  The pointer style appropriate for actively dragging to reposition content within specific bounds, such as panning a large image.
- [static let link: PointerStyle](pointerstyle/link.md)
  The pointer style appropriate for content opens a URL link to a webpage, document, or other item when clicked.
- [static let zoomIn: PointerStyle](pointerstyle/zoomin.md)
  The pointer style appropriate to indicate that the content can be zoomed in.
- [static let zoomOut: PointerStyle](pointerstyle/zoomout.md)
  The pointer style appropriate to indicate that the content can be zoomed out.
- [static func columnResize(directions: HorizontalDirection.Set) -> PointerStyle](pointerstyle/columnresize(directions:).md)
  The pointer style for resizing a column, or vertical division.
- [static func rowResize(directions: VerticalDirection.Set) -> PointerStyle](pointerstyle/rowresize(directions:).md)
  The pointer style for resizing a row, or horizontal division.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/pointerstyle/frameresize(position:directions:))*
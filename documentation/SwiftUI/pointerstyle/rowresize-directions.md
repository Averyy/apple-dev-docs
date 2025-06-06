# rowResize(directions:)

**Framework**: SwiftUI  
**Kind**: method

The pointer style for resizing a row, or horizontal division.

**Availability**:
- macOS 15.0+

## Declaration

```swift
static func rowResize(directions: VerticalDirection.Set) -> PointerStyle
```

#### Discussion

You may apply this pointer style to a single view or a view hierarchy using the [`pointerStyle(_:)`](view/pointerstyle(_:).md) modifier.

## Parameters

- `directions`: The vertical directions in which a row can be   resized.

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
- [static func frameResize(position: FrameResizePosition, directions: FrameResizeDirection.Set) -> PointerStyle](pointerstyle/frameresize(position:directions:).md)
  The pointer style for resizing a rectangular frame from a specific edge or corner.
- [static func columnResize(directions: HorizontalDirection.Set) -> PointerStyle](pointerstyle/columnresize(directions:).md)
  The pointer style for resizing a column, or vertical division.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/pointerstyle/rowresize(directions:))*
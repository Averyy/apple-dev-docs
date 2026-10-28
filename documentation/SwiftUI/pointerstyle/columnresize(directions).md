# columnResize(directions:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

The pointer style for resizing a column, or vertical division.

**Availability**:
- macOS 15.0+

## Declaration

```swift
static func columnResize(directions: HorizontalDirection.Set) -> PointerStyle
```

## Return Value

A pointer style for resizing a column.

## Discussion

You may apply this pointer style to a single view or a view hierarchy using the [`pointerStyle(_:)`](../view/pointerstyle%28_%29.md) modifier.

## Parameters

- `directions`: The horizontal directions in which a column can be resized. This must not be empty.

## See Also

### Getting built-in pointer styles
- [static let `default`: PointerStyle](./default.md)
  The pointer style that uses the default platform appearance.
- [static let horizontalText: PointerStyle](./horizontaltext.md)
  The pointer style appropriate for selecting or inserting text in a horizontal layout.
- [static let verticalText: PointerStyle](./verticaltext.md)
  The pointer style appropriate for selecting or inserting text in a vertical layout.
- [static let rectSelection: PointerStyle](./rectselection.md)
  The pointer style appropriate for precise rectangular selection, such as selecting a portion of an image or multiple lines of text.
- [static let grabIdle: PointerStyle](./grabidle.md)
  The pointer style appropriate to indicate that dragging to reposition content within specific bounds, such as panning a large image, is possible.
- [static let grabActive: PointerStyle](./grabactive.md)
  The pointer style appropriate for actively dragging to reposition content within specific bounds, such as panning a large image.
- [static let link: PointerStyle](./link.md)
  The pointer style appropriate for content opens a URL link to a webpage, document, or other item when clicked.
- [static let zoomIn: PointerStyle](./zoomin.md)
  The pointer style appropriate to indicate that the content can be zoomed in.
- [static let zoomOut: PointerStyle](./zoomout.md)
  The pointer style appropriate to indicate that the content can be zoomed out.
- [static func frameResize(position: FrameResizePosition, directions: FrameResizeDirection.Set) -> PointerStyle](./frameresize%28position,directions%29.md)
  The pointer style for resizing a rectangular frame from a specific edge or corner.
- [static func rowResize(directions: VerticalDirection.Set) -> PointerStyle](./rowresize%28directions%29.md)
  The pointer style for resizing a row, or horizontal division.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/pointerstyle/columnresize(directions:))*
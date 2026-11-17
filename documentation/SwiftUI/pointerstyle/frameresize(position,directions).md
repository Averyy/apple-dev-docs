# frameResize(position:directions:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

The pointer style for resizing a rectangular frame from a specific edge or corner.

**Availability**:
- macOS 15.0+

## Declaration

```swift
static func frameResize(position: FrameResizePosition, directions: FrameResizeDirection.Set = .all) -> PointerStyle
```

## Discussion

The `position` parameter selects the edge or corner of the frame, and the `directions` parameter specifies whether that edge or corner can resize outward, away from the center of the frame, inward, toward the center, or both. The pointer changes to show the allowed directions.

The following table shows the pointer style for each position and set of directions in a left-to-right layout:

| Position | `.outward` | `.inward` | `.all` |
| --- | --- | --- | --- |
| `.top` | ![The bottom edge pointer, resizing inward.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/PointerStyle-frameResize-north@2x.png) | ![The bottom edge pointer, resizing outward.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/PointerStyle-frameResize-south@2x.png) | ![The bottom edge pointer, resizing inward or outward.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/PointerStyle-frameResize-north-south@2x.png) |
| `.leading` | ![The trailing edge pointer, resizing inward.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/PointerStyle-frameResize-west@2x.png) | ![The trailing edge pointer, resizing outward.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/PointerStyle-frameResize-east@2x.png) | ![The trailing edge pointer, resizing inward or outward.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/PointerStyle-frameResize-east-west@2x.png) |
| `.bottom` | ![The bottom edge pointer, resizing outward.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/PointerStyle-frameResize-south@2x.png) | ![The bottom edge pointer, resizing inward.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/PointerStyle-frameResize-north@2x.png) | ![The bottom edge pointer, resizing inward or outward.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/PointerStyle-frameResize-north-south@2x.png) |
| `.trailing` | ![The trailing edge pointer, resizing outward.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/PointerStyle-frameResize-east@2x.png) | ![The trailing edge pointer, resizing inward.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/PointerStyle-frameResize-west@2x.png) | ![The trailing edge pointer, resizing inward or outward.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/PointerStyle-frameResize-east-west@2x.png) |
| `.topLeading` | ![The bottom trailing corner pointer, resizing inward.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/PointerStyle-frameResize-northwest@2x.png) | ![The bottom trailing corner pointer, resizing outward.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/PointerStyle-frameResize-southeast@2x.png) | ![The bottom trailing corner pointer, resizing inward or outward.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/PointerStyle-frameResize-northwest-southeast@2x.png) |
| `.topTrailing` | ![The bottom leading corner pointer, resizing inward.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/PointerStyle-frameResize-northeast@2x.png) | ![The bottom leading corner pointer, resizing outward.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/PointerStyle-frameResize-southwest@2x.png) | ![The bottom leading corner pointer, resizing inward or outward.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/PointerStyle-frameResize-northeast-southwest@2x.png) |
| `.bottomLeading` | ![The bottom leading corner pointer, resizing outward.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/PointerStyle-frameResize-southwest@2x.png) | ![The bottom leading corner pointer, resizing inward.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/PointerStyle-frameResize-northeast@2x.png) | ![The bottom leading corner pointer, resizing inward or outward.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/PointerStyle-frameResize-northeast-southwest@2x.png) |
| `.bottomTrailing` | ![The bottom trailing corner pointer, resizing outward.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/PointerStyle-frameResize-southeast@2x.png) | ![The bottom trailing corner pointer, resizing inward.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/PointerStyle-frameResize-northwest@2x.png) | ![The bottom trailing corner pointer, resizing inward or outward.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/PointerStyle-frameResize-northwest-southeast@2x.png) |

## Parameters

- `position`: The position along the perimeter of the frame (its edges and corners) from which it’s resized.
- `directions`: The directions in which the frame can be resized.

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
- [static func columnResize(directions: HorizontalDirection.Set) -> PointerStyle](./columnresize%28directions%29.md)
  The pointer style for resizing a column, or vertical division.
- [static func rowResize(directions: VerticalDirection.Set) -> PointerStyle](./rowresize%28directions%29.md)
  The pointer style for resizing a row, or horizontal division.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/pointerstyle/frameresize(position:directions:))*
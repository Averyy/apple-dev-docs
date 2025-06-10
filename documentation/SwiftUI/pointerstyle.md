# PointerStyle

**Framework**: SwiftUI  
**Kind**: struct

A style describing the appearance of the pointer (also called a cursor) when it’s hovered over a view.

**Availability**:
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct PointerStyle
```

#### Overview

Use the [`pointerStyle(_:)`](view/pointerstyle(_:).md) view modifier to set a view’s pointer style.

For guidance on choosing an appropriate pointer style, refer to [`Pointing devices`](https://developer.apple.com/design/Human-Interface-Guidelines/pointing-devices) in the Human Interface Guidelines.

## Topics

### Getting built-in pointer styles
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
- [static func rowResize(directions: VerticalDirection.Set) -> PointerStyle](pointerstyle/rowresize(directions:).md)
  The pointer style for resizing a row, or horizontal division.
### Creating custom pointer styles
- [static image(_:hotSpot:)](pointerstyle/image(_:hotspot:).md)
  Initializes a pointer style with a given image and hot spot.
- [static func shape(some Shape, eoFill: Bool, size: CGSize) -> PointerStyle](pointerstyle/shape(_:eofill:size:).md)
  Initializes a pointer style with a given shape.
### Supporting types
- [enum HorizontalDirection](horizontaldirection.md)
  A direction on the horizontal axis.
- [enum VerticalDirection](verticaldirection.md)
  A direction on the horizontal axis.
- [enum FrameResizePosition](frameresizeposition.md)
  The position along the perimeter of a rectangular frame (its edges and corners) from which it’s resized.
- [enum FrameResizeDirection](frameresizedirection.md)
  The direction in which a rectangular frame can be resized.
### Type Properties
- [static let columnResize: PointerStyle](pointerstyle/columnresize.md)
  The pointer style for resizing a column, or vertical division, in either direction.
- [static let rowResize: PointerStyle](pointerstyle/rowresize.md)
  The pointer style for resizing a row, or horizontal division, in either direction.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func pointerStyle(PointerStyle?) -> some View](view/pointerstyle(_:).md)
  Sets the pointer style to display when the pointer is over the view.
- [func pointerVisibility(Visibility) -> some View](view/pointervisibility(_:).md)
  Sets the visibility of the pointer when it’s over the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/pointerstyle)*
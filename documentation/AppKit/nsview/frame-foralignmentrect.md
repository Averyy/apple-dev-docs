# frame(forAlignmentRect:)

**Framework**: AppKit  
**Kind**: method

Returns the view’s frame for a given alignment rectangle.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func frame(forAlignmentRect alignmentRect: NSRect) -> NSRect
```

#### Return Value

The frame for the specified alignment rectangle

#### Discussion

The constraint-based layout system uses alignment rectangles to align views, rather than their frame. This allows custom views to be aligned based on the location of their content while still having a frame that encompasses any ornamentation they need to draw around their content, such as shadows or reflections.

The default implementation returns `alignmentRect` modified by the insets specified by the view’s [`alignmentRectInsets`](nsview/alignmentrectinsets.md) method. Most custom views can override [`alignmentRectInsets`](nsview/alignmentrectinsets.md) to specify the location of their content within their frame. Custom views that require arbitrary transformations can override [`alignmentRect(forFrame:)`](nsview/alignmentrect(forframe:).md) and [`frame(forAlignmentRect:)`](nsview/frame(foralignmentrect:).md) to describe the location of their content. These two methods must always be inverses of each other.

## Parameters

- `alignmentRect`: The alignment rectangle whose corresponding frame is desired.

## See Also

- [func alignmentRect(forFrame: NSRect) -> NSRect](nsview/alignmentrect(forframe:).md)
  Returns the view’s alignment rectangle for a given frame.
- [var alignmentRectInsets: NSEdgeInsets](nsview/alignmentrectinsets.md)
  The insets (in points) from the view’s frame that define its content rectangle.
- [var baselineOffsetFromBottom: CGFloat](nsview/baselineoffsetfrombottom.md)
  The distance (in points) between the bottom of the view’s alignment rectangle and its baseline.
- [var firstBaselineOffsetFromTop: CGFloat](nsview/firstbaselineoffsetfromtop.md)
  The distance (in points) between the top of the view’s alignment rectangle and its topmost baseline.
- [var lastBaselineOffsetFromBottom: CGFloat](nsview/lastbaselineoffsetfrombottom.md)
  The distance (in points) between the bottom of the view’s alignment rectangle and its bottommost baseline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/frame(foralignmentrect:))*
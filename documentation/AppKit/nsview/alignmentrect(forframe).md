# alignmentRect(forFrame:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the view’s alignment rectangle for a given frame.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func alignmentRect(forFrame frame: NSRect) -> NSRect
```

```objc
- (NSRect) alignmentRectForFrame:(NSRect) frame;
```

## Return Value

The alignment rectangle for the specified frame.

## Discussion

The constraint-based layout system uses alignment rectangles to align views, rather than their frame. This allows custom views to be aligned based on the location of their content while still having a frame that encompasses any ornamentation they need to draw around their content, such as shadows or reflections.

The default implementation returns the view’s frame modified by the insets specified by the view’s [`alignmentRectInsets`](./alignmentrectinsets.md) method. Most custom views can override [`alignmentRectInsets`](./alignmentrectinsets.md) to specify the location of their content within their frame. Custom views that require arbitrary transformations can override [`alignmentRect(forFrame:)`](./alignmentrect%28forframe%29.md) and [`frame(forAlignmentRect:)`](./frame%28foralignmentrect%29.md) to describe the location of their content. These two methods must always be inverses of each other.

## Parameters

- `frame`: The frame whose corresponding alignment rectangle is desired.

## See Also

### Aligning Views with Auto Layout
- [func frame(forAlignmentRect: NSRect) -> NSRect](./frame%28foralignmentrect%29.md)
  Returns the view’s frame for a given alignment rectangle.
- [var alignmentRectInsets: NSEdgeInsets](./alignmentrectinsets.md)
  The insets (in points) from the view’s frame that define its content rectangle.
- [var baselineOffsetFromBottom: CGFloat](./baselineoffsetfrombottom.md)
  The distance (in points) between the bottom of the view’s alignment rectangle and its baseline.
- [var firstBaselineOffsetFromTop: CGFloat](./firstbaselineoffsetfromtop.md)
  The distance (in points) between the top of the view’s alignment rectangle and its topmost baseline.
- [var lastBaselineOffsetFromBottom: CGFloat](./lastbaselineoffsetfrombottom.md)
  The distance (in points) between the bottom of the view’s alignment rectangle and its bottommost baseline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/alignmentrect(forframe:))*
# alignmentRectInsets

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The insets (in points) from the view’s frame that define its content rectangle.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var alignmentRectInsets: NSEdgeInsets { get }
```

```objc
@property (readonly) NSEdgeInsets alignmentRectInsets;
```

## Discussion

The default value is an [`NSEdgeInsets`](../../Foundation/nsedgeinsets.md) structure with the value `0` for each component. Custom views that draw ornamentation around their content can override this property and return insets that align with the edges of the content, excluding the ornamentation. This allows the constraint-based layout system to align views based on their content, rather than just their frame.

Custom views whose content location can’t be expressed by a simple set of insets should override [`alignmentRect(forFrame:)`](./alignmentrect%28forframe%29.md) and [`frame(forAlignmentRect:)`](./frame%28foralignmentrect%29.md) to describe their custom transform between alignment rectangle and frame.

## See Also

### Aligning Views with Auto Layout
- [func alignmentRect(forFrame: NSRect) -> NSRect](./alignmentrect%28forframe%29.md)
  Returns the view’s alignment rectangle for a given frame.
- [func frame(forAlignmentRect: NSRect) -> NSRect](./frame%28foralignmentrect%29.md)
  Returns the view’s frame for a given alignment rectangle.
- [var baselineOffsetFromBottom: CGFloat](./baselineoffsetfrombottom.md)
  The distance (in points) between the bottom of the view’s alignment rectangle and its baseline.
- [var firstBaselineOffsetFromTop: CGFloat](./firstbaselineoffsetfromtop.md)
  The distance (in points) between the top of the view’s alignment rectangle and its topmost baseline.
- [var lastBaselineOffsetFromBottom: CGFloat](./lastbaselineoffsetfrombottom.md)
  The distance (in points) between the bottom of the view’s alignment rectangle and its bottommost baseline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/alignmentrectinsets)*
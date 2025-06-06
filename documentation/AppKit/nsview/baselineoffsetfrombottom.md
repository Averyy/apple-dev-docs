# baselineOffsetFromBottom

**Framework**: AppKit  
**Kind**: property

The distance (in points) between the bottom of the view’s alignment rectangle and its baseline.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var baselineOffsetFromBottom: CGFloat { get }
```

#### Discussion

The default value of this property is `0`. For views that contain text or other content whose layout benefits from having a custom baseline, you can override this property and provide the correct distance between the bottom of the view’s alignment rectangle and that baseline.

## See Also

- [func alignmentRect(forFrame: NSRect) -> NSRect](nsview/alignmentrect(forframe:).md)
  Returns the view’s alignment rectangle for a given frame.
- [func frame(forAlignmentRect: NSRect) -> NSRect](nsview/frame(foralignmentrect:).md)
  Returns the view’s frame for a given alignment rectangle.
- [var alignmentRectInsets: NSEdgeInsets](nsview/alignmentrectinsets.md)
  The insets (in points) from the view’s frame that define its content rectangle.
- [var firstBaselineOffsetFromTop: CGFloat](nsview/firstbaselineoffsetfromtop.md)
  The distance (in points) between the top of the view’s alignment rectangle and its topmost baseline.
- [var lastBaselineOffsetFromBottom: CGFloat](nsview/lastbaselineoffsetfrombottom.md)
  The distance (in points) between the bottom of the view’s alignment rectangle and its bottommost baseline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/baselineoffsetfrombottom)*
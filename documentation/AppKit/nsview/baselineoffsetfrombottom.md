# baselineOffsetFromBottom

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The distance (in points) between the bottom of the view’s alignment rectangle and its baseline.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var baselineOffsetFromBottom: CGFloat { get }
```

```objc
@property (readonly) CGFloat baselineOffsetFromBottom;
```

## Discussion

The default value of this property is `0`. For views that contain text or other content whose layout benefits from having a custom baseline, you can override this property and provide the correct distance between the bottom of the view’s alignment rectangle and that baseline.

## See Also

### Aligning Views with Auto Layout
- [func alignmentRect(forFrame: NSRect) -> NSRect](./alignmentrect%28forframe%29.md)
  Returns the view’s alignment rectangle for a given frame.
- [func frame(forAlignmentRect: NSRect) -> NSRect](./frame%28foralignmentrect%29.md)
  Returns the view’s frame for a given alignment rectangle.
- [var alignmentRectInsets: NSEdgeInsets](./alignmentrectinsets.md)
  The insets (in points) from the view’s frame that define its content rectangle.
- [var firstBaselineOffsetFromTop: CGFloat](./firstbaselineoffsetfromtop.md)
  The distance (in points) between the top of the view’s alignment rectangle and its topmost baseline.
- [var lastBaselineOffsetFromBottom: CGFloat](./lastbaselineoffsetfrombottom.md)
  The distance (in points) between the bottom of the view’s alignment rectangle and its bottommost baseline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/baselineoffsetfrombottom)*
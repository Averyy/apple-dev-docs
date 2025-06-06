# drawDivider(in:)

**Framework**: AppKit  
**Kind**: method

Draws a divider between two of the split view’s subviews.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func drawDivider(in rect: NSRect)
```

#### Discussion

If you override this method to use a custom style for the divider, you may need to change the size of the divider.

## Parameters

- `rect`: The entire divider rectangle in the split view’s flipped coordinate system.

## See Also

- [var dividerStyle: NSSplitView.DividerStyle](nssplitview/dividerstyle-swift.property.md)
  The style of divider between views.
- [NSSplitView.DividerStyle](nssplitview/dividerstyle-swift.enum.md)
  Constants that specify the style of the split view’s dividers.
- [var dividerColor: NSColor](nssplitview/dividercolor.md)
  The color of the dividers that the split view draws between subviews.
- [var dividerThickness: CGFloat](nssplitview/dividerthickness.md)
  The thickness of the dividers for the split view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitview/drawdivider(in:))*
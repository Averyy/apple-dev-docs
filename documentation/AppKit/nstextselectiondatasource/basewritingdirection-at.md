# baseWritingDirection(at:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns the base writing direction at the location you specify.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func baseWritingDirection(at location: any NSTextLocation) -> NSTextSelectionNavigation.WritingDirection
```

#### Return Value

The [`NSWritingDirection`](nswritingdirection.md).

## Parameters

- `location`: The location where you want to examine the text’s writing direction.

## See Also

- [NSTextSelectionNavigation.WritingDirection](nstextselectionnavigation/writingdirection.md)
  Values that describe the writing direction inside a text selection.
- [func textLayoutOrientation(at: any NSTextLocation) -> NSTextSelectionNavigation.LayoutOrientation](nstextselectiondatasource/textlayoutorientation(at:).md)
  Returns the layout orientation at the location you specify.
- [NSTextSelectionNavigation.LayoutOrientation](nstextselectionnavigation/layoutorientation.md)
  Values that describe the possible layout orientations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselectiondatasource/basewritingdirection(at:))*
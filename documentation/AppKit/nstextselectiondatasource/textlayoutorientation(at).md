# textLayoutOrientation(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the layout orientation at the location you specify.

**Availability**:
- macOS 12.0+

## Declaration

```swift
optional func textLayoutOrientation(at location: any NSTextLocation) -> NSTextSelectionNavigation.LayoutOrientation
```

```objc
- (NSTextSelectionNavigationLayoutOrientation) textLayoutOrientationAtLocation:(id<NSTextLocation>) location;
```

#### Return Value

Returns an [`NSTextSelectionNavigation.LayoutOrientation`](../nstextselectionnavigation/layoutorientation.md) that describes the orientation of the layout.

## Parameters

- `location`: The location where you want to examine the text’s layout orientation.

## See Also

### Changing the characteristics of the selection
- [func baseWritingDirection(at: any NSTextLocation) -> NSTextSelectionNavigation.WritingDirection](./basewritingdirection%28at%29.md)
  Returns the base writing direction at the location you specify.
- [NSTextSelectionNavigation.WritingDirection](../nstextselectionnavigation/writingdirection.md)
  Values that describe the writing direction inside a text selection.
- [NSTextSelectionNavigation.LayoutOrientation](../nstextselectionnavigation/layoutorientation.md)
  Values that describe the possible layout orientations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselectiondatasource/textlayoutorientation(at:))*
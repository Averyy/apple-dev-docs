# draw(withExpansionFrame:in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Performs custom expansion tool tip drawing.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func draw(withExpansionFrame contentFrame: NSRect, in view: NSView)
```

```objc
- (void) drawWithExpansionFrame:(NSRect) contentFrame inView:(NSView *) view;
```

#### Discussion

Note that the view may be different from the original view in which the text appeared.

## Parameters

- `contentFrame`: The frame in which to draw.
- `view`: The view in which to draw.

## See Also

### Managing Expansion Tool Tips
- [var allowsExpansionToolTips: Bool](./allowsexpansiontooltips.md)
  A Boolean value that indicates whether expansion tool tips are shown when the control is hovered over.
- [func expansionFrame(withFrame: NSRect) -> NSRect](./expansionframe%28withframe%29.md)
  The frame in which a tool tip can be displayed, if needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/draw(withexpansionframe:in:))*
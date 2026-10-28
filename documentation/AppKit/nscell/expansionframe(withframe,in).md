# expansionFrame(withFrame:in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the expansion cell frame for the receiver.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func expansionFrame(withFrame cellFrame: NSRect, in view: NSView) -> NSRect
```

```objc
- (NSRect) expansionFrameWithFrame:(NSRect) cellFrame inView:(NSView *) view;
```

## Return Value

The expansion cell frame for the receiver. If the frame is not too small, return an empty rect ([`NSZeroRect`](../../Foundation/nszerorect.md)), and no expansion tool tip view will be shown.

## Discussion

This method allows the cell to return an expansion cell frame if `cellFrame` is too small for the entire contents in the view. When the mouse is hovered over the cell in certain controls, the full cell contents are shown in a special floating tool tip view. By default, `NSCell` returns `NSZeroRect`, while some subclasses (such as `NSTextFieldCell`) will return the proper frame when required.

## Parameters

- `cellFrame`: The frame for the receiver.
- `view`: The view in which the receiver will be drawn.

## See Also

### Managing Expansion Frames
- [func draw(withExpansionFrame: NSRect, in: NSView)](./draw%28withexpansionframe,in%29.md)
  Instructs the receiver to draw in an expansion frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/expansionframe(withframe:in:))*
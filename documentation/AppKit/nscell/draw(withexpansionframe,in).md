# draw(withExpansionFrame:in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Instructs the receiver to draw in an expansion frame.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func draw(withExpansionFrame cellFrame: NSRect, in view: NSView)
```

```objc
- (void) drawWithExpansionFrame:(NSRect) cellFrame inView:(NSView *) view;
```

## Discussion

This method allows the cell to perform custom expansion tool tip drawing. By default, `NSCell` simply calls [`draw(withFrame:in:)`](./draw%28withframe,in%29.md).

## Parameters

- `cellFrame`: The frame in which to draw.
- `view`: The view in which to draw. This view may be different from the original view that the cell appeared in.

## See Also

### Managing Expansion Frames
- [func expansionFrame(withFrame: NSRect, in: NSView) -> NSRect](./expansionframe%28withframe,in%29.md)
  Returns the expansion cell frame for the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/draw(withexpansionframe:in:))*
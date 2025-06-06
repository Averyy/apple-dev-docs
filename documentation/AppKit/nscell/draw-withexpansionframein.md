# draw(withExpansionFrame:in:)

**Framework**: AppKit  
**Kind**: method

Instructs the receiver to draw in an expansion frame.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func draw(withExpansionFrame cellFrame: NSRect, in view: NSView)
```

#### Discussion

This method allows the cell to perform custom expansion tool tip drawing. By default, `NSCell` simply calls [`draw(withFrame:in:)`](nscell/draw(withframe:in:).md).

## Parameters

- `cellFrame`: The frame in which to draw.
- `view`: The view in which to draw. This view may be different from the original view that the cell appeared in.

## See Also

- [func expansionFrame(withFrame: NSRect, in: NSView) -> NSRect](nscell/expansionframe(withframe:in:).md)
  Returns the expansion cell frame for the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/draw(withexpansionframe:in:))*
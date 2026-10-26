# NSRectClip

**Framework**: AppKit  
**Kind**: func  
**Role**: Function

Modifies the current clipping path by intersecting it with the passed rect.

**Availability**:
- macOS

## Declaration

```c
extern void NSRectClip(NSRect rect);
```

#### Discussion

This function modifies the clipping path permanently. If you need to undo this modification later, you should save the current graphics state before calling this function and restore it once you are done.

A side effect of this function is that it clears the current Quartz 2D drawing path information. If you used Quartz 2D functions to create a drawing path in the current context, and you want to save that path information and use it later, you should transfer it to a [`CGPath`](../CoreGraphics/cgpath.md) opaque type before calling this function. If you are using only Cocoa to do your drawing, this behavior should not affect you.

## Parameters

- `rect`: The rectangle to intersect with the current clipping rectangle.

## See Also

### Clipping Rectangles
- [NSRectClipList](./nsrectcliplist.md)
  Modifies the current clipping path by intersecting it with the passed rect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrectclip)*
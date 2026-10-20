# CGTextDrawingMode.clip

**Framework**: Core Graphics  
**Kind**: case  
**Role**: Case

Specifies to intersect the text with the current clipping path. This mode does not paint the text.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
case clip
```

```c
kCGTextClip
```

## See Also

### Constants
- [CGTextDrawingMode.fill](./fill.md)
  Perform a fill operation on the text.
- [CGTextDrawingMode.stroke](./stroke.md)
  Perform a stroke operation on the text.
- [CGTextDrawingMode.fillStroke](./fillstroke.md)
  Perform fill, then stroke operations on the text.
- [CGTextDrawingMode.invisible](./invisible.md)
  Do not draw the text, but do update the text position.
- [CGTextDrawingMode.fillClip](./fillclip.md)
  Perform a fill operation, then intersect the text with the current clipping path.
- [CGTextDrawingMode.strokeClip](./strokeclip.md)
  Perform a stroke operation, then intersect the text with the current clipping path.
- [CGTextDrawingMode.fillStrokeClip](./fillstrokeclip.md)
  Perform fill then stroke operations, then intersect the text with the current clipping path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgtextdrawingmode/clip)*
# CGDisplayStreamUpdateRectType.dirtyRects

**Framework**: Core Graphics  
**Kind**: case  
**Role**: Case

The union of both rectangles that were redrawn and rectangles that were moved.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
case dirtyRects
```

```c
kCGDisplayStreamUpdateDirtyRects
```

## See Also

### Constants
- [CGDisplayStreamUpdateRectType.refreshedRects](./refreshedrects.md)
  The rectangles for the portions of the display that were redrawn.
- [CGDisplayStreamUpdateRectType.movedRects](./movedrects.md)
  The rectangles for the portions of the display that were simply moved from one part of the display to another.
- [CGDisplayStreamUpdateRectType.reducedDirtyRects](./reduceddirtyrects.md)
  The union is calculated and then simplified. This reduces the number of rectangles returned to your app, but it may report some pixels that were not actually changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdisplaystreamupdaterecttype/dirtyrects)*
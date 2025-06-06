# CGDisplayStreamUpdateRectType.refreshedRects

**Framework**: Core Graphics  
**Kind**: case

The rectangles for the portions of the display that were redrawn.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
case refreshedRects
```

## See Also

- [CGDisplayStreamUpdateRectType.movedRects](cgdisplaystreamupdaterecttype/movedrects.md)
  The rectangles for the portions of the display that were simply moved from one part of the display to another.
- [CGDisplayStreamUpdateRectType.dirtyRects](cgdisplaystreamupdaterecttype/dirtyrects.md)
  The union of both rectangles that were redrawn and rectangles that were moved.
- [CGDisplayStreamUpdateRectType.reducedDirtyRects](cgdisplaystreamupdaterecttype/reduceddirtyrects.md)
  The union is calculated and then simplified. This reduces the number of rectangles returned to your app, but it may report some pixels that were not actually changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdisplaystreamupdaterecttype/refreshedrects)*
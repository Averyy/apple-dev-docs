# CGDisplayStreamUpdateRectType.reducedDirtyRects

**Framework**: Core Graphics  
**Kind**: case

The union is calculated and then simplified. This reduces the number of rectangles returned to your app, but it may report some pixels that were not actually changed.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
case reducedDirtyRects
```

## See Also

- [CGDisplayStreamUpdateRectType.refreshedRects](cgdisplaystreamupdaterecttype/refreshedrects.md)
  The rectangles for the portions of the display that were redrawn.
- [CGDisplayStreamUpdateRectType.movedRects](cgdisplaystreamupdaterecttype/movedrects.md)
  The rectangles for the portions of the display that were simply moved from one part of the display to another.
- [CGDisplayStreamUpdateRectType.dirtyRects](cgdisplaystreamupdaterecttype/dirtyrects.md)
  The union of both rectangles that were redrawn and rectangles that were moved.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdisplaystreamupdaterecttype/reduceddirtyrects)*
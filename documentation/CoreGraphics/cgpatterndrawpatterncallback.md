# CGPatternDrawPatternCallback

**Framework**: Core Graphics  
**Kind**: typealias  
**Role**: Type Alias

Draws a pattern cell.

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
typealias CGPatternDrawPatternCallback = (UnsafeMutableRawPointer?, CGContext) -> Void
```

```c
typedef void (*)(void *, struct CGContext *) CGPatternDrawPatternCallback;
```

## Discussion

When a pattern is used to stroke or fill a graphics path,Quartz calls your custom drawing function at the appropriatetime to draw the pattern cell. The cell should be drawn exactly thesame way each time the drawing function is called.

In a drawing function associated with an uncolored pattern,you should not attempt to set a stroke or fill color or color space—ifyou do so, the result is undefined.

To learn how to associate your drawing function with a Quartzpattern, see [`init(info:bounds:matrix:xStep:yStep:tiling:isColored:callbacks:)`](./cgpattern/init%28info,bounds,matrix,xstep,ystep,tiling,iscolored,callbacks%29.md) and [`CGPatternCallbacks`](./cgpatterncallbacks.md).

## Parameters

- `info`: A generic pointer to private data associated with the pattern. This is the same pointer you supplied to [`init(info:bounds:matrix:xStep:yStep:tiling:isColored:callbacks:)`](./cgpattern/init%28info,bounds,matrix,xstep,ystep,tiling,iscolored,callbacks%29.md).
- `context`: The graphics context for drawing the pattern cell.

## See Also

### Callbacks
- [struct CGPatternCallbacks](./cgpatterncallbacks.md)
  A structure that holds a version and two callback functions for drawing a custom pattern.
- [typealias CGPatternReleaseInfoCallback](./cgpatternreleaseinfocallback.md)
  Release private data or resources associated with the pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpatterndrawpatterncallback)*
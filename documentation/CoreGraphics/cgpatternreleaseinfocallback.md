# CGPatternReleaseInfoCallback

**Framework**: Core Graphics  
**Kind**: typealias

Release private data or resources associated with the pattern.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
typealias CGPatternReleaseInfoCallback = (UnsafeMutableRawPointer?) -> Void
```

#### Discussion

Quartz calls your release function when it frees your pattern object.

To learn how to associate your release function with a Quartz pattern, see [`init(info:bounds:matrix:xStep:yStep:tiling:isColored:callbacks:)`](cgpattern/init(info:bounds:matrix:xstep:ystep:tiling:iscolored:callbacks:).md) and [`CGPatternCallbacks`](cgpatterncallbacks.md).

## Parameters

- `info`: A generic pointer to private data shared among your callback functions. This is the same pointer you supplied to  .

## See Also

- [struct CGPatternCallbacks](cgpatterncallbacks.md)
  A structure that holds a version and two callback functions for drawing a custom pattern.
- [typealias CGPatternDrawPatternCallback](cgpatterndrawpatterncallback.md)
  Draws a pattern cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpatternreleaseinfocallback)*
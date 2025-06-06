# drawPattern

**Framework**: Core Graphics  
**Kind**: property

A pointer to a custom function that draws thepattern. For information about this callback function, see [`CGPatternDrawPatternCallback`](cgpatterndrawpatterncallback.md).

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
var drawPattern: CGPatternDrawPatternCallback?
```

## See Also

- [var releaseInfo: CGPatternReleaseInfoCallback?](cgpatterncallbacks/releaseinfo.md)
  An optional pointer to a custom function that’sinvoked when the pattern is released. [`CGPatternReleaseInfoCallback`](cgpatternreleaseinfocallback.md).
- [var version: UInt32](cgpatterncallbacks/version.md)
  The version of the structure passed in as a parameterto the [`init(info:bounds:matrix:xStep:yStep:tiling:isColored:callbacks:)`](cgpattern/init(info:bounds:matrix:xstep:ystep:tiling:iscolored:callbacks:).md). Forthis version of the structure, you should set this value to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpatterncallbacks/drawpattern)*
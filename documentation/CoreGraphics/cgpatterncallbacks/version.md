# version

**Framework**: Core Graphics  
**Kind**: property

The version of the structure passed in as a parameterto the [`init(info:bounds:matrix:xStep:yStep:tiling:isColored:callbacks:)`](cgpattern/init(info:bounds:matrix:xstep:ystep:tiling:iscolored:callbacks:).md). Forthis version of the structure, you should set this value to zero.

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
var version: UInt32
```

## See Also

- [var drawPattern: CGPatternDrawPatternCallback?](cgpatterncallbacks/drawpattern.md)
  A pointer to a custom function that draws thepattern. For information about this callback function, see [`CGPatternDrawPatternCallback`](cgpatterndrawpatterncallback.md).
- [var releaseInfo: CGPatternReleaseInfoCallback?](cgpatterncallbacks/releaseinfo.md)
  An optional pointer to a custom function that’sinvoked when the pattern is released. [`CGPatternReleaseInfoCallback`](cgpatternreleaseinfocallback.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpatterncallbacks/version)*
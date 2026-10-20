# releaseInfo

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Instance Property

An optional pointer to a custom function that’sinvoked when the pattern is released. [`CGPatternReleaseInfoCallback`](../cgpatternreleaseinfocallback.md).

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
var releaseInfo: CGPatternReleaseInfoCallback?
```

```c
CGPatternReleaseInfoCallback releaseInfo;
```

## See Also

### Instance Properties
- [var drawPattern: CGPatternDrawPatternCallback?](./drawpattern.md)
  A pointer to a custom function that draws thepattern. For information about this callback function, see [`CGPatternDrawPatternCallback`](../cgpatterndrawpatterncallback.md).
- [var version: UInt32](./version.md)
  The version of the structure passed in as a parameterto the [`init(info:bounds:matrix:xStep:yStep:tiling:isColored:callbacks:)`](../cgpattern/init%28info,bounds,matrix,xstep,ystep,tiling,iscolored,callbacks%29.md). Forthis version of the structure, you should set this value to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpatterncallbacks/releaseinfo)*
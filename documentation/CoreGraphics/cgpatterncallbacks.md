# CGPatternCallbacks

**Framework**: Core Graphics  
**Kind**: struct

A structure that holds a version and two callback functions for drawing a custom pattern.

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
struct CGPatternCallbacks
```

#### Overview

You supply a [`CGPatternCallbacks`](cgpatterncallbacks.md) structure to the function [`init(info:bounds:matrix:xStep:yStep:tiling:isColored:callbacks:)`](cgpattern/init(info:bounds:matrix:xstep:ystep:tiling:iscolored:callbacks:).md) to create a data provider for direct access. The functions specified by the [`CGPatternCallbacks`](cgpatterncallbacks.md) structure are responsible for drawing the pattern and for handling the pattern’s memory management.

## Topics

### Initializers
- [init()](cgpatterncallbacks/init.md)
- [init(version: UInt32, drawPattern: CGPatternDrawPatternCallback?, releaseInfo: CGPatternReleaseInfoCallback?)](cgpatterncallbacks/init(version:drawpattern:releaseinfo:).md)
### Instance Properties
- [var drawPattern: CGPatternDrawPatternCallback?](cgpatterncallbacks/drawpattern.md)
  A pointer to a custom function that draws thepattern. For information about this callback function, see [`CGPatternDrawPatternCallback`](cgpatterndrawpatterncallback.md).
- [var releaseInfo: CGPatternReleaseInfoCallback?](cgpatterncallbacks/releaseinfo.md)
  An optional pointer to a custom function that’sinvoked when the pattern is released. [`CGPatternReleaseInfoCallback`](cgpatternreleaseinfocallback.md).
- [var version: UInt32](cgpatterncallbacks/version.md)
  The version of the structure passed in as a parameterto the [`init(info:bounds:matrix:xStep:yStep:tiling:isColored:callbacks:)`](cgpattern/init(info:bounds:matrix:xstep:ystep:tiling:iscolored:callbacks:).md). Forthis version of the structure, you should set this value to zero.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [typealias CGPatternDrawPatternCallback](cgpatterndrawpatterncallback.md)
  Draws a pattern cell.
- [typealias CGPatternReleaseInfoCallback](cgpatternreleaseinfocallback.md)
  Release private data or resources associated with the pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpatterncallbacks)*
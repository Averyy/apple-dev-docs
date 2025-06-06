# init(info:bounds:matrix:xStep:yStep:tiling:isColored:callbacks:)

**Framework**: Core Graphics  
**Kind**: init

Creates a pattern object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(info: UnsafeMutableRawPointer?, bounds: CGRect, matrix: CGAffineTransform, xStep: CGFloat, yStep: CGFloat, tiling: CGPatternTiling, isColored: Bool, callbacks: UnsafePointer<CGPatternCallbacks>)
```

#### Return Value

A new Core Graphics pattern. In Objective-C, you’re responsible for releasing this object using [`CGPatternRelease`](cgpatternrelease.md).

#### Discussion

Core Graphics calls your drawing function at the appropriate timeto draw the pattern cell. A pattern cell must be invariant—thatis, the pattern cell should be drawn exactly the same way each timethe drawing function is called.

The appearance of a pattern cell is unaffected by changesin the graphics state of the context in which the pattern is used.

See [`CGPatternDrawPatternCallback`](cgpatterndrawpatterncallback.md) formore information about pattern drawing functions.

## Parameters

- `info`: A pointer to private storage used by your pattern drawing function, or  . For more information, see the discussion below.
- `bounds`: The bounding box of the pattern cell, specified in pattern space. (Pattern space is an abstract space that maps to the default user space by the transformation matrix you specify with the   parameter.)The drawing done in your pattern drawing function is clipped to this rectangle.
- `matrix`: A matrix that represents a transform from pattern space to the default user space of the context in which the pattern is used. If no transform is needed, pass the identity matrix.
- `xStep`: The horizontal displacement between cells, specified in pattern space. For no additional horizontal space between cells (so that each pattern cells abuts the previous pattern cell in the horizontal direction), pass the width of the pattern cell.
- `yStep`: The vertical displacement between cells, specified in pattern space. For no additional vertical space between cells(so that each pattern cells abuts the previous pattern cell in the vertical direction), pass the height of the pattern cell.
- `tiling`: A   constant that specifies the desired tiling method.
- `isColored`: If you want to draw your pattern using its own intrinsic color, pass  . If you want to draw an uncolored (or masking) pattern that uses the fill or stroke color in the graphics state, pass  .
- `callbacks`: A pointer to a pattern  callback function table—your pattern drawing function is an entry in this table. See   for more information about callback function tables for patterns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpattern/init(info:bounds:matrix:xstep:ystep:tiling:iscolored:callbacks:))*
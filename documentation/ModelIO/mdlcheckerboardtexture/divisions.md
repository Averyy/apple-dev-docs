# divisions

**Framework**: Model I/O  
**Kind**: property

The number of squares along each dimension in the checkerboard pattern.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var divisions: Float { get set }
```

#### Discussion

For example, a value of 2 creates a checkerboard pattern of four squares (a 2 x 2 grid), where the top-left and bottom-right squares use the [`color1`](mdlcheckerboardtexture/color1.md) color and the other two squares use the [`color2`](mdlcheckerboardtexture/color2.md) color. A value of 4 creates a pattern of 16 squares (a 4 x 4 grid), and so on.

Changing the [`divisions`](mdlcheckerboardtexture/divisions.md), [`color1`](mdlcheckerboardtexture/color1.md), or [`color2`](mdlcheckerboardtexture/color2.md) properties invalidates the cache, causing Model I/O to regenerate texel data the next time it is needed.

## See Also

- [var color1: CGColor?](mdlcheckerboardtexture/color1.md)
  The color for half of the squares in the checkerboard pattern.
- [var color2: CGColor?](mdlcheckerboardtexture/color2.md)
  The color for the other half of the squares in the checkerboard pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlcheckerboardtexture/divisions)*
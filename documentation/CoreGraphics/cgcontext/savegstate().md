# saveGState()

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Pushes a copy of the current graphics state onto the graphics state stack for the context.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func saveGState()
```

```c
extern void CGContextSaveGState(CGContextRef c);
```

## Discussion

Each graphics context maintains a stack of graphics states. Note that not all aspects of the current drawing environment are elements of the graphics state. For example, the current path is not considered part of the graphics state and is therefore not saved when you call this function. The graphics state parameters that *are* saved are:

- CTM (current transformation matrix)
- clip region
- image interpolation quality
- line width
- line join
- miter limit
- line cap
- line dash
- flatness
- should anti-alias
- rendering intent
- fill color space
- stroke color space
- fill color
- stroke color
- alpha value
- font
- font size
- character spacing
- text drawing mode
- shadow parameters
- the pattern phase
- the font smoothing parameter
- blend mode

To restore your drawing environment to a previously saved state, you can use [`restoreGState()`](./restoregstate%28%29.md).

## See Also

### Saving and Restoring Graphics State
- [func restoreGState()](./restoregstate%28%29.md)
  Sets the current graphics state to the state most recently saved.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/savegstate())*
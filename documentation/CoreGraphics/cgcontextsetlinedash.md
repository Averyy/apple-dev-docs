# CGContextSetLineDash

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Sets the pattern for dashed lines in a graphics context.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void CGContextSetLineDash(CGContextRef c, CGFloat phase, const CGFloat *lengths, size_t count);
```

## Parameters

- `c`: The graphics context to modify.
- `phase`: A value that specifies how far into the dash pattern the line starts, in units of the user space. For example, passing a value of `3` means the line is drawn with the dash pattern starting at three units from its beginning. Passing a value of `0` draws a line starting with the beginning of a dash pattern.
- `lengths`: An array of values that specify the lengths of the painted segments and unpainted segments, respectively, of the dash pattern—or `NULL` for no dash pattern.

  For example, passing an array with the values `[2,3]` sets a dash pattern that alternates between a 2-user-space-unit-long painted segment and a 3-user-space-unit-long unpainted segment. Passing the values `[1,3,4,2]` sets the pattern to a 1-unit painted segment, a 3-unit unpainted segment, a 4-unit painted segment, and a 2-unit unpainted segment.
- `count`: If the `lengths` parameter specifies an array, pass the number of elements in the array. Otherwise, pass `0`.

## See Also

### Setting Path Drawing Options
- [func setAllowsAntialiasing(Bool)](./cgcontext/setallowsantialiasing%28_%29.md)
  Sets whether or not to allow antialiasing for a graphics context.
- [func setFlatness(CGFloat)](./cgcontext/setflatness%28_%29.md)
  Sets the accuracy of curved paths in a graphics context.
- [func setLineCap(CGLineCap)](./cgcontext/setlinecap%28_%29.md)
  Sets the style for the endpoints of lines drawn in a graphics context.
- [func setLineJoin(CGLineJoin)](./cgcontext/setlinejoin%28_%29.md)
  Sets the style for the joins of connected lines in a graphics context.
- [func setLineWidth(CGFloat)](./cgcontext/setlinewidth%28_%29.md)
  Sets the line width for a graphics context.
- [func setMiterLimit(CGFloat)](./cgcontext/setmiterlimit%28_%29.md)
  Sets the miter limit for the joins of connected lines in a graphics context.
- [func setPatternPhase(CGSize)](./cgcontext/setpatternphase%28_%29.md)
  Sets the pattern phase of a context.
- [func setFillPattern(CGPattern, colorComponents: UnsafePointer<CGFloat>)](./cgcontext/setfillpattern%28_,colorcomponents%29.md)
  Sets the fill pattern in the specified graphics context.
- [func setShouldAntialias(Bool)](./cgcontext/setshouldantialias%28_%29.md)
  Sets antialiasing on or off for a graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontextsetlinedash)*
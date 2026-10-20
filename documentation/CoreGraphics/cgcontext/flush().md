# flush()

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Forces all pending drawing operations in a window context to be rendered immediately to the destination device.

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
func flush()
```

```c
extern void CGContextFlush(CGContextRef c);
```

#### Discussion

When you call this function, Core Graphics immediately flushes the current drawing to the destination device (for example, a screen). Because the system software flushes a context automatically at the appropriate times, calling this function could have an adverse effect on performance. Under normal conditions, you do not need to call this function.

## See Also

### Managing a Graphics Context
- [func synchronize()](./synchronize%28%29.md)
  Marks a window context for update.
- [func setBlendMode(CGBlendMode)](./setblendmode%28_%29.md)
  Sets how sample values are composited by a graphics context.
- [enum CGBlendMode](../cgblendmode.md)
  Compositing operations for images.
- [func setRenderingIntent(CGColorRenderingIntent)](./setrenderingintent%28_%29.md)
  Sets the rendering intent in the current graphics state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/flush())*
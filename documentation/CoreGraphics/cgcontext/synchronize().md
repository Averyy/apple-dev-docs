# synchronize()

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Marks a window context for update.

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
func synchronize()
```

```c
extern void CGContextSynchronize(CGContextRef c);
```

## Discussion

When you call this function, all drawing operations since the last update are flushed at the next regular opportunity. Under normal conditions, you do not need to call this function.

## See Also

### Managing a Graphics Context
- [func flush()](./flush%28%29.md)
  Forces all pending drawing operations in a window context to be rendered immediately to the destination device.
- [func setBlendMode(CGBlendMode)](./setblendmode%28_%29.md)
  Sets how sample values are composited by a graphics context.
- [enum CGBlendMode](../cgblendmode.md)
  Compositing operations for images.
- [func setRenderingIntent(CGColorRenderingIntent)](./setrenderingintent%28_%29.md)
  Sets the rendering intent in the current graphics state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/synchronize())*
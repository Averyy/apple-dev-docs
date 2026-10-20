# setBlendMode(_:)

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Sets how sample values are composited by a graphics context.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func setBlendMode(_ mode: CGBlendMode)
```

```c
extern void CGContextSetBlendMode(CGContextRef c, CGBlendMode mode);
```

## Parameters

- `mode`: A blend mode. See [`CGBlendMode`](../cgblendmode.md) for a list of the constants you can supply.

## See Also

### Managing a Graphics Context
- [func flush()](./flush%28%29.md)
  Forces all pending drawing operations in a window context to be rendered immediately to the destination device.
- [func synchronize()](./synchronize%28%29.md)
  Marks a window context for update.
- [enum CGBlendMode](../cgblendmode.md)
  Compositing operations for images.
- [func setRenderingIntent(CGColorRenderingIntent)](./setrenderingintent%28_%29.md)
  Sets the rendering intent in the current graphics state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/setblendmode(_:))*
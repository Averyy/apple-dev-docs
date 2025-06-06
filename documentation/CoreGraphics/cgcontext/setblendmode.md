# setBlendMode(_:)

**Framework**: Core Graphics  
**Kind**: method

Sets how sample values are composited by a graphics context.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func setBlendMode(_ mode: CGBlendMode)
```

## Parameters

- `mode`: A blend mode. See   for a list of the constants you can supply.

## See Also

- [func flush()](cgcontext/flush.md)
  Forces all pending drawing operations in a window context to be rendered immediately to the destination device.
- [func synchronize()](cgcontext/synchronize.md)
  Marks a window context for update.
- [enum CGBlendMode](cgblendmode.md)
  Compositing operations for images.
- [func setRenderingIntent(CGColorRenderingIntent)](cgcontext/setrenderingintent(_:).md)
  Sets the rendering intent in the current graphics state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/setblendmode(_:))*
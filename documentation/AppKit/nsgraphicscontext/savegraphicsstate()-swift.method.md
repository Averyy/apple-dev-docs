# saveGraphicsState()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Saves the current graphics state and creates a new graphics state on the top of the stack.

**Availability**:
- macOS

## Declaration

```swift
func saveGraphicsState()
```

```objc
- (void) saveGraphicsState;
```

## Discussion

The new graphics state is a copy of the previous state that can be modified to handle new drawing operations.

Saving the graphics state saves such attributes as the current drawing style, transformation matrix, color, and font. To set drawing style attributes, use the methods of [`NSBezierPath`](../nsbezierpath.md). Other attributes are accessed through appropriate objects such as [`NSAffineTransform`](../../Foundation/nsaffinetransform.md), [`NSColor`](../nscolor.md), and [`NSFont`](../nsfont.md).

## See Also

### Managing the Graphics State
- [class func restoreGraphicsState()](./restoregraphicsstate%28%29-swift.type.method.md)
  Pops a graphics context from the per-thread stack, makes it current, and sends the context a restore graphics state message.
- [func restoreGraphicsState()](./restoregraphicsstate%28%29-swift.method.md)
  Removes the context’s graphics state from the top of the graphics state stack and makes the next graphics state the current graphics state.
- [class func saveGraphicsState()](./savegraphicsstate%28%29-swift.type.method.md)
  Saves the graphics state of the current graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/savegraphicsstate()-swift.method)*
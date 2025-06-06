# restoreGraphicsState()

**Framework**: AppKit  
**Kind**: method

Removes the context’s graphics state from the top of the graphics state stack and makes the next graphics state the current graphics state.

**Availability**:
- macOS ?+

## Declaration

```swift
func restoreGraphicsState()
```

#### Discussion

This method must have been preceded with a [`saveGraphicsState()`](nsgraphicscontext/savegraphicsstate()-swift.method.md) message to add the graphics state to the stack. Invocations of [`saveGraphicsState()`](nsgraphicscontext/savegraphicsstate()-swift.method.md) and [`restoreGraphicsState()`](nsgraphicscontext/restoregraphicsstate()-swift.method.md) methods may be nested.

Restoring the graphics state restores such attributes as the current drawing style, transformation matrix, color, and font of the original graphics state.

## See Also

- [class func restoreGraphicsState()](nsgraphicscontext/restoregraphicsstate-swift.type.method.md)
  Pops a graphics context from the per-thread stack, makes it current, and sends the context a restore graphics state message.
- [class func saveGraphicsState()](nsgraphicscontext/savegraphicsstate-swift.type.method.md)
  Saves the graphics state of the current graphics context.
- [func saveGraphicsState()](nsgraphicscontext/savegraphicsstate-swift.method.md)
  Saves the current graphics state and creates a new graphics state on the top of the stack.
- [class func setGraphicsState(Int)](nsgraphicscontext/setgraphicsstate(_:).md)
  Makes the graphics context of the specified graphics state current, and resets graphics state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/restoregraphicsstate()-swift.method)*
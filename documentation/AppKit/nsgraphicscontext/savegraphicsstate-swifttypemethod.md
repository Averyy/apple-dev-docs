# saveGraphicsState()

**Framework**: AppKit  
**Kind**: method

Saves the graphics state of the current graphics context.

**Availability**:
- macOS ?+

## Declaration

```swift
class func saveGraphicsState()
```

#### Discussion

This method sends the current graphics context a [`saveGraphicsState()`](nsgraphicscontext/savegraphicsstate()-swift.method.md) message and pushes the context onto the per-thread stack.

## See Also

- [class func restoreGraphicsState()](nsgraphicscontext/restoregraphicsstate-swift.type.method.md)
  Pops a graphics context from the per-thread stack, makes it current, and sends the context a restore graphics state message.
- [func restoreGraphicsState()](nsgraphicscontext/restoregraphicsstate-swift.method.md)
  Removes the context’s graphics state from the top of the graphics state stack and makes the next graphics state the current graphics state.
- [func saveGraphicsState()](nsgraphicscontext/savegraphicsstate-swift.method.md)
  Saves the current graphics state and creates a new graphics state on the top of the stack.
- [class func setGraphicsState(Int)](nsgraphicscontext/setgraphicsstate(_:).md)
  Makes the graphics context of the specified graphics state current, and resets graphics state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/savegraphicsstate()-swift.type.method)*
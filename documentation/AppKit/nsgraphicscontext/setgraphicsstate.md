# setGraphicsState(_:)

**Framework**: AppKit  
**Kind**: method

Makes the graphics context of the specified graphics state current, and resets graphics state.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class func setGraphicsState(_ gState: Int)
```

#### Discussion

The `graphicState` identifier must be created in the calling thread.

## See Also

- [class func restoreGraphicsState()](nsgraphicscontext/restoregraphicsstate-swift.type.method.md)
  Pops a graphics context from the per-thread stack, makes it current, and sends the context a restore graphics state message.
- [func restoreGraphicsState()](nsgraphicscontext/restoregraphicsstate-swift.method.md)
  Removes the context’s graphics state from the top of the graphics state stack and makes the next graphics state the current graphics state.
- [class func saveGraphicsState()](nsgraphicscontext/savegraphicsstate-swift.type.method.md)
  Saves the graphics state of the current graphics context.
- [func saveGraphicsState()](nsgraphicscontext/savegraphicsstate-swift.method.md)
  Saves the current graphics state and creates a new graphics state on the top of the stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/setgraphicsstate(_:))*
# saveGraphicsState()

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Saves the graphics state of the current graphics context.

**Availability**:
- macOS

## Declaration

```swift
class func saveGraphicsState()
```

```objc
+ (void) saveGraphicsState;
```

#### Discussion

This method sends the current graphics context a [`saveGraphicsState()`](./savegraphicsstate%28%29-swift.method.md) message and pushes the context onto the per-thread stack.

## See Also

### Managing the Graphics State
- [class func restoreGraphicsState()](./restoregraphicsstate%28%29-swift.type.method.md)
  Pops a graphics context from the per-thread stack, makes it current, and sends the context a restore graphics state message.
- [func restoreGraphicsState()](./restoregraphicsstate%28%29-swift.method.md)
  Removes the context’s graphics state from the top of the graphics state stack and makes the next graphics state the current graphics state.
- [func saveGraphicsState()](./savegraphicsstate%28%29-swift.method.md)
  Saves the current graphics state and creates a new graphics state on the top of the stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/savegraphicsstate()-swift.type.method)*
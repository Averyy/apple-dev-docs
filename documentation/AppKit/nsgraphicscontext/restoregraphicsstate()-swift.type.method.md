# restoreGraphicsState()

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Pops a graphics context from the per-thread stack, makes it current, and sends the context a restore graphics state message.

**Availability**:
- macOS

## Declaration

```swift
class func restoreGraphicsState()
```

```objc
+ (void) restoreGraphicsState;
```

## See Also

### Managing the Graphics State
- [func restoreGraphicsState()](./restoregraphicsstate%28%29-swift.method.md)
  Removes the context’s graphics state from the top of the graphics state stack and makes the next graphics state the current graphics state.
- [class func saveGraphicsState()](./savegraphicsstate%28%29-swift.type.method.md)
  Saves the graphics state of the current graphics context.
- [func saveGraphicsState()](./savegraphicsstate%28%29-swift.method.md)
  Saves the current graphics state and creates a new graphics state on the top of the stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/restoregraphicsstate()-swift.type.method)*
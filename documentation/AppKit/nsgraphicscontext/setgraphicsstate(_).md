# setGraphicsState(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Makes the graphics context of the specified graphics state current, and resets graphics state.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: This method has no effect

## Declaration

```swift
class func setGraphicsState(_ gState: Int)
```

```objc
+ (void) setGraphicsState:(NSInteger) gState;
```

## Discussion

The `graphicState` identifier must be created in the calling thread.

## See Also

### Deprecated methods
- [init(window: NSWindow)](./init%28window%29.md)
  Creates a new graphics context for drawing into a window.
- [init(graphicsPort: UnsafeMutableRawPointer, flipped: Bool)](./init%28graphicsport,flipped%29.md)
  Creates a new graphics context from the specified graphics port.
- [- focusStack](./focusstack.md)
  Returns the object used by the context to track the hierarchy of views with locked focus.
- [- setFocusStack:](./setfocusstack_.md)
  Sets the object used by the receiver to track the hierarchy of views with locked focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/setgraphicsstate(_:))*
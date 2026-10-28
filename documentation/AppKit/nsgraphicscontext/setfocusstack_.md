# setFocusStack:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the object used by the receiver to track the hierarchy of views with locked focus.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```objc
- (void) setFocusStack:(id) stack;
```

## Discussion

You should never need to get or modify the focus stack information. The use of focus stacks may be deprecated in a future release.

## Parameters

- `stack`: The object used by the graphics context for view-hierarchy tracking.

## See Also

### Deprecated methods
- [init(window: NSWindow)](./init%28window%29.md)
  Creates a new graphics context for drawing into a window.
- [init(graphicsPort: UnsafeMutableRawPointer, flipped: Bool)](./init%28graphicsport,flipped%29.md)
  Creates a new graphics context from the specified graphics port.
- [class func setGraphicsState(Int)](./setgraphicsstate%28_%29.md)
  Makes the graphics context of the specified graphics state current, and resets graphics state.
- [- focusStack](./focusstack.md)
  Returns the object used by the context to track the hierarchy of views with locked focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/setfocusstack:)*
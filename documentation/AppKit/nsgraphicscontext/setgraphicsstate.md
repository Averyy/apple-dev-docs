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

- [init(window: NSWindow)](nsgraphicscontext/init(window:).md)
  Creates a new graphics context for drawing into a window.
- [init(graphicsPort: UnsafeMutableRawPointer, flipped: Bool)](nsgraphicscontext/init(graphicsport:flipped:).md)
  Creates a new graphics context from the specified graphics port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/setgraphicsstate(_:))*
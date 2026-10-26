# Deprecated symbols

**Framework**: AppKit  
**Role**: API Collection

Review symbols that are no longer in active development, and their recommended replacements.

#### Overview

Although these symbols are available for use, Apple is no longer actively developing them, and may remove them in a future release. Apple recommends moving away from these symbols and using their indicated replacements instead. Check the individual symbol pages for the recommended replacements.

## Topics

### Deprecated methods
- [init(window: NSWindow)](./nsgraphicscontext/init%28window%29.md)
  Creates a new graphics context for drawing into a window.
- [init(graphicsPort: UnsafeMutableRawPointer, flipped: Bool)](./nsgraphicscontext/init%28graphicsport,flipped%29.md)
  Creates a new graphics context from the specified graphics port.
- [class func setGraphicsState(Int)](./nsgraphicscontext/setgraphicsstate%28_%29.md)
  Makes the graphics context of the specified graphics state current, and resets graphics state.
- [- focusStack](./nsgraphicscontext/focusstack.md)
  Returns the object used by the context to track the hierarchy of views with locked focus.
- [- setFocusStack:](./nsgraphicscontext/setfocusstack_.md)
  Sets the object used by the receiver to track the hierarchy of views with locked focus.
### Deprecated properties
- [var graphicsPort: UnsafeMutableRawPointer](./nsgraphicscontext/graphicsport.md)
  The low-level, platform-specific graphics context represented by the graphic port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext-deprecated-symbols)*
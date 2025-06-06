# context

**Framework**: AppKit  
**Kind**: property

The graphics context object used for generating output.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var context: NSGraphicsContext? { get }
```

#### Return Value

The graphics context object used for drawing during the operation.

## See Also

- [func createContext() -> NSGraphicsContext?](nsprintoperation/createcontext.md)
  Creates the graphics context object used for drawing during the operation.
- [func destroyContext()](nsprintoperation/destroycontext.md)
  Destroys the print operation’s graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintoperation/context)*
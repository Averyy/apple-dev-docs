# destroyContext()

**Framework**: AppKit  
**Kind**: method

Destroys the print operation’s graphics context.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func destroyContext()
```

#### Discussion

Do not invoke this method directly—it is invoked at the end of a print operation.

## See Also

- [var context: NSGraphicsContext?](nsprintoperation/context.md)
  The graphics context object used for generating output.
- [func createContext() -> NSGraphicsContext?](nsprintoperation/createcontext.md)
  Creates the graphics context object used for drawing during the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintoperation/destroycontext())*
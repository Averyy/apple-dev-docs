# createContext()

**Framework**: AppKit  
**Kind**: method

Creates the graphics context object used for drawing during the operation.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func createContext() -> NSGraphicsContext?
```

#### Return Value

The graphics context object used for drawing. This object is created using the settings from the receiver’s `NSPrintInfo` object.

#### Discussion

Do not invoke this method directly—it is invoked before any output is generated.

## See Also

- [var context: NSGraphicsContext?](nsprintoperation/context.md)
  The graphics context object used for generating output.
- [func destroyContext()](nsprintoperation/destroycontext.md)
  Destroys the print operation’s graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintoperation/createcontext())*
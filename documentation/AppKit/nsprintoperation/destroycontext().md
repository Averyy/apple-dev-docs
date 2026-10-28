# destroyContext()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Destroys the print operation’s graphics context.

**Availability**:
- macOS

## Declaration

```swift
func destroyContext()
```

```objc
- (void) destroyContext;
```

## Discussion

Do not invoke this method directly—it is invoked at the end of a print operation.

## See Also

### Managing the Drawing Context
- [var context: NSGraphicsContext?](./context.md)
  The graphics context object used for generating output.
- [func createContext() -> NSGraphicsContext?](./createcontext%28%29.md)
  Creates the graphics context object used for drawing during the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintoperation/destroycontext())*
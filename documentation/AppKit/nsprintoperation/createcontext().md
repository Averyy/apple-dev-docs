# createContext()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Creates the graphics context object used for drawing during the operation.

**Availability**:
- macOS

## Declaration

```swift
func createContext() -> NSGraphicsContext?
```

```objc
- (NSGraphicsContext *) createContext;
```

#### Return Value

The graphics context object used for drawing. This object is created using the settings from the receiver’s `NSPrintInfo` object.

#### Discussion

Do not invoke this method directly—it is invoked before any output is generated.

## See Also

### Managing the Drawing Context
- [var context: NSGraphicsContext?](./context.md)
  The graphics context object used for generating output.
- [func destroyContext()](./destroycontext%28%29.md)
  Destroys the print operation’s graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintoperation/createcontext())*
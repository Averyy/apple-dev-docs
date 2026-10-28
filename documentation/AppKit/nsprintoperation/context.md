# context

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The graphics context object used for generating output.

**Availability**:
- macOS

## Declaration

```swift
var context: NSGraphicsContext? { get }
```

```objc
@property (strong, readonly, nullable) NSGraphicsContext * context;
```

## Return Value

The graphics context object used for drawing during the operation.

## See Also

### Managing the Drawing Context
- [func createContext() -> NSGraphicsContext?](./createcontext%28%29.md)
  Creates the graphics context object used for drawing during the operation.
- [func destroyContext()](./destroycontext%28%29.md)
  Destroys the print operation’s graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintoperation/context)*
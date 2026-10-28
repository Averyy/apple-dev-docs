# isDrawingToScreen

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the drawing destination is the screen.

**Availability**:
- macOS

## Declaration

```swift
var isDrawingToScreen: Bool { get }
```

```objc
@property (readonly, getter=isDrawingToScreen) BOOL drawingToScreen;
```

## Discussion

[`true`](../../Swift/true.md) if the drawing destination is the screen. If the value of the property is [`false`](../../Swift/false.md) may mean that the drawing destination is a printer, but the destination may also be a PDF or EPS file. You can call [`attributes`](./attributes.md) to see if additional information is available about the drawing destination.

## See Also

### Testing the Drawing Destination
- [class func currentContextDrawingToScreen() -> Bool](./currentcontextdrawingtoscreen%28%29.md)
  Returns a Boolean value that indicates whether the current context is drawing to the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/isdrawingtoscreen)*
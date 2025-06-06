# isDrawingToScreen

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the drawing destination is the screen.

**Availability**:
- macOS ?+

## Declaration

```swift
var isDrawingToScreen: Bool { get }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/swift/true) if the drawing destination is the screen. If the value of the property is [`false`](https://developer.apple.com/documentation/swift/false) may mean that the drawing destination is a printer, but the destination may also be a PDF or EPS file. You can call [`attributes`](nsgraphicscontext/attributes.md) to see if additional information is available about the drawing destination.

## See Also

- [class func currentContextDrawingToScreen() -> Bool](nsgraphicscontext/currentcontextdrawingtoscreen.md)
  Returns a Boolean value that indicates whether the current context is drawing to the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/isdrawingtoscreen)*
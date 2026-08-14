# currentContextDrawingToScreen()

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value that indicates whether the current context is drawing to the screen.

**Availability**:
- macOS ?+

## Declaration

```swift
class func currentContextDrawingToScreen() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the current context is drawing to the screen, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

This convenience method is equivalent to sending [`isDrawingToScreen`](nsgraphicscontext/isdrawingtoscreen.md) to the result of [`current`](nsgraphicscontext/current.md).

## See Also

- [var isDrawingToScreen: Bool](nsgraphicscontext/isdrawingtoscreen.md)
  A Boolean value that indicates whether the drawing destination is the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/currentcontextdrawingtoscreen())*